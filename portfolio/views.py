
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import *
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse

from portfolio.models import *
from .forms import *

import requests
from bs4 import BeautifulSoup

# Create your views here.

#  hello/views.py
def home_page_view(request):
    return render(request, 'portfolio/home.html')

def aboutme_page_view(request):
    context = {
        'formacoes': Formacao.objects.order_by('data_inicio'),
        'participacoes': Participacao.objects.order_by('data_inicio'),
        'interesses': Interesse.objects.all()
    }

    return render(request, 'portfolio/aboutme.html', context)

def projects_page_view(request):
    return render(request, 'portfolio/projects.html')

def contacts_page_view(request):
    return render(request, 'portfolio/contacts.html')

def scripts_page_view(request):
    url = "https://api.weatherapi.com/v1/current.json?key=c36ba19e1cad4b18a0a182405231406&q=Lisbon"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temperature = data["current"]["temp_c"]
    else:
        temperature = "N/A"

    context = {
        'temperature': temperature,
    }

    return render(request, 'portfolio/scripts.html', context)

def login_page_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,
                            username=username,
                            password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('portfolio:home'))
        else:
            return render(request, "portfolio/login.html", {
                'message': "Invalid credentials."
            })

    return render(request, 'portfolio/login.html')

def logout_page_view(request):
    logout(request)

    return render(request, 'portfolio/home.html')



@login_required
def new_formacao_page_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))

    form = FormacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:aboutme'))

    context = {'form': form}

    return render(request, 'portfolio/new_formacao.html', context)

@login_required
def edit_formacao_page_view(request, formacao_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))

    formacao = Formacao.objects.get(pk=formacao_id)
    form = FormacaoForm(request.POST or None, instance = formacao)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:aboutme'))

    context = {'form': form, 'formacao_id': formacao_id}

    return render(request, 'portfolio/edit_formacao.html', context)

@login_required
def remove_formacao_page_view(request, formacao_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))

    Formacao.objects.get(pk=formacao_id).delete()
    return HttpResponseRedirect(reverse('portfolio:aboutme'))

@login_required
def new_participacao_page_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))

    form = ParticipacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:aboutme'))

    context = {'form': form}

    return render(request, 'portfolio/new_participacao.html', context)

@login_required
def edit_participacao_page_view(request, participacao_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))

    participacao = Participacao.objects.get(pk=participacao_id)
    form = ParticipacaoForm(request.POST or None, instance = participacao)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:aboutme'))

    context = {'form': form, 'participacao_id': participacao_id}

    return render(request, 'portfolio/edit_participacao.html', context)

@login_required
def remove_participacao_page_view(request, participacao_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))

    Participacao.objects.get(pk=participacao_id).delete()
    return HttpResponseRedirect(reverse('portfolio:aboutme'))

@login_required
def new_interesse_page_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))

    form = InteresseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:aboutme'))

    context = {'form': form}

    return render(request, 'portfolio/new_interesse.html', context)

@login_required
def edit_interesse_page_view(request, interesse_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))

    interesse = Interesse.objects.get(pk=interesse_id)
    form = InteresseForm(request.POST or None, instance = interesse)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:aboutme'))

    context = {'form': form, 'interesse_id': interesse_id}

    return render(request, 'portfolio/edit_interesse.html', context)

@login_required
def remove_interesse_page_view(request, interesse_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))

    Interesse.objects.get(pk=interesse_id).delete()
    return HttpResponseRedirect(reverse('portfolio:aboutme'))