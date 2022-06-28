# -*- coding: utf-8 -*-
import os

# --------------- 登录账号(根据自己 企业微信 账号填写) --------------- #

# 企业微信相关的ID (必填项)
CORPID = 'XXXXXXXXXXXXXXXXXXXX_XXXXXXXXXX_XXXXXX'

# 自己的 id, 设置仅自己可见 (必填项)
ROLE_PERSON_ID = '244XXXXXXX'

# 二维码保存路径
QRCODE_PATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 'login', 'qrcode', 'qrcode.png'))

# cookies 保存路径
COOKIE_FILE_PATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 'login', 'cookie', 'cookie.txt'))


# --------------- 定时任务 (可修改) --------------- #
# 默认是每天的9：30 分执行任务(24小时制, 可自定义)
JOB_HOUR = 9
JOB_MINUTE = 30

# 任务次数, 默认执行3次, 详情查看 images/《积分规则.html》
JOB_NUMBER = 3

# 任务之间间隔时间
JOB_DELAY_TIME = 5


# --------------- 发布动态 (一般不修改) --------------- #
# 话题 id, 如 932765 对应话题 "吃瓜群众"
CHANNEL_ID = '932765'

# 目标动态的类型
BUSINESS_TYPE = '40501'

# 目标动态的第 x 条评论 x=0 表示第一条评论
BUSINESS_SEC_ID = '0'