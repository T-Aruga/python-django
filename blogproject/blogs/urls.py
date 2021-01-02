from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    path('top/', views.index, name='index'),
]
