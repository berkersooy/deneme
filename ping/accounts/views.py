from django.shortcuts import render, redirect


from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from .models import ip_address
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    #ip_addresss = request.user.userid.home_set.all()
    #user = authenticate(username=username, password=password)
    #user_form = User.objects.get(id=userid)
    ip_addresss = ip_address.objects.filter(userid=request.user)
    #ip_addresss = ip_address.objects.all()
    return render(request, "home.html", {"ip_addresss": ip_addresss})


def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "login.html", context)


def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "signup.html", context)


def logout_view(request):
    logout(request)
    return redirect('/')


# def ip_address(request):
#    def get_queryset(self):
#        queryset = ip_address.objects.filter(userid_id=request.user)
#    return render(request, "ip_address.html", {'ip_address': ip_address})

#    if User.id==userid_id:
#        ip_addresss = ip_address.objects.filter(ip_address)
#        return render(request, "ip_address.html", {'ipaddress': ip_address})
