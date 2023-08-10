from django.urls import path

from.import views

urlpatterns = [
    path("", views.index, name="index"), #/challenges/
    path("<int:month>", views.monthly_challenge_by_number), #1,2...12
    path("<str:month>", views.monthly_challenge, name="month_challenge"), #reverse functions,
     #urltags, dynamic url
]