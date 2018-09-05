from django.urls import path

from . import views

urlpatterns = [
    # ex: /kfc/
    path('', views.index, name='index'),
    # ex: /kfc/home/
    path('home/', views.home, name='home'),
    # ex: /kfc/logout/
    path('logout/', views.index, name='logout'),
]
