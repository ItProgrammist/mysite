from django.shortcuts import render
from django.http import HttpResponse

from .models import Question, Choice

# Create your views here
def index(request):
    questions = Question.objects.all()
    
    context = {
        "questions": questions
    }

    return render(request, "polls/index.html", context)

def meme(request):
    return HttpResponse('<img src="http://img.1001mem.ru/posts_temp/17-12-02/3922587.jpg">')
# Страница /polls/q_id
def detail(request, q_id):
        #Берём ОДИН вопрос по PK, используя get()
        question = Question.objects.get(pk=q_id)
        context = {
                "question": question,
        }
        return render(request, "polls/detail.html", context)


def results(request, q_id):
        res = 'Result for question number %s. ' % q_id
        return HttpResponse(res)

def vote(request, q_id):
        res = 'Vote for question number %s. ' % q_id
        return HttpResponse(res)