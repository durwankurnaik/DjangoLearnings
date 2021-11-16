from django.shortcuts import render
from .models import *

players = Player.objects.all()
points_table = PointsTable.objects.all()
registers = Register.objects.all()
team_info = TeamInfo.objects.all()
top_raiders = TopRaider.objects.all()
top_defenders = TopDefender.objects.all()

params = {
        'points_table': points_table,
        'players': players,
        'registers': points_table,
        'team_info': team_info,
        'top_raiders': top_raiders,
        'top_defenders': top_defenders
    }


def index(request):
    return render(request, 'home/index.html', params)


def players(request):
    return render(request, 'home/players.html', params)


def teams(request):
    return render(request, 'home/teams.html', params)


def register(request):
    return render(request, 'home/register.html', params)
