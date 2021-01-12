from django.http import HttpResponse
from django.shortcuts import render

def about(request):
	return HttpResponse('Hello')

def home(request):
	return render(request,'home.html',{'greeting':'ti gay'})

def reverse(request):
	get_text = request.GET['usertext']
	reversed_text = get_text [::-1]

	return render(request,'reverse.html',{'usertext': get_text, 'reversedtext': reversed_text})
