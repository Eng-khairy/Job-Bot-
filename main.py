import requests
import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_GROUP_ID")

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=data)

def fetch_jobs():
    # Demo jobs (replace later with APIs)
    return [
        "Senior System Administrator - Riyadh (AWS, Azure) VISA",
        "Cloud Engineer AWS - Saudi Arabia",
        "IT Support L2 - Cairo",
        "Frontend Developer (ignore)",
    ]

def filter_jobs(jobs):
    keywords = ["system administrator", "cloud", "aws", "azure", "infrastructure"]
    result = []
    for job in jobs:
        text = job.lower()
        if any(k in text for k in keywords):
            result.append(job)
    return result

def main():
    jobs = fetch_jobs()
    jobs = filter_jobs(jobs)

    if not jobs:
        send_message("No jobs found today 😢")
        return

    msg = "🔥 Latest Jobs:\n\n"
    for job in jobs[:5]:
        msg += f"• {job}\n"

    send_message(msg)

if __name__ == "__main__":
    main()
