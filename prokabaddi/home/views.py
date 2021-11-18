from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index(request):
    context = {
        'points_table': PointsTable.objects.all(),
        'top_raiders': TopRaider.objects.all(),
        'top_defenders': TopDefender.objects.all(),
    }
    return render(request, 'home/index.html', context)


def players(request):
    player_info = Player.objects.all()
    return render(request, 'home/players.html', {'player_info': player_info})


def teams(request):
    team_info = TeamInfo.objects.all()
    return render(request, 'home/teams.html', {'team_info': team_info})


def registry(request):
    entry = Register.objects.all()
    return render(request, 'home/registry.html', {'entry': entry})


def entries(request, pk):
    count = Register.objects.all().count()
    context = {
        'entry': Register.objects.get(id=pk),
        'all_data': Register.objects.all(),
        'count': count,
    }
    return render(request, 'home/entries.html', context)


def createEntry(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/registry')

    return render(request, 'home/create_entry.html', {'form': form})


def updateEntry(request, pk):
    entry = Register.objects.get(id=pk)
    form = RegisterForm(instance=entry)

    if request.method == 'POST':
        form = RegisterForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('/registry')

    return render(request, 'home/create_entry.html', {'form': form})


def deleteEntry(request, pk):
    Register.objects.filter(id=pk).delete()
    return redirect('/registry')
