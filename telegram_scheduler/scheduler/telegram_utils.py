import requests
from django.conf import settings

TELEGRAM_TOKEN = "7727934479:AAFRPDbB9tYS4tNoHF_mdMWoTbVKXbsOjzw"
CHANNEL_MAP = {
    "USD": "@usd_testing",
    "EUR": "@eur_testing"
}

def send_telegram(msg_obj):
    for channel in msg_obj.channels:
        chat_id = CHANNEL_MAP.get(channel)
        if not chat_id:
            continue
        data = {
            "chat_id": chat_id,
            "caption": msg_obj.message,
            "parse_mode": "HTML"
        }
        if msg_obj.image:
            with msg_obj.image.open('rb') as img:
                requests.post(
                    f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto",
                    data=data,
                    files={"photo": img}
                )
        else:
            data["text"] = msg_obj.message
            requests.post(
                f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
                data=data
            )
