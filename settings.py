# -*- coding: utf-8 -*-
# settings.py

# --------------- 登录账号(必填, 根据自己 企业微信 账号填写) --------------- #
# 企业微信相关的ID 
CORPID = 'wp58xxxxxxxxxxx_xxx-xxx_x_xxxxEg'

# 登录账号获取 cookie (必填项)
USER_COOKIES = 'rememberme-wp58xxxxxxxxxxx_xxx-xxx_x_xxxxEg=xxx; JSESSIONID=wp58xxxxxxxxxxx_xxx-xxx_x_xxxxEg_xxx'

# 自己的 id, 设置仅自己可见 (必填项)
ROLE_PERSON_ID = '24xxxxx1'


# --------------- 发布动态 (一般不修改) --------------- #
# 话题 id, 如 932765 对应话题 "吃瓜群众"
CHANNEL_ID = '932765'

# 评论内容 ≥10字
COMMENT_CONTENT = '测试测试测试测试测试测试测试测试'

# 目标动态的类型
BUSINESS_TYPE = '40501'

# 目标动态的第 x 条评论 x=0 表示第一条评论
BUSINESS_SEC_ID = '0'


# --------------- 定时任务 (一般不修改) --------------- #
# 任务之间间隔时间
JOB_DELAY_TIME = 10

# 任务次数, 默认执行3次, 详情查看《积分规则.html》
JOB_NUMBER = 3

# 默认是每天的10：30 分执行任务(24小时制, 可自定义)
JOB_HOUR = 10
JOB_MINUTE = 30
