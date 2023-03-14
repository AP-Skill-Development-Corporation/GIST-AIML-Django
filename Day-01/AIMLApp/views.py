from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def demo(k):
	return HttpResponse("Hi Welcome")

def sample(request,k):
	return HttpResponse("Hi Welcome {}".format(k))

def gy(request,q,w):
	return HttpResponse("<h2>Hi Welcome {} your age is: {}</h2>".format(w,q))

	
