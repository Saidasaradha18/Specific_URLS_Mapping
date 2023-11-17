from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def india(request):
    return render(request,'india.html')

def bharath(request):
    return HttpResponse('<h1>Cup Mukhyam Bigiluu')