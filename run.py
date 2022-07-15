# -*- coding: utf-8 -*-
import json
import datetime
import random
import string
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

# from business.business_delete import business_delete
from business.business_prise import business_prise
from business.comment import comment
from business.comment_prise import comment_prise
from business.community import community
from business.reader import reader

from care.care_comment import care_comment
from care.care_delete import care_delete

from medal.medal_check import medal_check
from medal.medal_reader import medal_reader

from settings import (QRCODE_PATH, COOKIE_FILE_PATH, CORPID, JOB_NUMBER, BUSINESS_SEC_ID, BUSINESS_TYPE, CHANNEL_ID,
                        JOB_DELAY_TIME, JOB_HOUR, JOB_MINUTE, ROLE_PERSON_ID)


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
    # 每日任务
    logger.debug("每日任务已开启...")

    _cookies = read_cookie(COOKIE_FILE_PATH)
    _corpid = CORPID
    delay = JOB_DELAY_TIME

    # 签到
    logger.debug('"签到"任务已开启...')
    try:
        is_sign_in(_corpid, _cookies)
        sleep(delay)
        get_sign_in(_corpid, _cookies)
        sleep(delay)
        post_sign_in(_corpid, _cookies)
        logger.debug('"每日签到"任务已完成...')
    except json.JSONDecodeError as e:
        logger.debug('"签到"任务失败, 需要重新登录, Error：', e)
        # 清除cookie, 重新登录
        clear_cookie(COOKIE_FILE_PATH)
        input()

    try:
        # 阅读勋章
        medals = medal_check(corpid=_corpid, cookies=_cookies)
        for medal_id in medals:
            medal_reader(medal_id=medal_id, corpid=_corpid, cookies=_cookies)

        # 每日动态
        logger.debug("每日动态已开启...")
        for index in range(1, JOB_NUMBER+1):
            # 生成指定长度的随机字符串
            text = ''.join(random.sample(string.ascii_letters + string.digits, 20))
            # 标题
            title = text
            # 内容
            content = text
            # 消息摘要
            content_summary = text
            # 评论内容 ≥10字
            comment_content = text

            business_id = community(title=title, content=content, content_summary=content_summary,
                                    role_person_id=ROLE_PERSON_ID, channel_id=CHANNEL_ID, corpid=_corpid, cookies=_cookies)
            logger.debug("business_id: ", business_id)
            sleep(delay)

            reader(business_id, _corpid, _cookies)
            sleep(delay)

            comment_id = comment(business_id=business_id, business_type=BUSINESS_TYPE,
                                    content=comment_content, corpid=_corpid, cookies=_cookies)
            logger.debug("comment_id", comment_id)
            sleep(delay)

            business_prise(business_id=business_id, business_type=BUSINESS_TYPE,
                            business_sec_id=BUSINESS_SEC_ID, corpid=_corpid, cookies=_cookies)
            sleep(delay)

            comment_prise(comment_id=comment_id,
                            corpid=_corpid, cookies=_cookies)
            # sleep(delay)
            # business_delete(business_id=business_id,
            #                 corpid=_corpid, cookies=_cookies)
            logger.debug(f"已完成动态任务次数: {index}")


        # 送祝福
        staff_id = ROLE_PERSON_ID
        logger.debug('"送祝福" 已开启...')
        # try:
        for index in range(1, 3+1):
            comment_id = care_comment(staff_id, _corpid, _cookies)
            sleep(delay)
            care_delete(comment_id, _corpid, _cookies)
            logger.debug(f"已完成动态任务次数: {index}")
        logger.debug('"送祝福"任务已完成...')
        # except json.JSONDecodeError as e:
        #     logger.debug('"签到"任务失败，Error：', e)
        #     input()


    except json.JSONDecodeError as e:
        logger.debug("执行任务失败，Error：", e)
        # clear_cookie(COOKIE_FILE_PATH)
        input()

    logger.debug("每日任务, 已完成.")
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    strtomorrow = tomorrow.strftime('%Y-%m-%d')
    logger.debug(f"下次执行时间：{strtomorrow} {JOB_HOUR}:{JOB_MINUTE}")


if __name__ == '__main__':
    # job()
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
