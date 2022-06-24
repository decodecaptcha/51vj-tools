# -*- coding: utf-8 -*-
import json
import datetime
from logging import exception
from time import sleep
from apscheduler.schedulers.blocking import BlockingScheduler
from loguru import logger

from login.a_qrConnect import qrConnect
from login.b_qrImg import qrImg
from login.c_login_auth_code import login_auth_code
from login.d_login_cookies import login_cookies
from login.show import Show

from sign_in.get_sign_in import get_sign_in
from sign_in.is_sign_in import is_sign_in
from sign_in.post_sign_in import post_sign_in

from business.business_delete import business_delete
from business.business_prise import business_prise
from business.comment import comment
from business.comment_prise import comment_prise
from business.community import community
from business.reader import reader

from settings import (QRCODE_PATH, COOKIE_FILE_PATH, CORPID, JOB_NUMBER, BUSINESS_SEC_ID, BUSINESS_TYPE, CHANNEL_ID,
                      COMMENT_CONTENT, JOB_DELAY_TIME, JOB_HOUR, JOB_MINUTE,
                      ROLE_PERSON_ID)


print(r"""
 ____  _       _     _              _     
| ___|/ |_   _(_)   | |_ ___   ___ | |___ 
|___ \| \ \ / / |   | __/ _ \ / _ \| / __|
 ___) | |\ V /| |   | || (_) | (_) | \__ \
|____/|_| \_/_/ |    \__\___/ \___/|_|___/
            |__/                          
author: aiden2048                                     
address: https://github.com/aiden2048
""")


def read_file(abspath):
    try:
        with open(abspath, 'r') as f:
            text = f.read()
            return text
    except Exception as e:
        logger.debug(e)
        return None


def write_file(abspath, data: str):
    try:
        with open(abspath, 'w') as f:
            f.write(data)
    except Exception as e:
        logger.debug(e)
        return None


def read_cookie(abspath):
    text = read_file(abspath)
    dict_data = json.loads(text)
    logger.debug(f'read_file: {abspath}, text: {text}, status: successful')
    return dict_data


def write_cookie(abspath, dict_data: dict):
    data = json.dumps(dict_data)
    write_file(abspath, data)
    logger.debug(f'write_cookie: {abspath}, status: successful')


def clear_cookie(abspath):
    """清除过期的cookie"""
    dict_data = ''
    write_file(abspath, dict_data)


def login():
    corpid = CORPID
    show = Show()
    key = qrConnect(corpid)
    content = qrImg(key)
    show.save_img(content, QRCODE_PATH)
    show.show_img(QRCODE_PATH)

    logger.debug('请使用企业微信扫描二维码登录 “微加”')
    auth_code = ''

    # 轮询规则: 每x秒轮询一次
    while 1:
        callback = login_auth_code(key, corpid)

        # 未扫码 {"status":"QRCODE_SCAN_NEVER","auth_code":""}
        if callback.get("status") == "QRCODE_SCAN_NEVER":
            logger.debug('请使用企业微信扫描二维码登录 “微加”')
            sleep(2)

        # 未扫码, 当前二维码已过期 {"status":"QRCODE_SCAN_ERR","auth_code":""}
        elif callback.get("status") == "QRCODE_SCAN_ERR":
            logger.debug('当前二维码已过期, 请重启')
            break

        # 已扫码 {"status":"QRCODE_SCAN_ING","auth_code":""}
        elif callback.get("status") == "QRCODE_SCAN_ING":
            logger.debug('扫描成功, 请在企业微信中点击确认即可登录')
            sleep(2)

        # 已扫码, 已确认登录 {"status":"QRCODE_SCAN_SUCC","auth_code":"xxxxxxxxxxx"}
        elif callback.get("status") == "QRCODE_SCAN_SUCC":
            auth_code = callback.get("auth_code")
            logger.debug('登录成功')
            break

        # 未知 callback {}
        else:
            logger.debug(f'未知 callback : callback = {callback}')
            break

    show.close_img()

    cookies = login_cookies(auth_code, corpid) or {}
    logger.debug(f'cookies: {cookies}')
    write_cookie(COOKIE_FILE_PATH, cookies)


def job():
    _cookies = read_cookie(COOKIE_FILE_PATH)
    _corpid = CORPID
    delay = JOB_DELAY_TIME

    # 每日签到
    logger.debug("每日签到任务已开启...")
    try:
        is_sign_in(_corpid, _cookies)
        sleep(delay)
        get_sign_in(_corpid, _cookies)
        sleep(delay)
        post_sign_in(_corpid, _cookies)
        logger.debug("每日签到任务已完成...")
    except json.JSONDecodeError as e:
        logger.debug("每日签到任务失败，Error：", e)
        clear_cookie(COOKIE_FILE_PATH)
        input()

    # 每日动态
    logger.debug("每日动态任务已开启...")
    try:
        for index in range(1, JOB_NUMBER+1):
            role_person_id = ROLE_PERSON_ID
            channel_id = CHANNEL_ID
            business_id = community(role_person_id, channel_id, _corpid, _cookies)
            logger.debug("business_id: ", business_id)
            sleep(delay)

            reader(business_id, _corpid, _cookies)
            sleep(delay)

            comment_content = COMMENT_CONTENT
            comment_id = comment(business_id, comment_content, _corpid, _cookies)
            logger.debug("comment_id", comment_id)
            sleep(delay)

            business_type = BUSINESS_TYPE
            business_sec_id = BUSINESS_SEC_ID
            business_prise(business_id, business_type,
                            business_sec_id, _corpid, _cookies)
            sleep(delay)

            comment_prise(comment_id, _corpid, _cookies)
            sleep(delay)

            business_delete(business_id, _corpid, _cookies)
            logger.debug(f"已完成动态任务次数: {index}")
    except json.JSONDecodeError as e:
        logger.debug("每日动态任务失败，Error：", e)
        clear_cookie(COOKIE_FILE_PATH)
        input()

    logger.debug("每日任务, 已完成.")
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    strtomorrow = tomorrow.strftime('%Y-%m-%d')
    logger.debug(f"下次执行时间：{strtomorrow} {JOB_HOUR}:{JOB_MINUTE}")


if __name__ == '__main__':
    
    logger.debug("==================== 程序启动...")
    if not read_file(COOKIE_FILE_PATH):
        logger.debug("登录状态: 检测到未登录...")
        login()
    logger.debug("登录状态: 检测到已登录...")
    logger.debug(f"定时任务: 已开启...")
    logger.debug(f"执行时间: 每日 {JOB_HOUR}:{JOB_MINUTE}")
    scheduler = BlockingScheduler()
    scheduler.add_job(job, 'cron', hour=JOB_HOUR, minute=JOB_MINUTE)
    scheduler.start()