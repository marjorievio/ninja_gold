from django.urls import path
from . import views

app_name = 'ninja_gold'
urlpatterns = [
    path('', views.index, name='index'),
    path('reset', views.reset, name='reset'),
    path('process_money', views.process_money, name='process')
]
