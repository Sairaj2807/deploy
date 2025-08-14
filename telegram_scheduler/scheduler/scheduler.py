import pytz
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, time
from .models import ScheduledMessage
from .telegram_utils import send_telegram

def send_scheduled_messages():
    now = datetime.now(pytz.timezone("Asia/Singapore")).time()

    for msg in ScheduledMessage.objects.filter(sent=False):
        if now.hour == msg.send_time.hour and now.minute == msg.send_time.minute:
            send_telegram(msg)
            msg.sent = True
            msg.save()

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_scheduled_messages, 'interval', minutes=1)
    scheduler.start()
