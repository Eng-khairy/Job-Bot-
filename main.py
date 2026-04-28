import requests
import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_GROUP_ID")

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=data)


# ================= FETCH JOBS =================

def fetch_remotive():
    url = "https://remotive.com/api/remote-jobs"
    jobs = []
    try:
        res = requests.get(url).json()
        for job in res.get("jobs", [])[:20]:
            jobs.append({
                "title": job["title"],
                "company": job["company_name"],
                "location": "Remote",
                "url": job["url"]
            })
    except:
        pass
    return jobs


def fetch_adzuna():
    url = "https://api.adzuna.com/v1/api/jobs/sa/search/1?app_id=demo&app_key=demo&results_per_page=20"
    jobs = []
    try:
        res = requests.get(url).json()
        for job in res.get("results", []):
            jobs.append({
                "title": job["title"],
                "company": job["company"]["display_name"],
                "location": job["location"]["display_name"],
                "url": job["redirect_url"]
            })
    except:
        pass
    return jobs


def fetch_jobs():
    return fetch_remotive() + fetch_adzuna()


# ================= FILTER =================

def is_relevant(job):
    text = f"{job['title']} {job['location']}".lower()

    keywords = [
        "system administrator",
        "cloud",
        "aws",
        "azure",
        "oracle",
        "infrastructure",
        "it support"
    ]

    if not any(k in text for k in keywords):
        return False

    # Saudi / Egypt / Remote
    if any(x in text for x in ["saudi", "riyadh", "jeddah", "egypt", "cairo", "remote"]):
        return True

    return False


# ================= MAIN =================

def main():
    jobs = fetch_jobs()

    jobs = [job for job in jobs if is_relevant(job)]

    if not jobs:
        send_message("❌ No relevant jobs found today")
        return

    msg = "🔥 Latest Jobs (Saudi 🇸🇦 | Egypt 🇪🇬 | Remote 🌍):\n\n"

    for job in jobs[:5]:
        msg += f"• {job['title']}\n🏢 {job['company']}\n📍 {job['location']}\n🔗 {job['url']}\n\n"

    send_message(msg)


if __name__ == "__main__":
    main()
