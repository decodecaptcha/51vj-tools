# 查询结果
import time
import requests
from loguru import logger
# from settings import CORPID, USER_COOKIES


def get_sign_in(corpid, cookies):
    timestamp = int(time.time() * 1000)
    # corpid = CORPID
    # _cookie = USER_COOKIES
    url = 'https://qy.51vj.cn/club/sign-in'
    params = {
        '_': f'{timestamp}',
        '_v': '1.2.7',
        'corpid': f'{corpid}',
        'appid': '31',
        'parentid': '1002'
    }
    payload = {}
    headers = {
        'Accept': 'application/json;charset=utf-8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        # 'cookie': cookie,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }
    response = requests.get(url, params=params, headers=headers, cookies=cookies, data=payload)

    logger.debug(response.text)


# if __name__ == '__main__':
#     get_sign_in()


# {"success": true,"code": 1,"sign_in_record": {"max_sign_in_day": 3,"continue_sign_in_day": 3,"record_details": [{"time": "2022-06-01 12:25:52","create_time": "2022-06-01 12:25:52"},{"time": "2022-06-02 09:41:42","create_time": "2022-06-02 09:41:42"},{"time": "2022-06-04 13:08:45","create_time": "2022-06-04 13:08:45"},{"time": "2022-06-05 00:47:32","create_time": "2022-06-05 00:47:32"},{"time": "2022-06-06 09:46:09","create_time": "2022-06-06 09:46:09"}],"need_continue_sign_in_day": 4}}
