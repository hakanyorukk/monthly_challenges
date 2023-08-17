from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.views import View
from django.http import HttpResponseRedirect
from .models import Months, Challenges
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.sessions.models import Session

class StartingPageView(ListView):
    model = Months
    template_name = "challenges/index.html"
    context_object_name = "months"

class MonthlyChallengeDetailView(DetailView):
    template_name = "challenges/challenge.html"
    model = Months
    context_object_name="month"

class AcceptChallenge(View):
    def get(self,request):
        accepted_challenges = request.session.get("accepted_challenges")
        context = {}

        if accepted_challenges is None:
            context["accepts"] = []
            context["has_accept"] = False

        else:
            accepts = Months.objects.filter(id__in=accepted_challenges)
            context["accepts"] = accepts
            context["has_accept"] = True
        return render(request, "challenges/accept-challenge.html", context)


    def post(self,request):
        accepted_challenges = request.session.get("accepted_challenges")

        if accepted_challenges is None:
            accepted_challenges = []
        
        month_id = int(request.POST["month_id"])
        if month_id not in accepted_challenges:
            accepted_challenges.append(month_id)
            print(month_id)

        request.session["accepted_challenges"] = accepted_challenges
        return HttpResponseRedirect("/")