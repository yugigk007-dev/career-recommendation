from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=255)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    skill_tag = models.CharField(max_length=100)  # IMPORTANT

class Job(models.Model):
    title = models.CharField(max_length=100)
    required_skills = models.JSONField()  # ["python", "math", "design"]
def match_jobs(user_skills):
    jobs = Job.objects.all()
    scored_jobs = []

    for job in jobs:
        score = len(set(user_skills) & set(job.required_skills))
        scored_jobs.append((job, score))

    scored_jobs.sort(key=lambda x: x[1], reverse=True)
    return [job for job, score in scored_jobs if score > 0]