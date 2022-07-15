import time
import requests

# url = "https://qy.51vj.cn/medal/record?_=1656656582691&_v=1.0.12&corpid=wp58yYCQAAA2tAN_zvV-Thr_b_JDPqEg&appid=65&parentid=1002&type=&page=1&size=15"

# payload={}
# headers = {
#   'accept': ' application/json;charset=utf-8',
#   'accept-encoding': ' gzip, deflate, br',
#   'accept-language': ' zh-CN,zh;q=0.9,en;q=0.8',
#   'cache-control': ' no-cache',
#   'cookie': ' rememberme-wp58yYCQAAA2tAN_zvV-Thr_b_JDPqEg=d281OHlZQ1FBQXdPanpHRjFpcVpaOFE1TVVObzJ5WVFAMjYzNTIwOjE2NTcyNjEzMjk0NDY6YWVkZDg1ODU0YTY4OGE0NmVjN2NhNjg4ZDA5MWEwZjI; JSESSIONID=wp58yYCQAAA2tAN---zvV-Thr---b---JDPqEg_cb695491-7cab-41d4-bf4a-dc740d1268a2',
#   'pragma': ' no-cache',
#   'referer': ' https://qy.51vj.cn/app/medal/home/list/all?appid=65&corpid=wp58yYCQAAA2tAN_zvV-Thr_b_JDPqEg&parentid=1002',
#   'sec-ch-ua': ' "Chromium";v="21", " Not;A Brand";v="99"',
#   'sec-ch-ua-mobile': ' ?0',
#   'sec-ch-ua-platform': ' "Windows"',
#   'sec-fetch-dest': ' empty',
#   'sec-fetch-mode': ' cors',
#   'sec-fetch-site': ' same-origin',
#   'user-agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
# }

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)



# -*- coding: utf-8 -*-
import json
import requests
from loguru import logger


def medal_check(corpid, cookies):
    """查询勋章列表

    :param corpid: _description_
    :param cookies: _description_
    """
    url = 'https://qy.51vj.cn/medal/record'
    timestamp = int(time.time() * 1000)
    params = {
        '_': f'{timestamp}',
        '_v': '1.0.12',
        'corpid': f'{corpid}',
        'appid': '56',
        'parentid': '1002',
        'type': '',
        'page': '1',
        'size': '15'
    }

    headers = {
        "Accept": "application/json",
        "Accept-Wncoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    }
    response = requests.get(url, params=params, headers=headers, cookies=cookies)
    logger.debug(response.text)
    medals = []
    json_data = json.loads(response.text)
    medal_records = json_data.get("medal_records")
    # 取 top 2
    for medal_record in medal_records[:2]:
        medals.append(medal_record.get("id"))
    return medals