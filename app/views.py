from django.shortcuts import render
from .models import Question, Choice, Job

def quiz(request):
    questions = Question.objects.all()
    return render(request, 'quiz.html', {'questions': questions})


def result(request):
    if request.method == 'POST':
        selected_choices = request.POST.getlist('choices')

        skills = []
        for choice_id in selected_choices:
            choice = Choice.objects.get(id=choice_id)
            skills.append(choice.skill_tag)

        jobs = match_jobs(skills)

        return render(request, 'result.html', {'jobs': jobs})
def match_jobs(user_skills):
    from .models import Job

    jobs = Job.objects.all()
    scored_jobs = []

    for job in jobs:
        score = len(set(user_skills) & set(job.required_skills))
        scored_jobs.append((job, score))

    scored_jobs.sort(key=lambda x: x[1], reverse=True)

    return [job for job, score in scored_jobs if score > 0]