from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.views import View
from django.http import HttpResponseRedirect
from .models import Months, Challenges
from django.views.generic import ListView, DetailView, TemplateView

class StartingPageView(ListView):
    model = Months
    template_name = "challenges/index.html"
    context_object_name = "months"

class MonthlyChallengeDetailView(DetailView):
    template_name = "challenges/challenge.html"
    model = Months
    