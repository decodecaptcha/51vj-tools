# -*- coding: utf-8 -*-
import json
import time
import requests
from loguru import logger
from settings import CORPID


def login_auth_code(key):
    """_summary_

    :param key: _description_
    :return: callback {"status":"QRCODE_SCAN_xxx","auth_code":"xxx"}
    """
    timestamp = int(time.time() * 1000)
    corpid = CORPID
    goto = f'https://qy.51vj.cn/app/home/culture?corpid={corpid}&appid=1002&corpid={corpid}&appid=1002'
    redirect_uri = f'https://qy.51vj.cn/wechat/login?goto={goto}&corpid={corpid}&appid=1002'
    url = 'https://open.work.weixin.qq.com/wwopen/sso/l/qrConnect'
    params = {
        'callback': 'jsonpCallback',
        'key': key,
        'redirect_uri': redirect_uri,
        'appid': 'wxd1165b872e863a03',
        '_': f'{timestamp}'
    }
    payload = {}
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Referer': 'https://open.work.weixin.qq.com/', # Referer 必须携带
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }

    response = requests.get(url, params=params, headers=headers, data=payload)
    logger.debug(response.status_code)
    logger.debug(response.text)

    data =  response.text[14:-1] if response.text else {}
    callback = json.loads(data)
    return callback


# if __name__ == '__main__':
#     key = 'a3a278502a4c5bf3'
#     auth_code = login_auth_code(key)
#     print(auth_code)

# 轮询规则: 每5秒轮询一次 login_qrConnect

# 未扫码
# jsonpCallback({"status":"QRCODE_SCAN_NEVER","auth_code":""})

# 未扫码, 当前二维码已过期
# jsonpCallback({"status":"QRCODE_SCAN_ERR","auth_code":""})

# 已扫码
# jsonpCallback({"status":"QRCODE_SCAN_ING","auth_code":""})

# 已扫码, 已确认登录
# jsonpCallback({"status":"QRCODE_SCAN_SUCC","auth_code":"xxxxxxxxxxx"})



# 若返回 
# "status":"QRCODE_SCAN_SUCC"
# "auth_code":"加密参数"
# 代表 app端 验证成功
# 则提取 auth_code
