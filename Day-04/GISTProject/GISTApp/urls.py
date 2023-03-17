from django.urls import path
from . import views

urlpatterns=[
	path('',views.home,name="hm"),
	path('abt/',views.about,name="ab"),
	path('reg/',views.register,name="rg"),
	path('streg/',views.streg,name="stg"),
	path('stp/<int:w>/',views.stupd,name="stup"),
	path('stdy/<int:k>/',views.stdte,name="std"),
]
