# -*- coding: utf-8 -*-
import time
import requests
from loguru import logger
# from settings import CORPID, USER_COOKIES

def business_delete(business_id, corpid, cookies):
    """删除动态

    :param business_id: _description_
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
        'Content-Type': 'application/json',
        'Connection': 'keep-alive',
        # 'cookie': _cookie,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }
    url = 'https://qy.51vj.cn/club/'
    params = {
        '_': f'{timestamp}',
        '_v': '1.2.7',
        'corpid': f'{corpid}',
        'appid': '31',
        'parentid': '1002',
        'ids': f'{business_id}'
    }

    payload = {}
    response = requests.delete(url=url, params=params,
                                headers=headers, cookies=cookies, data=payload)
    logger.debug(response.text)


# if __name__ == '__main__':
#     business_id = 'xxxxxx'
#     business_delete(business_id)

# 成功响应:
# {"success": true,"msg": "删除成功"}
