from django.urls import path

from.import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="index"), #starting page
    path("<slug:slug>", views.MonthlyChallenge.as_view(), name="month_challenge") #reverse functions,#urltags, dynamic url
    #path("accepted/challenges", views.AcceptedChallenges.as_view(), name="challenges")
]