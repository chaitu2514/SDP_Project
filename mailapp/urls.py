from .import views
from django.urls import path
urlpattern =[
    path('', views.send_emails,name='send_emails'),
]