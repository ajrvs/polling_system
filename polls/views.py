from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import *

# Create your views here.
def home(request):
    polls = Poll.objects.all()
    context = {"polls":polls}
    return render(request, "polls/home.html", context)

def poll(request, id):
    poll = get_object_or_404(Poll, pk=id)
    choices = Choice.objects.filter(poll=poll)
    context = {"poll":poll, "choices":choices}
    return render(request, "polls/poll.html", context)

def vote(request, id):
    poll = Poll.objects.get(pk=id)
    choices = Choice.objects.filter(poll=poll)
    if request.method == "POST":
        selected_choice_id = request.POST.get("choice")
        # selected_choice = Choice.objects.get(pk=selected_choice_id) -> raise exception that needs to be manally handled
        if selected_choice_id:
            selected_choice = get_object_or_404(Choice, pk=selected_choice_id)
            selected_choice.votes += 1
            selected_choice.save()
            messages.success(request, "Voted successfully!")
            return redirect("detail", id=id)
        else:
            messages.error(request, "Please select a choice before voting.")
        context = {"poll":poll, "choices":choices}
        return render(request, "polls/poll.html", context)

def detail(request, id):
    poll = get_object_or_404(Poll, pk=id)
    choices = Choice.objects.filter(poll=poll)
    context = {"poll":poll, "choices":choices}
    return render(request, "polls/detail.html", context)

def all(request):
    polls = Poll.objects.all()
    # choices = Choice.objects.filter(poll=poll)
    context = {"polls":polls}
    return render(request, "polls/all.html", context)