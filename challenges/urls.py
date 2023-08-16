from django.urls import path

from.import views
from .views import DetailView

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="index"), #starting page
    path("months/<int:pk>", views.MonthlyChallengeDetailView.as_view(), name="month_challenge")
]