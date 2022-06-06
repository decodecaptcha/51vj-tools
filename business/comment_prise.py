# -*- coding: utf-8 -*-
import time
import requests
from loguru import logger
from settings import CORPID, USER_COOKIES


def comment_prise(comment_id):
    """点赞评论

    :param comment_id: _description_
    """
    timestamp = int(time.time() * 1000)
    corpid = CORPID
    _cookie = USER_COOKIES
    headers = {
        'Accept': 'application/json;charset=utf-8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection': 'keep-alive',
        'cookie': _cookie,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }

    url = f'https://qy.51vj.cn/userpreference/comment/prise/{comment_id}'
    params = {
        '_': f'{timestamp}',
        '_v': '1.2.7',
        'app-id': '31',
        'corpid': f'{corpid}',
        'appid': '31',
        'parentid': '1002'
    }

    payload = {}
    response = requests.post(url, params=params, headers=headers, data=payload)

    logger.debug(response.text)


# if __name__ == '__main__':
#     comment_id = '47xxxx7'
#     comment_prise(comment_id)

# 成功响应:
# {"success": true,"code": 1}
