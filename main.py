import requests
import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_GROUP_ID")

def send_message(text):
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": CHAT_ID, "text": text})
    except Exception as e:
        print("Telegram Error:", e)


def fetch_remotive():
    jobs = []
    try:
        res = requests.get("https://remotive.com/api/remote-jobs", timeout=10).json()
        for job in res.get("jobs", [])[:10]:
            jobs.append({
                "title": job.get("title", ""),
                "company": job.get("company_name", ""),
                "location": "Remote",
                "url": job.get("url", "")
            })
    except Exception as e:
        print("Remotive Error:", e)

    return jobs


def fetch_jobs():
    return fetch_remotive()


def is_relevant(job):
    text = f"{job['title']} {job['location']}".lower()

    keywords = [
        "system administrator",
        "cloud",
        "aws",
        "azure",
        "infrastructure",
        "it support"
    ]

    if not any(k in text for k in keywords):
        return False

    if any(x in text for x in ["saudi", "egypt", "remote"]):
        return True

    return False


def main():
    try:
        jobs = fetch_jobs()
        jobs = [j for j in jobs if is_relevant(j)]

        if not jobs:
            send_message("❌ No jobs found")
            return

        msg = "🔥 Jobs:\n\n"

        for job in jobs[:5]:
            msg += f"• {job['title']}\n🏢 {job['company']}\n🔗 {job['url']}\n\n"

        send_message(msg)

    except Exception as e:
        send_message(f"❌ Error: {str(e)}")


if __name__ == "__main__":
    main()
