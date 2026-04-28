from typing import List

def job_score(job_text: str) -> int:
    text = job_text.lower()
    score = 0

    if "system administrator" in text:
        score += 50
    if "infrastructure" in text:
        score += 40

    if "azure" in text:
        score += 40
    if "aws" in text:
        score += 40
    if "oracle cloud" in text or "oci" in text:
        score += 35

    if "l1" in text or "l2" in text or "l3" in text:
        score += 20

    if "senior" in text:
        score += 30

    if "saudi" in text or "riyadh" in text:
        score += 50

    if "remote" in text:
        score += 20

    if "visa" in text or "sponsorship" in text:
        score += 60

    return score
