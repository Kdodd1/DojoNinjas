from django.shortcuts import render, HttpResponse, redirect

def index(request):

	return render(request, 'myapps/index.html')