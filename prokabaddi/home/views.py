from django.shortcuts import render
from .models import *
from django.utils import timezone

players = Player.objects.all()
points_table = PointsTable.objects.all()
registers = Register.objects.all()
team_info = TeamInfo.objects.all()
top_raiders = TopRaider.objects.all()
top_defenders = TopDefender.objects.all()

params = {
    'points_table': points_table,
    'players': players,
    'registers': registers,
    'team_info': team_info,
    'top_raiders': top_raiders,
    'top_defenders': top_defenders,
}


def index(request):
    return render(request, 'home/index.html', params)


def players(request):
    return render(request, 'home/players.html', params)


def teams(request):
    return render(request, 'home/teams.html', params)


def register(request):
    create = request.POST.get('create', 'off')
    update = request.POST.get('update', 'off')
    delete = request.POST.get('delete', 'off')

    if create == 'on':
        createRegister(request)

    # if update == 'on':
    #     updateRegister(request)
    #
    # if delete == 'on':
    #     deleteRegister(request)

    return render(request, 'home/register.html', params)


def createRegister(request):
    username = request.POST.get('username')
    name = request.POST.get('name')
    place = request.POST.get('place')
    age = request.POST.get('age')

    Register.objects.create(
        user=username,
        name=name,
        city=place,
        age=age
    )

    return render(request, 'home/operation_success.html', params)


# def updateRegister(request):
#     username = request.POST.get('username')
#     name = request.POST.get('name')
#     place = request.POST.get('place')
#     age = request.POST.get('age')
#
#     Register.objects.create(
#         user=username,
#         name=name,
#         city=place,
#         age=age
#     )
#
#
# def deleteRegister(request):
#     name = request.POST.get('name')
#     Register.objects.filter(name='something').delete()
#
#     return render(request, 'home/operation_success.html', params)

