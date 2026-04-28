from models import Job, _flatten_tags, _is_in_saudi, _is_remote

def job_score(job: Job) -> int:
    text = f"{job.title} {job.location} {_flatten_tags(job.tags)}".lower()
    score = 0

    # Core
    if "system administrator" in text:
        score += 50
    if "infrastructure" in text:
        score += 40

    # Cloud
    if "azure" in text:
        score += 40
    if "aws" in text:
        score += 40
    if "oracle cloud" in text or "oci" in text:
        score += 35

    # Support
    if "l1" in text or "l2" in text or "l3" in text:
        score += 20

    # Senior
    if "senior" in text:
        score += 30

    # Saudi
    if _is_in_saudi(job.location):
        score += 50

    # Remote
    if _is_remote(job):
        score += 20

    # Visa
    if any(k in text for k in ["visa", "sponsorship", "relocation"]):
        score += 60

    return score
