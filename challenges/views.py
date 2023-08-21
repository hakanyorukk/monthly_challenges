from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string
from django.views import View
from django.http import HttpResponseRedirect
from .models import Months, Challenges, Note
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.sessions.models import Session
from .forms import NoteForm
from django.urls import reverse

class StartingPageView(ListView):
    model = Months
    template_name = "challenges/index.html"
    context_object_name = "months"

# class MonthlyChallengeDetailView(DetailView):
#     template_name = "challenges/challenge.html"
#     model = Months
#     context_object_name="month"
class MonthlyChallengeDetailView(View): 
    def is_accepted_challenges(self, request, month_id):
        accepted_challenges = request.session.get("accepted_challenges")

        if accepted_challenges is not None:
            is_accepted_challenges = month_id in accepted_challenges
        else:
            is_accepted_challenges=False

        return is_accepted_challenges
    
    def get(self,request, slug):
        month = Months.objects.get(slug=slug)
        context = {
            "month":month,
            "save_challenge":self.is_accepted_challenges(request, month.id),
            "note_form":NoteForm(),
            "notes":month.notes.all()
        }
        return render(request, "challenges/challenge.html", context)
    
    
    def post(self, request, slug):  
        note_form = NoteForm(request.POST)
        month = Months.objects.get(slug=slug)

        if note_form.is_valid():
            note = note_form.save(commit=False)
            note.month = month
            note.save()
            return redirect("month_challenge", slug=slug)

        context = {
            "month":month,
            "save_challenge":self.is_accepted_challenges(request, month.id),
            "note_form":note_form,
            "notes":month.notes.all()

        }
        return render(request, "challenges/challenge.html", context)
    
class AcceptChallenge(View):
    def get(self,request):
        accepted_challenges = request.session.get("accepted_challenges")
        context = {}

        if accepted_challenges is None:
            context["months"] = []
            context["has_accept"] = False
            return render(request, "challenges/accept-challenge.html", context)
        else:
            month = Months.objects.filter(id__in=accepted_challenges)
            context["months"] = month
            context["has_accept"] = True
            context["save-challenge"] = True
        return render(request, "challenges/accept-challenge.html", context)


    def post(self,request):
        accepted_challenges = request.session.get("accepted_challenges")

        if accepted_challenges is None:
            accepted_challenges = []
        
        month_id = int(request.POST["month_id"])
        print(month_id)
        if month_id not in accepted_challenges:
            accepted_challenges.append(month_id)
        else:
            accepted_challenges.remove(month_id)
        request.session["accepted_challenges"] = accepted_challenges
        return HttpResponseRedirect("/")


        