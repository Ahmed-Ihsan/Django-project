from django.shortcuts import render
from django.http import HttpResponse
from app_1 import models
from app_1 import forms
# Create your views here.

def for_user(request):
	all_user=models.User.objects.all()
	context={
		'data':all_user
	}
	return render(request,'app_1/page1.html',context)

def for_img(request):
		all_post=models.img.objects.all()
		context={
			'all_post':all_post
		}
		return render(request,'app_1/page2.html',context)

def id_user(request ,id):
		all_post=models.User.objects.filter(id=id)
		context={
			'all_post':all_post
		}
		return render(request,'app_1/page4.html',context)

def input_post(request):
	data=forms.input_post(request.POST or None)
	if data.is_valid():
		inf=models.img()
		inf.title=data.cleaned_data['title']
		inf.text=data.cleaned_data['text']
		inf.img=data.cleaned_data['img']
		inf.many=data.cleaned_data['many']
		inf.save()
	context={
		'formdata':data
	}
	return render(request,'app_1/page3.html',context)

def input_user(request):
	data=forms.input_user(request.POST or None)
	if data.is_valid():
		inf=models.User()
		inf.first_name=data.cleaned_data['first_name']
		inf.lest_name=data.cleaned_data['lest_name']
		inf.age=data.cleaned_data['age']
		inf.date_bith=data.cleaned_data['date_bith']
		inf.save()
	context={
		'formdata':data
	}
	return render(request,'app_1/page3.html',context)
