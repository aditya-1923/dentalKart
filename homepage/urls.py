from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),

]

