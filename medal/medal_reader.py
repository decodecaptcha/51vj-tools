# -*- coding: utf-8 -*-
import json
import time
import requests
from loguru import logger

# url = "https://qy.51vj.cn/medal/record/32764?_=1656657488328&_v=1.0.12&corpid=wp58yYCQAAA2tAN_zvV-Thr_b_JDPqEg&appid=65&parentid=1002"

def medal_reader(medal_id, corpid, cookies):
    """阅读勋章"""
    url = f'https://qy.51vj.cn/medal/record/{medal_id}'
    timestamp = int(time.time() * 1000)
    params = {
        '_': f'{timestamp}',
        '_v': '1.0.12',
        'corpid': f'{corpid}',
        'appid': '56',
        'parentid': '1002'
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