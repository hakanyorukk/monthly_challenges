from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.views import View
from django.http import HttpResponseRedirect
from .models import Months, Challenges
from django.views.generic import ListView, DetailView, TemplateView

# Create your views here.
class StartingPageView(ListView):
    model = Months
    template_name = "challenges/index.html"
    context_object_name = "months"

class MonthlyChallenge(ListView):
    template_name = "challenges/challenge.html"
    model = Challenges
    context_object_name = "monthlychallenge"
   
    # def get(self, request):
    #     challenge = Challenges.objects.get(pk=id)  # Query the Months model to get all months
    #     return render(request, "challenges/starting_page.html", {"months": challenge.month})

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
  
    # def challenge_detail(request, slug):
    #     #month_name = Months.objects.all(pk=id)
    #     identified_challenge = get_object_or_404(Challenges, slug=slug)
    #     return render(request, "blog/post-detail.html", {
    #         "post":identified_challenge,
    #         "post_tags":identified_challenge.months.all(pk=id),
    #     #"image": image_name  #Now it si dynmaic we don't need this
    #     })