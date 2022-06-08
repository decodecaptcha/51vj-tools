# -*- coding: utf-8 -*-
import re
import requests
from loguru import logger


def qrConnect(corpid):
    """二维码
    
    :param wxd_appid: _description_
    :return: _description_
    """
    redirect_uri = f'https://qy.51vj.cn/wechat/login?goto=https://qy.51vj.cn/app/home/culture?corpid={corpid}&appid=1002&corpid={corpid}&appid=1002&corpid={corpid}&appid=1002'
    url = 'https://open.work.weixin.qq.com/wwopen/sso/3rd_qrConnect'
    params = {
        'appid': 'wxd1165b872e863a03',
        'redirect_uri': f'{redirect_uri}',
        'state': 'pcBrowserWechatLogin',
        'usertype': 'member',
    }
    payload = {}
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Referer': 'https://qy.51vj.cn/', # Referer 必须携带
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }

    response = requests.get(url, params=params, headers=headers, data=payload)
    result = re.findall(r'"key":"(.*?)"', response.text)
    key =  result[0] if result else ''
    logger.debug(f"key: {key}")
    return key