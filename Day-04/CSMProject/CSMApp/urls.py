from django.urls import path
from . import views
from django.contrib.auth import views as ad

urlpatterns = [
	path('',views.home,name="hm"),
	path('rg/',views.register,name="rg"),
	path('lg/',ad.LoginView.as_view(template_name="html/login.html"),name="lg"),
	path('lgn/',ad.LogoutView.as_view(template_name="html/logout.html"),name="lgo"),
]