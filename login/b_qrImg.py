# -*- coding: utf-8 -*-
import requests
from loguru import logger


def qrImg(key):
    """二维码

    :param key: _description_
    """
    url = f'https://open.work.weixin.qq.com/wwopen/sso/qrImg'
    params = {
        'key': key
    }
    payload = {}
    headers = {
        'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }

    response = requests.get(url, params=params, headers=headers, data=payload)
    logger.debug(response.status_code)
    return response.content

    


# if __name__ == '__main__':
#     key = '357236e854ffaf23'
#     content = qrImg(key)
#     # plt.imshow(plt.imread(BytesIO(content)))
#     # plt.axis('off')
#     # plt.show()

#     img = Image.open(BytesIO(content))
#     plt.imshow(img)
#     plt.axis('off')
#     # block=False 开启交互模式
#     plt.show(block=False)
#     input()
#     plt.close()


