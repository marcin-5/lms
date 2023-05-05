from django.shortcuts import render, redirect
from django.urls import reverse

from . import forms


def home(request):
    return render(request, 'home/home.html')


def contact(request):
    form = forms.ContactMessageForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('home:home'))

    return render(request, 'home/contact.html', {"form": form})
