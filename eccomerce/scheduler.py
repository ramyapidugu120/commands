# eccomerce/scheduler.py
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from .tasks import send_daily_email
# import logging

# logger = logging.getLogger(__name__)

def start():
    scheduler = BackgroundScheduler()

    # Log when the scheduler starts
    # logger.info("Scheduler started")

    # Schedule the job to run every minute (for testing)
    scheduler.add_job(
        send_daily_email,
        CronTrigger(hour='12',minute='0'),  # This will run the task every minute
        name='every-minute-email-task',
        replace_existing=True,
    )

    scheduler.start()
    # logger.info("Email job scheduled to run every minute")
