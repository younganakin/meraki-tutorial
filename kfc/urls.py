from django.urls import path

from . import views

urlpatterns = [
    # ex: /kfc/
    path('', views.index, name='index'),
    # ex: /kfc/api/login/
    path('api/login/',
         views.login_api,
         name='login_api'),
    # ex: /kfc/home/
    path('home/', views.home, name='home'),
]
