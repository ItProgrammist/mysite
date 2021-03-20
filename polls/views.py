from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "questions"

    def get_queryset(self):
        return Question.objects.all()

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

def meme(request):
    return HttpResponse('<img src="http://img.1001mem.ru/posts_temp/17-12-02/3922587.jpg">')


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


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def results(request, q_id):
    question = Question.objects.get(pk=q_id)
    context = {
        "question": question,
    }

    return render(request, "polls/results.html", context)