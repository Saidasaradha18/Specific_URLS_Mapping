from django.urls import path
from App2.views import *

urlpatterns=[
    path('india/',india,name='india'),
    path('bharath/',bharath,name='bharath'),
]