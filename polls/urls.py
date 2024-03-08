from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("polls/", views.home, name="home"), # not necessary
    path("polls/all/", views.all, name="all"),
    path("polls/<int:id>", views.poll, name="poll"),
    path("polls/<int:id>/vote", views.vote, name="vote"),
    path("polls/<int:id>/detail", views.detail, name="detail"),
]