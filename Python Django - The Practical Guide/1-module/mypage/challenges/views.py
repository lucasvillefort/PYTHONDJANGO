from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

# Create your views here. where we will create what will be seems by the clients

monthly_challenges = {
    "january": "this works january",
    "february": "walk for at least 20 minute february",
    "march": "learnin Django for at least 20 minute' march",
    "april": "this works april",
    "may": "walk for at least 20 minute may",
    "june": "learnin Django for at least 20 minute' june",
    "july": "walk for at least 20 minute july",
    "august": "learnin Django for at least 20 minute' august",
    "september": "walk for at least 20 minute september",
    "october": "learnin Django for at least 20 minute' october",
    "november": "walk for at least 20 minute november",
    "december": "learnin Django for at least 20 minute' december",
}


def index(request):

    list_items = ""
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {"months": months})


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("number of month is not supported")
    redirect_month = months[month - 1]
    redirect_path = reverse(
        "month-challenge", args=[redirect_month]
    )  # /challenge/january exemplo
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):  # it is gonna be a trigger
    try:
        chanllenge_text = monthly_challenges[month]
        return render(
            request,
            "challenges/challenge.html",
            {"text": chanllenge_text, "month_name": month},
        )
    except:
        return HttpResponseNotFound("<h1>this month is not supported</h1>")
