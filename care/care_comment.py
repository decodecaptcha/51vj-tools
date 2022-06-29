# -*- coding: utf-8 -*-
import json
import requests
from loguru import logger


def care_comment(staff_id, corpid, cookies):
    """送祝福"""
    url = 'https://qy.51vj.cn/care/comment/v2'
    params = {
        'corpid': f'{corpid}',
        'appid': '33',
    }

    payload = "{\"staff_id\":\"" + staff_id + \
        "\",\"record_year\":\"\",\"business_type\":\"1\",\"comment_content\":\"生日快乐！愿你永远做特别的自己~\",\"gift_id\":75}"
    payload = payload.encode('utf-8')

    # 员工编号
    # <清凉西瓜> 礼物编号
    headers = {
        "Accept": "application/json",
        "Accept-Wncoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    }
    response = requests.post(
        url, params=params, headers=headers, cookies=cookies, data=payload)
    logger.debug(response.text)
    # logger.debug(response.status_code)
    json_data = json.loads(response.text)
    comment_id = json_data.get("comment").get("id")
    return comment_id
