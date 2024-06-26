from django.urls import path

from.import views
from .views import DetailView

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="index"), #starting page
    path("months/<slug:slug>", views.MonthlyChallengeDetailView.as_view(), name="month_challenge"),
    path("accept-challenge/", views.AcceptChallenge.as_view(), name="accept-challenge"),
    path("months/delete-not/<int:note_id>", views.delete_note, name="delete-note")
    #path("accept-challenge/", views.AcceptChallenge.as_view(), name="accept-challenge")

]