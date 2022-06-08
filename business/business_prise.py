# -*- coding: utf-8 -*-
import time
import requests
from loguru import logger
# from settings import CORPID, USER_COOKIES


def business_prise(business_id, business_type, business_sec_id, corpid, cookies):
    """点赞动态

    :param business_id: _description_
    :param business_type: _description_
    :param business_sec_id: _description_
    :param corpid:
    :param cookies:
    """
    timestamp = int(time.time() * 1000)
    # corpid = CORPID
    # _cookie = USER_COOKIES

    headers = {
        'Accept': 'application/json;charset=utf-8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection': 'keep-alive',
        # 'cookie': _cookie,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }

    url = f'https://qy.51vj.cn/userpreference/prise/'
    params = {
        '_': f'{timestamp}',
        '_v': '1.2.7',
        'app-id': '31',
        'corpid': f'{corpid}',
        'appid': '31',
        'parentid': '1002',
        'business-id': f'{business_id}',
        'business-type': f'{business_type}',
        'business-sec-id': f'{business_sec_id}',
        'status': '1'
    }
    payload = {}
    response = requests.put(url, params=params, headers=headers, cookies=cookies, data=payload)

    logger.debug(response.text)


# if __name__ == '__main__':
#     business_id = 'xxxxxx'
#     business_type = '40501'
#     business_sec_id = '0'
#     business_prise(business_id, business_type, business_sec_id)

# 成功响应:
# {"success": true,"msg": "点赞成功","priseRecord": [...}
