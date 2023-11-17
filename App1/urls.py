from django.urls import path
from App1.views import *
app_name='Virat'
urlpatterns=[
    path('msd/',msd,name='msd'),
    path('raina/',raina,name='raina'),
]