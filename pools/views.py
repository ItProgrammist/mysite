from django.shortcuts import render
from django.http import HttpResponse

# Create your views here
def index(request):
    return HttpResponse('<h1 align="center">Hello World</h1>')
def meme(meme):
    return HttpResponse('<img src="https://millionstatusov.ru/pic/statpic/all8/5e04c21a52a39.jpg">')
