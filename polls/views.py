from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

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


def vote(request, q_id):
        # Ответы пользователя - хранит pk
        choices = request.POST.getlist("choice")
        question = Question.objects.get(pk=q_id)
        
        res = ""
        for c_pk in choices:
                choice = question.choice_set.get(pk=c_pk)
                choice.votes += 1
                choice.save()
                res += "<h1>%s</h1>" % question.choice_set.get(pk=c_pk).votes

        return HttpResponseRedirect( reverse("polls:results", args = (q_id, )) )

def results(request, q_id):
    question = Question.objects.get(pk=q_id)
    context = {
        "question": question,
    }

    return render(request, "polls/results.html", context)