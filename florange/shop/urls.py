from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Sho pHome'),
    path('about', views.about, name='AboutUs'),
    path('contact', views.contact, name='ContactUs'),
    path('search', views.search, name='Search'),
    path('productview', views.productview, name='Search'),
    path('tracker', views.tracker, name='Tracker')
]
