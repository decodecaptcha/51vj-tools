# -*- coding: utf-8 -*-
import requests
from loguru import logger


def login_cookies(auth_code, corpid):
    """_summary_

    :param auth_code: 从 login_qrConnect 接口获取 auth_code
    :return: cookies
    """
    url = 'https://qy.51vj.cn/wechat/login'
    params = {
        'goto': f'https://qy.51vj.cn/app/home/culture?corpid={corpid}&appid=1002&corpid={corpid}&appid=1002',
        'corpid': corpid,
        'appid': '1002',
        'auth_code': auth_code,
        'state': 'pcBrowserWechatLogin',
        'appid': 'wxd1165b872e863a03'
    }
    payload = {}
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Referer': 'https://open.work.weixin.qq.com/',  # Referer 必须携带
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }

    response = requests.get(
        url, params=params, headers=headers, data=payload, allow_redirects=False)
    logger.debug(response.status_code)  # 状态码 302 是成功状态, 需要禁止重定向
    logger.debug(response.text)
    logger.debug(response.cookies.get_dict())

    return response.cookies.get_dict()
