import datetime
from django.shortcuts import render, redirect

from ParadiseApp.forms import CreateRoll
from ParadiseApp.models import Roll, Plan, Pack


def rolls(request):
    rolls = Roll.objects.all()
    form = CreateRoll(request.POST)

    if request.method == 'POST' and form.is_valid():
        roll = Roll()
        roll.producer = form.cleaned_data["producer"]
        roll.number = form.cleaned_data["number"]
        roll.batch = form.cleaned_data["batch"]
        roll.size = form.cleaned_data["size"]
        roll.coating = form.cleaned_data["coating"]
        roll.hardness = form.cleaned_data["hardness"]
        roll.net = form.cleaned_data["net"]
        roll.gross = form.cleaned_data["gross"]
        roll.remainder = form.cleaned_data["net"]

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

def process(request, roll_id):
    roll = Roll.objects.filter(id=roll_id).first()
    packs = Pack.objects.filter(roll_id=roll_id)
    return render (request, "process.html", {"roll": roll, "packs": packs.all(), "packs_bool": packs.count() > 1})

def add_pack(request, roll_id):
    roll = Roll.objects.filter(id=roll_id).first()
    packs = Pack.objects.filter(roll_id=roll_id)
    last_pack = packs.order_by('-date').first()
    pack = Pack()
    pack.number = last_pack.number + 1 if last_pack != None else roll.number + 1
    pack.roll_id = roll.id
    pack.gross = 0
    pack.net = 0
    pack.date = datetime.datetime.now()
    pack.save()

    return render (request, "process.html", {"roll": roll, "packs": packs.all(), "packs_bool": packs.count() > 1})


def delete_pack(request, pack_id, roll_id):
    Pack.objects.filter(id=pack_id).delete()
    return redirect("process", roll_id=roll_id)




