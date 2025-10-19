import requests
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

TELEGRAM_TOKEN = "8409480894:AAGxhDz1siXDaoTgTFMzKA4T6oP8OsqyLXg"

GROUP_MAP = {
    # Forex
    "Forex_Updates": "-1002600232801",
    "Forex_FX": "-1002600232801",
    "Forex_Premium": "-1002600232801",
    "Forex_Disclaimers": "-1002600232801",
    "Forex_USDT": "-1002600232801",
    "Forex_Sponsorships": "-1002600232801",
    "Forex_Events": "-1002600232801",
    "Forex_JYP": "-1002600232801",
    "Forex_GBP": "-1002600232801",
    "Forex_CAD": "-1002600232801",
    "Forex_NZD": "-1002600232801",
    "Forex_AUD": "-1002600232801",
    "Forex_DXY": "-1002600232801",
    "Forex_EUR": "-1002600232801",
    "Forex_CHF": "-1002600232801",
    "Forex_Feedbacks": "-1002600232801",
    "Forex_Social_Media": "-1002600232801",
    "Forex_All": "-1002600232801",

    # Commodities
    "Commodities_Updates": "-1002589959992",
    "Commodities_Fx": "-1002589959992",
    "Commodities_Events": "-1002589959992",
    "Commodities_Feedbacks": "-1002589959992",
    "Commodities_Sponsorships": "-1002589959992",
    "Commodities_Social_Media": "-1002589959992",
    "Commodities_Disclaimers": "-1002589959992",
    "Commodities_Premium": "-1002589959992",
    "Commodities_XAG": "-1002589959992",
    "Commodities_DXY": "-1002589959992",
    "Commodities_Natural_Gas": "-1002589959992",
    "Commodities_XAU": "-1002589959992",
    "Commodities_USDT": "-1002589959992",
    "Commodities_OIL": "-1002589959992",
    "Commodities_All": "-1002589959992",

    # Crypto
    "Crypto_Updates": "-1002589776402",
    "Crypto_Fx": "-1002589776402",
    "Crypto_Events": "-1002589776402",
    "Crypto_Feedbacks": "-1002589776402",
    "Crypto_Sponsorships": "-1002589776402",
    "Crypto_BNB": "-1002589776402",
    "Crypto_Solana": "-1002589776402",
    "Crypto_BTC": "-1002589776402",
    "Crypto_Tron": "-1002589776402",
    "Crypto_ETH": "-1002589776402",
    "Crypto_Ripple": "-1002589776402",
    "Crypto_Polkadot": "-1002589776402",
    "Crypto_Litecoin": "-1002589776402",
    "Crypto_DXY": "-1002589776402",
    "Crypto_Stella": "-1002589776402",
    "Crypto_Shiba": "-1002589776402",
    "Crypto_Doge": "-1002589776402",
    "Crypto_Cardando": "-1002589776402",
    "Crypto_Link": "-1002589776402",
    "Crypto_Avalanche": "-1002589776402",
    "Crypto_Pancake": "-1002589776402",
    "Crypto_USDT": "-1002589776402",
    "Crypto_Social_Media": "-1002589776402",
    "Crypto_Disclaimers": "-1002589776402",
    "Crypto_Premium": "-1002589776402",
    "Crypto_All": "-1002589776402",

    # Stocks
    "Stocks_Updates": "-1002614326762",
    "Stocks_Fx": "-1002614326762",
    "Stocks_Events": "-1002614326762",
    "Stocks_Feedbacks": "-1002614326762",
    "Stocks_Sponsorships": "-1002614326762",
    "Stocks_Tesla": "-1002614326762",
    "Stocks_Disclaimers": "-1002614326762",
    "Stocks_Premium": "-1002614326762",
    "Stocks_USDT": "-1002614326762",
    "Stocks_Social_Media": "-1002614326762",
    "Stocks_DXY": "-1002614326762",
    "Stocks_All": "-1002614326762",

    # Indices
    "Indices_Updates": "-1002519061327",
    "Indices_Fx": "-1002519061327",
    "Indices_Events": "-1002519061327",
    "Indices_Feedbacks": "-1002519061327",
    "Indices_Sponsorships": "-1002519061327",
    "Indices_FTSE": "-1002519061327",
    "Indices_IBEX": "-1002519061327",
    "Indices_CAC40": "-1002519061327",
    "Indices_AEX": "-1002519061327",
    "Indices_Eurostoxx50": "-1002519061327",
    "Indices_DAX": "-1002519061327",
    "Indices_A50": "-1002519061327",
    "Indices_Hangseng": "-1002519061327",
    "Indices_DOW": "-1002519061327",
    "Indices_Swiss20": "-1002519061327",
    "Indices_Nikkei": "-1002519061327",
    "Indices_Disclaimers": "-1002519061327",
    "Indices_Premium": "-1002519061327",
    "Indices_USDT": "-1002519061327",
    "Indices_Social_Media": "-1002519061327",
    "Indices_All": "-1002519061327",
}

TOPIC_MAP = {
    # Forex
    "Forex_Updates": 7, "Forex_FX": 6, "Forex_Feedbacks": 727, "Forex_Premium": 8, "Forex_Disclaimers": 10,
    "Forex_USDT": 20, "Forex_Sponsorships": 13, "Forex_Events": 11, "Forex_JYP": 5, "Forex_GBP": 4, "Forex_CAD": 85,
    "Forex_NZD": 86, "Forex_AUD": 84, "Forex_DXY": 2, "Forex_EUR": 3, "Forex_CHF": 83,

    # Commodities
    "Commodities_Updates": 15, "Commodities_Fx": 26, "Commodities_Events": 21, "Commodities_Feedbacks": 324,
    "Commodities_Sponsorships": 22, "Commodities_Social_Media": 17, "Commodities_Disclaimers": 20,
    "Commodities_Premium": 18, "Commodities_XAG": 6, "Commodities_DXY": 27, "Commodities_Natural_Gas": 10,
    "Commodities_XAU": 5, "Commodities_USDT": 25, "Commodities_OIL": 8,

    # Crypto
    "Crypto_Updates": 19, "Crypto_Fx": 27, "Crypto_Events": 13, "Crypto_Feedbacks": 704, "Crypto_Sponsorships": 2,
    "Crypto_BNB": 49, "Crypto_Solana": 11, "Crypto_BTC": 5, "Crypto_Tron": 48, "Crypto_ETH": 10,
    "Crypto_Ripple": 60, "Crypto_Polkadot": 56, "Crypto_Litecoin": 55, "Crypto_DXY": 18, "Crypto_Stella": 63,
    "Crypto_Shiba": 8, "Crypto_Doge": 6, "Crypto_Cardando": 59, "Crypto_Link": 57, "Crypto_Avalanche": 53,
    "Crypto_Pancake": 52, "Crypto_USDT": 12, "Crypto_Social_Media": 16, "Crypto_Disclaimers": 14, "Crypto_Premium": 15,

    # Stocks
    "Stocks_Updates": 28, "Stocks_Fx": 8, "Stocks_Events": 4, "Stocks_Feedbacks": 102, "Stocks_Sponsorships": 5,
    "Stocks_Tesla": 55, "Stocks_Disclaimers": 3, "Stocks_Premium": 6, "Stocks_USDT": 7, "Stocks_Social_Media": 2,
    "Stocks_DXY": 29,

    # Indices
    "Indices_Updates": 7, "Indices_Fx": 12, "Indices_Events": 3, "Indices_Feedbacks": 497, "Indices_Sponsorships": 4,
    "Indices_FTSE": 94, "Indices_IBEX": 100, "Indices_CAC40": 99, "Indices_AEX": 98, "Indices_Eurostoxx50": 97,
    "Indices_DAX": 95, "Indices_A50": 93, "Indices_Hangseng": 86, "Indices_DOW": 88, "Indices_Swiss20": 101,
    "Indices_Nikkei": 96, "Indices_Disclaimers": 2, "Indices_Premium": 5, "Indices_USDT": 9, "Indices_Social_Media": 8,
}


# ✅ Expand "All" categories dynamically
def expand_channels(channels):
    expanded = set()
    for ch in channels:
        if ch.endswith("_All"):
            prefix = ch.split("_All")[0]
            for topic in TOPIC_MAP.keys():
                if topic.startswith(prefix + "_"):
                    expanded.add(topic)
        else:
            expanded.add(ch)
    return list(expanded)


def send_telegram(msg_obj):
    all_channels = expand_channels(msg_obj.channels)
    sent_flags = set()  # Use (chat_id, topic_id) flags to prevent duplicates

    for channel in all_channels:
        chat_id = GROUP_MAP.get(channel)
        topic_id = TOPIC_MAP.get(channel)

        if not chat_id:
            logger.warning(f"❌ Group not found for {channel}")
            continue

        flag = (chat_id, topic_id)
        if flag in sent_flags:
            continue  # Prevent duplicate message
        sent_flags.add(flag)

        payload = {"chat_id": chat_id, "parse_mode": "HTML"}
        if topic_id:
            payload["message_thread_id"] = topic_id

        try:
            if msg_obj.image:
                payload["caption"] = msg_obj.message
                with msg_obj.image.open("rb") as img:
                    response = requests.post(
                        f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto",
                        data=payload,
                        files={"photo": img},
                        timeout=300,
                    )
            else:
                payload["text"] = msg_obj.message
                response = requests.post(
                    f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
                    data=payload,
                    timeout=300,
                )

            if response.status_code == 200:
                logger.info(f"✅ Sent successfully to {channel}")
            else:
                logger.error(f"⚠️ Failed to send to {channel}: {response.status_code} - {response.text}")

        except requests.exceptions.RequestException as e:
            logger.error(f"🌐 Network error sending to {channel}: {str(e)}")
        except Exception as e:
            logger.error(f"💥 Unexpected error sending to {channel}: {str(e)}")
