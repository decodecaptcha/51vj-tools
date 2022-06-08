# -*- coding: utf-8 -*-
import json
import time
import requests
from loguru import logger
# from settings import CORPID, USER_COOKIES


def comment(business_id, content, corpid, cookies):
    """评论动态

    :param business_id: 动态id
    :param content: 评论内容 ≥10字
    :param corpid:
    :param cookies:
    :return: comment_id 评论id
    """
    timestamp = int(time.time() * 1000)
    # corpid = CORPID
    # _cookie = USER_COOKIES
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
        'business-type': '40501',
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
        # 'cookie': _cookie,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }

    response = requests.post(url, params=params, headers=headers, cookies=cookies, data=payload)

    logger.debug(response.text)
    json_data = json.loads(response.text)
    commentRecord = json_data.get("commentRecord")[0]
    comment_id = commentRecord.get("id")
    return comment_id


# if __name__ == '__main__':
#     business_id = '7xxxx2'
#     comment_content = '测试测试测试测试测试测试测试测试测试测试测试4'
#     comment_id = comment(business_id, comment_content)
#     print("comment_id", comment_id)


# {"success": true,"msg": "评论成功", ...}
