from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='HomePage'),
    path('players', views.players, name='PlayersInfo'),
    path('teams', views.teams, name='TeamInfo'),
    path('register', views.register, name='Register'),
    path('registered', views.createRegister, name='Registered'),
    # path('deleted', views.deleteRegister, name='Registered'),
    # path('registered', views.createRegister, name='Registered'),
]
