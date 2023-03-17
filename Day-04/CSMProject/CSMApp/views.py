from django.shortcuts import render,redirect
from .forms import Streg
# Create your views here.
def home(request):
	return render(request,'html/home.html')

def register(request):
	d = Streg()
	if request.method == "POST":
		d = Streg(request.POST)
		if d.is_valid():
			d.save()
			return redirect('/lg')
	return render(request,'html/reg.html',{'f':d})