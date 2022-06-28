# -*- coding: utf-8 -*-
import time
import requests
from loguru import logger

# 删除动态-10分， 以后不再删除
# def business_delete(business_id, corpid, cookies):
#     """删除动态

#     :param business_id: _description_
#     :param corpid:
#     :param cookies:
#     """
#     timestamp = int(time.time() * 1000)

#     headers = {
#         'Accept': 'application/json;charset=utf-8',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'Accept-Language': 'zh-CN,zh;q=0.9',
#         'Content-Type': 'application/json',
#         'Connection': 'keep-alive',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
#     }
#     url = 'https://qy.51vj.cn/club/'
#     params = {
#         '_': f'{timestamp}',
#         '_v': '1.2.7',
#         'corpid': f'{corpid}',
#         'appid': '31',
#         'parentid': '1002',
#         'ids': f'{business_id}'
#     }

#     payload = {}
#     response = requests.delete(url=url, params=params,
#                                headers=headers, cookies=cookies, data=payload)
#     logger.debug(response.text)