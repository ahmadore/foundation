from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    return render(request, 'foundation/index.html', {'title': 'Home'})


def about(request):
    return render(request, 'foundation/about.html', {'title': 'About'})

def contact(request):
    return render(request, 'foundation/contact.html', {'title': 'Contact Us'})

def constitution(request):
    return render(request, 'foundation/constitution.html', {'title': 'Constitution'})

def how_to_apply(request):
    return render(request, 'foundation/apply.html', {'title':'Apply'})