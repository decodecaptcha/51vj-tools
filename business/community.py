# -*- coding: utf-8 -*-
import json
import time
import requests
from loguru import logger


def community(role_person_id, channel_id, corpid, cookies):
    """发布动态

    :param role_person_id: 自己的 id, 设置仅自己可见
    :param channel_id: 话题 id, 如 932765 对应话题 "吃瓜群众"
    :param corpid:
    :param cookies:
    :return: 动态 id 
    """
    timestamp = int(time.time() * 1000)

    params = {
        '_': f'{timestamp}',
        '_v': '1.2.7',
        'corpid': f'{corpid}',
        'appid': '31',
        'parentid': '1002',
        'top': 'false',
        'ismanager': '0'
    }

    headers = {
        'Accept': 'application/json;charset=utf-8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Content-Type': 'application/json',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }

    url = 'https://qy.51vj.cn/club/'

    payload = json.dumps({
        "title": "测试标题",
        "content": "<p>测试内容</p>",
        "roles": [
            # 仅对某人开放动态, 设置本人唯一id, 如 "id": 24xxxxx1
            f"ROLE_PERSON_{role_person_id}"
        ],
        "remind_roles": [],
        "push_cover": [],
        "is_broadcast": 0,
        "push_date": None,
        "images": [],
        "files": [],
        "is_anonymous_publication": 1,
        "channel_id": f'{channel_id}',
        "is_anonymous_comment": 1,
        "allow_share": 0,
        "tags": [],
        "links": [],
        "wechat_of_pc": 1,
        "content_type": 1,
        "content_summary": "测试内容\n"
    })

    response = requests.put(
        url, params=params, headers=headers, cookies=cookies, data=payload)
    logger.debug(response.text)
    json_data = json.loads(response.text)
    business_id = json_data.get("community").get("id")
    return business_id
