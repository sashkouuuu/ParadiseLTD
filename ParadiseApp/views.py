from django.http import HttpResponse
from django.shortcuts import render, redirect

from ParadiseApp.forms import CreateRoll
from ParadiseApp.models import Roll


def rolls(request):
    rolls = Roll.objects.all()
    form = CreateRoll(request.POST)

    if request.method == 'POST' and form.is_valid():
        roll = Roll()
        roll.producer = form.cleaned_data["producer"]
        roll.size = form.cleaned_data["size"]
        roll.coating = form.cleaned_data["coating"]
        roll.hardness = form.cleaned_data["hardness"]
        roll.net = form.cleaned_data["net"]
        roll.gross = form.cleaned_data["gross"]

        roll.save()

    return render(request, "rolls.html", {"rolls":rolls, "form": form})

def index(request):
    return redirect("rolls")

def create_roll(request):
    return render(request, "index.html")



