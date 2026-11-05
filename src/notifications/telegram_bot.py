import os
import requests
from dotenv import load_dotenv

load_dotenv()

def send_notification(message):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    response = requests.post(
        url,
        data={
            "chat_id": chat_id,
            "text": message
        },
        timeout=15
    )

    response.raise_for_status()
    print("Notification sent successfully!")


if __name__ == "__main__":
    send_notification(
        "🔔 TEST ALERT\n\nYour Sathyabama notification system is connected!"
    )