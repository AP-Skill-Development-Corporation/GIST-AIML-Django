from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def demo(k):
	return HttpResponse("Hi Welcome")

def sample(request,k):
	return HttpResponse("Hi Welcome {}".format(k))

def gy(request,q,w):
	return HttpResponse("<h2>Hi Welcome {} your age is: {}</h2>".format(w,q))

def jk(request,r,b):
	return HttpResponse("<h2>Hi Welcome <span style='color:blue'>{}</span> your age is: <span style='color:green'>{}</span></h2>".format(r,b))

def std(request,nm,yr,bh):
	return HttpResponse("<html><head><title>Student Record</title><style>#n{color:red}#y{color:green}#b{color:blue}</style></head><body><h2>Student Name is: <span id='n'>%s</span></h2><h3>Year is: <span id='y'>%d</span></h3><h3>Branch is: <span id='b'>%s</span></h3></body></html>"%(nm,yr,bh))

def ak(request,p):
	return HttpResponse("<script>alert('Welcome User {}')</script>".format(p))

def k(request):
	return render(request,'demo.html')

def zw(request):
	return render(request,'ht/test.html')
