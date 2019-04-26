from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('login', views.login, name='login'),
        path('logout', views.logout, name='logout'),
        path('rcode', views.rcode, name='rcode'),
        path('add', views.add, name='add')
        ]
