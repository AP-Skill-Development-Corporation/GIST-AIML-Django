from django.shortcuts import render

# Create your views here.
def home(self):
	return render(self,'html/home.html')

def about(self):
	return render(self,'html/about.html')

def register(self):
	return render(self,'html/register.html')