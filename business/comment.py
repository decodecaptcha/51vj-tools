# -*- coding: utf-8 -*-
import json
import time
import requests
from loguru import logger


def comment(business_id, business_type, content, corpid, cookies):
    """评论动态

    :param business_id: 动态id
    :param content: 评论内容 ≥10字
    :param corpid:
    :param cookies:
    :return: comment_id 评论id
    """
    timestamp = int(time.time() * 1000)
    _content = content

    url = f'https://qy.51vj.cn/userpreference/comment/'
    params = {
        '_': f'{timestamp}',
        '_v': '1.2.7',
        'app-id': '31',
        'corpid': f'{corpid}',
        'appid': '31',
        'parentid': '1002',
        'business-id': f'{business_id}',
        'business-type': f'{business_type}',
        'business-sec-id': '0',
        'comment-content': f'{_content}',
        'is-anonymity': '0',
        'images': '',
        'remind-roles': ''
    }
    payload = {}
    headers = {
        'Accept': 'application/json;charset=utf-8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }

    response = requests.post(
        url, params=params, headers=headers, cookies=cookies, data=payload)

    logger.debug(response.text)
    json_data = json.loads(response.text)
    commentRecord = json_data.get("commentRecord")[0]
    comment_id = commentRecord.get("id")
    return comment_id
