# -*- coding: utf-8 -*-
import json
import requests
from loguru import logger


def care_delete(comment_id, corpid, cookies):
    url = 'https://qy.51vj.cn/care/comment/delete'
    params = {
        'id': f'{comment_id}',
        'corpid': f'{corpid}',
        'appid': '33',
    }
    headers = {
        "Accept": "application/json",
        "Accept-Wncoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    }
    response = requests.post(
        url, params=params, headers=headers, cookies=cookies)
    json.loads(response.text)
    logger.debug(response.text)