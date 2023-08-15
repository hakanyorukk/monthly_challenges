from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.views import View
from django.http import HttpResponseRedirect
from .models import Months, Challenges
from django.views.generic import ListView, DetailView

# Create your views here.
class StartingPageView(ListView):
    model = Months
    template_name = "challenges/index.html"
    context_object_name = "months"

class MonthlyChallenge(DetailView):
    model = Challenges
    template_name = "challenges/challenge.html"
    context_object_name = "challenges"  

# class AcceptedChallenges(View):
#     def get(self,request):
#         accepted_challenges = request.session.get("accepted_challenges")
#         context = {}

#         if accepted_challenges is None or len(accepted_challenges) == 0:
#             context["accepts"] = 0
#             context["has_challenge"] = False
#         else:

#             context["has_challenge"] = True
#             print("accepted_challenges:", accepted_challenges)

#         return render(request,"challenges/accepted-challenges.html", context)

#     def post(self,request):
#         accepted_challenges = request.session.get("accepted_challenges")
#         if accepted_challenges is None:
#             accepted_challenges = []

#         accept_id = request.POST["challenge_id"]
#         if accept_id not in accepted_challenges:
#             accepted_challenges.append(accept_id)
#         else: 
#             accepted_challenges.remove(accept_id)
#         request.session["accepted_challenges"] = accepted_challenges
#         return HttpResponseRedirect("/")
  
