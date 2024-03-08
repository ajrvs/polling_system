from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    polls = Poll.objects.all()
    context = {"polls":polls}
    return render(request, "polls/home.html", context)

def poll(request, id):
    poll = Poll.objects.filter(pk=id)
    choices = Poll.objects.filter(poll=poll)
    context = {"poll":poll, "choices":choices}
    return render(request, "polls/poll.html", context)