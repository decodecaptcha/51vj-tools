# -*- coding: utf-8 -*-
import time

from apscheduler.schedulers.blocking import BlockingScheduler
from loguru import logger

from business.business_delete import business_delete
from business.business_prise import business_prise
from business.comment import comment
from business.comment_prise import comment_prise
from business.community import community
from business.reader import reader
from settings import (BUSINESS_SEC_ID, BUSINESS_TYPE, CHANNEL_ID,
                        COMMENT_CONTENT, JOB_DELAY_TIME, JOB_HOUR, JOB_MINUTE,
                        ROLE_PERSON_ID)


def job():
    delay = JOB_DELAY_TIME
    role_person_id = ROLE_PERSON_ID
    channel_id = CHANNEL_ID
    business_id = community(role_person_id, channel_id)
    logger.debug("business_id: ", business_id)
    time.sleep(delay)

    reader(business_id)
    time.sleep(delay)

    comment_content = COMMENT_CONTENT
    comment_id = comment(business_id, comment_content)
    logger.debug("comment_id", comment_id)
    time.sleep(delay)

    business_type = BUSINESS_TYPE
    business_sec_id = BUSINESS_SEC_ID
    business_prise(business_id, business_type, business_sec_id)
    time.sleep(delay)

    comment_prise(comment_id)
    time.sleep(delay)

    business_delete(business_id)
    logger.debug("每日任务, 已完成...")


if __name__ == '__main__':
    # 定时任务
    logger.debug("定时任务已开启...")
    scheduler = BlockingScheduler()
    scheduler.add_job(job, 'cron', hour=JOB_HOUR, minute=JOB_MINUTE)
    scheduler.start()
