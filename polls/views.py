from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    polls = Poll.objects.all()
    context = {"polls":polls}
    return render(request, "polls/home.html", context)
