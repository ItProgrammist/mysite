from django.shortcuts import render
from django.http import HttpResponse

# Create your views here
def index(request):
    return HttpResponse('<h1 align="center">Hello World</h1>')
def meme(request):
    return HttpResponse('<img src="http://img.1001mem.ru/posts_temp/17-12-02/3922587.jpg">')
