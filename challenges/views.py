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

class AcceptChallenge(View):
    def get(self,requset):
        accepted_challenges = requset.session.get("accepted_challenges")
        context = {}

        if accepted_challenges is None:
            context["accepts"] = []
            context["has_accept"] = False

        else:
            accepts = Months.objects.filter(id__in=accepted_challenges)
            context["accepts"] = accepts
            context["has_accept"] = True
        return render(requset, "", context)


    def post(self,requset):
        accepted_challenges = requset.session.get("accepted_challenges")

        if accepted_challenges is None:
            accepted_challenges = []
        
        accept_id = requset.POST["accept_id"]

        if accept_id not in accepted_challenges:
            print(accept_id)
            print(accepted_challenges)
            accepted_challenges.append(accept_id)

        else:
            accepted_challenges.remove(accept_id)

        requset.session["accepted_challenges"] = accepted_challenges
        return HttpResponseRedirect("/")