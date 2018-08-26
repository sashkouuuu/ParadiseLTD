from django.shortcuts import render, redirect

from ParadiseApp.forms import CreateRoll
from ParadiseApp.models import Roll, Plan


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
    return redirect("overview")

def delete_roll(request, roll_id):
    Roll.objects.filter(id=roll_id).delete()
    return redirect("rolls")

def overview(request):
    return render(request, "overview.html")

def plans(request):
    plans = Plan.objects.all()
    return render(request, "plan.html", {"plans": plans})

def plan(request, plan_id):
    plan = Plan.objects.filter(id=plan_id).first()
    return render(request, "plan.html", {"plan": plan})




