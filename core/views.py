from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import  login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.


def login_user(request):
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')


def submit_login(request):
    if request.POST:
        usuario = request.POST.get('username')
        password = request.POST.get('password')
        usuario =authenticate(username = usuario , password=password)
        if usuario is not None and usuario.is_active:
            login(request,usuario)
            return redirect ('/')
        else:
            messages.error(request, '   usuario ou senha invalido')
    return redirect('/')


def index(request):
    return redirect('/agenda')

@login_required(login_url='/login/')
def lista_eventos(request):
    evento = Evento.objects.all()
    dados={'eventos':evento}
    return render(request,'agenda.html',dados)