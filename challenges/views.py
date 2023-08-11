from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges_dic = {
    "january": "01",
    "february":"02",
    "march":"03",
    "april":"04",
    "may":"05",
    "june":"06",
    "july":"07",
    "august":"This is a branch test 11/08/2023!",
    "september":"09",
    "october":"010",
    "november":"011",
    "december":None
}
# Create your views here.

def index(request):
    months = list(monthly_challenges_dic.keys())

    return render(request, "challenges/index.html", {
        "months":months
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges_dic.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month-1]
    redirect_path = reverse("month_challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges_dic[month]

        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)

