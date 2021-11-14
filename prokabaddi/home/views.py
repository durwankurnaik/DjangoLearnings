from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'home/index.html')


def players(request):
    return render(request, 'home/players.html')


def teams(request):
    return render(request, 'home/teams.html')


def register(request):
    return render(request, 'home/register.html')


def about(request):
    return render(request, 'home/about.html')
