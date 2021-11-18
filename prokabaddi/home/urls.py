from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('players', views.players, name='players'),
    path('teams', views.teams, name='teaminfo'),
    path('registry', views.registry, name='registry'),
    path('create_entry/', views.createEntry, name='create_entry'),
    path('update_entry/<str:pk>', views.updateEntry, name='update_entry'),
    path('delete_entry/<str:pk>', views.deleteEntry, name='delete_entry'),
    path('entries/<str:pk>', views.entries, name='entries'),
]
