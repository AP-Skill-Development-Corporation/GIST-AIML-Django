from django.shortcuts import render,redirect
from .models import Student

# Create your views here.
def home(self):
	return render(self,'html/home.html')

def about(self):
	return render(self,'html/about.html')

def register(self):
	return render(self,'html/register.html')

def streg(request):
	h = Student.objects.all()
	if request.method == "POST":
		a = request.POST['sn']
		b = request.POST['sa']
		c = request.POST['se']
		z = Student(snme=a,sage=b,semail=c)
		z.save()
		return redirect('/streg')
	return render(request,'html/streg.html',{'v':h})

def stupd(request,w):
	a = Student.objects.get(id=w)
	if request.method == "POST":
		a.snme = request.POST['sn']
		a.sage = request.POST['sa']
		a.semail = request.POST['se']
		a.save()
		return redirect('/streg') 
	return render(request,'html/stpd.html',{'p':a})

def stdte(request,k):
	m = Student.objects.get(id=k)
	if request.method=="POST":
		m.delete()
		return redirect('/streg')	
	return render(request,'html/std.html',{'z':m})




