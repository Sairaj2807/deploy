import pytz
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from django.utils import timezone
from .models import ScheduledMessage
from .telegram_utils import send_telegram
import logging
import threading

logger = logging.getLogger(__name__)

# ---- GLOBAL FLAGS ----
scheduler_started = False
sending_lock = threading.Lock()
recently_sent = set()  # store msg.id recently sent to avoid duplicates in short time window


def send_scheduled_messages():
    global recently_sent

    try:
        now = datetime.now(pytz.timezone("Asia/Singapore")).time()
        logger.info(f"Checking for scheduled messages at {now.strftime('%H:%M')}")

        # Lock to prevent overlapping send attempts
        with sending_lock:
            messages = ScheduledMessage.objects.filter(sent=False)

            for msg in messages:
                # Skip if recently sent (avoid duplicates due to timing overlaps)
                if msg.id in recently_sent:
                    continue

                # Check time match
                if now.hour == msg.send_time.hour and now.minute == msg.send_time.minute:
                    try:
                        logger.info(f"Sending message ID {msg.id}: {msg.message[:50]}... to {msg.channels}")

                        send_telegram(msg)  # ✅ send message via telegram utility
                        msg.sent = True
                        msg.sent_at = timezone.now()
                        msg.save()

                        # Add to recently sent to prevent duplicates
                        recently_sent.add(msg.id)
                        logger.info(f"Message {msg.id} sent successfully at {msg.sent_at}")

                    except Exception as e:
                        logger.error(f"Failed to send message {msg.id}: {str(e)}")

            # Clear old entries (prevent unbounded growth)
            if len(recently_sent) > 500:
                recently_sent = set(list(recently_sent)[-100:])

    except Exception as e:
        logger.error(f"Error in send_scheduled_messages: {str(e)}")


def start():
    global scheduler_started

    if scheduler_started:
        logger.info("Scheduler already started, skipping duplicate start.")
        return  # ✅ Prevent duplicate scheduler start

    scheduler_started = True
    scheduler = BackgroundScheduler(timezone="Asia/Singapore")
    scheduler.add_job(send_scheduled_messages, 'interval', minutes=1)
    scheduler.start()

    logger.info("✅ Background scheduler started successfully (no duplicate start)")
