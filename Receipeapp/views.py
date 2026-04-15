from django.shortcuts import render, redirect
from .models import Receipe
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django import forms


class usersForm(forms.Form):
    num1 = forms.CharField(label="Value 1", required=False)


# Create your views here.

@login_required(login_url='/login_page')
def add_receipe(request):
    if request.method == "POST":
        receipe_name = request.POST['receipe_name']
        receipe_desc = request.POST['receipe_desc']
        receipe_image = request.FILES['receipe_image']

        receipe = Receipe(
            receipe_name=receipe_name, 
            receipe_desc=receipe_desc, 
            receipe_image=receipe_image
        )
        receipe.save()

        return redirect('/view_receipe')

    queryset = Receipe.objects.all()
    context = {'receipes':queryset}

    return render(request, template_name='receipe.html', context=context)


@login_required(login_url='/login_page')
def view_receipe(request):
    receipes = Receipe.objects.all()
    search = request.GET.get('search')

    if search:
        receipes = receipes.filter(receipe_name__icontains=search)

    return render(request, template_name='view_receipes.html', context={'receipes': receipes})


def update_receipe(request, id):
    queryset = Receipe.objects.get(id=id)

    if request.method == "POST":
        receipe_name = request.POST.get('receipe_name')
        receipe_desc = request.POST.get('receipe_desc')
        receipe_image = request.FILES.get('receipe_image')

        queryset.receipe_name = receipe_name
        queryset.receipe_desc = receipe_desc

        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()

        return redirect('/view_receipe')

    return render(request, template_name='update_receipe.html', context={'receipe':queryset} )


def delete_receipe(request, id):
    query = Receipe.objects.get(pk=id)
    query.delete()
    print(id)
    return redirect('/view_receipe', {'query':query})


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username):
            messages.error(request, message="Invalid Username..!")
            return redirect('/login_page')

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, message="Invalid Password..!")
            return redirect('/login_page')

        else:
            login(request, user)
            return redirect('/view_receipe')

    return render(request, template_name='login.html')


def logout_page(reqeust):
    logout(reqeust)
    return redirect('/login_page')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.warning(request, message="Username Already Taken..!")
            return redirect('/register')

        user = User.objects.create(first_name=first_name, last_name=last_name, username=username)

        user.set_password(password)
        user.save()

        return redirect('/login_page')

    return render(request, template_name='register.html')