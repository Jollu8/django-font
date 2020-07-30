from django.shortcuts import render
from django.http import HttpResponse
from news.models import News


def index(request):
    news = News.objects.all()
    context = {'news': news, 'title': 'список новостей'}
    return render(request, 'news/index.html', context)
