from datetime import datetime

import redis
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from pytz import utc

redis_client = redis.Redis(host="localhost", port=6379, db=0)

jobstores = {
    "default": SQLAlchemyJobStore(url="sqlite:///jobs.sqlite"),
}
executors = {"default": ThreadPoolExecutor(100)}
scheduler = BlockingScheduler(executors=executors, timezone=utc)
LIMIT = 100000


def send_to_redis(job_name):
    redis_client.set(job_name, str(datetime.now()))


def send_nothing(job_name):
    print(job_name)


for i in range(LIMIT):
    scheduler.add_job(
        send_to_redis,
        "cron",
        kwargs={"job_name": f"job_{i}"},
        hour=6,
        minute=18,
        id=f"job_{i}",
        replace_existing=True,
        misfire_grace_time=60,
    )
scheduler.start()
