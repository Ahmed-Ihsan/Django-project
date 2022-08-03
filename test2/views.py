from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login , logout 
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from .models import item ,sales ,User
from .forms import salesForm , itemForm


def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        except:
            messages.error(request,"User not found")
    context = {}
    return render(request,"test2/login_user.html",context)

def sinup_user(request):
    form = UserCreationForm()
    context = {'form':form}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            user = form.save(commit=False)
            user.username = user.username
            user.save()
        return redirect('user_login')
    return render(request,"test2/sinup_user.html",context)

@login_required(login_url='/user_login')
def log_out(request):
    logout(request)
    return redirect('user_login')

@login_required(login_url='/user_login')    
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    resl1 = item.objects.filter(Q(name__icontains= q))
    resl2 = sales.objects.filter(Q(item__name__icontains= q))
    conter = [resl1.count() ,resl2.count()]

    totel1= [i.number*i.cost for i  in resl1]
    totel2 = [i.number*i.cost for i  in resl2]

    resl1 = zip(resl1,totel1)
    resl2 = zip(resl2,totel2)
    context ={'item':resl1 ,'sales':resl2 ,"conter_iteam":conter[0],"conter_sales":conter[1]}
    return render(request,"test2/home.html",context)

@login_required(login_url='/user_login')
def input_sales(request):
    form = salesForm()
    context = {'form':form}
    if request.method == 'POST':
        form = salesForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('home')
    return render(request,"test2/input.html",context)

@login_required(login_url='/user_login')
def input_item(request):
    form = itemForm()
    context = {'form':form}
    if request.method == 'POST':
        form = itemForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('home')
    return render(request,"test2/input.html",context)

@login_required(login_url='/user_login')
def update_item(request,NP):
    resl = item.objects.get(id=NP)
    form = itemForm(instance=resl)
    context = {'form':form}
    if request.method == 'POST':
        form = itemForm(request.POST,instance=resl)
        if form.is_valid:
            form.save()
        return redirect('home')
    return render(request,"test2/input.html",context)

@login_required(login_url='/user_login')
def update_sales(request,NP):
    resl = sales.objects.get(id=NP)
    form = salesForm(instance=resl)
    context = {'form':form}
    if request.method == 'POST':
        form = salesForm(request.POST,instance=resl)
        if form.is_valid:
            form.save()
        return redirect('home')
    return render(request,"test2/input.html",context)

@login_required(login_url='/user_login')
def delete_item(request,NP):
    resl = item.objects.get(id=NP)
    context = {'obj':resl}
    if request.method == 'POST':
        resl.delete()
        return redirect('home')
    return render(request,"test2/delete.html",context)

@login_required(login_url='/user_login')
def delete_sales(request,NP):
    resl = sales.objects.get(id=NP)
    context = {'obj':resl}
    if request.method == 'POST':
        resl.delete()
        return redirect('home')
    return render(request,"test2/delete.html",context)