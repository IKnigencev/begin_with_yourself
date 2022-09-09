from django.urls import path

from . import views


app_name = 'news'

urlpatterns = [
    path('all/', views.news, name='news')
]
