# 查询结果
import time
import requests
from loguru import logger
# from settings import CORPID, USER_COOKIES


def post_sign_in(corpid, cookies):
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
    response = requests.post(url, params=params, headers=headers, cookies=cookies,data=payload)

    logger.debug(response.text)


# if __name__ == '__main__':
#     post_sign_in()

# {"success": true,"code": 1,"sign_in_record": {}}
