# from django.shortcuts import render, redirect, HttpResponse
# from django.views.generic import View, TemplateView
from django.http import HttpResponse
from django.template import loader


# def choose_sentiment_or_emotion(request):
#     return render(request, 'home/home.html')
def choose_sentiment_or_emotion(request):
    template = loader.get_template('home/home.html')
    return HttpResponse(template.render())