from django.http import HttpResponse
from django.shortcuts import render

def about(request):
	return HttpResponse('Hello')

def home(request):
	return render(request,'home.html',{'greeting':'ti gay'})