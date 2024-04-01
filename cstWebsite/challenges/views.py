from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

def monthly_challenges() -> dict[str,str]:
    challenges = {
        "january" : "Eat Satvik",
        "february" : "Sleep Early",
        "march" : "Sadhana Regular",
        "april" : "Seva Regular",
        "may" : "Knowledge Series with Pure Intention",
        "june" : "Advance Course",
        "july" : None,
        "august" : "Blessing Course",
        "september" : "Sanyam",
        "october" : "Intuition Program",
        "november" : "Yoga Level 2",
        "december" : "Sahaj Meditation"
    }
    return challenges

def index(request):
    months = list(monthly_challenges().keys())
    # list_items = ""
    # for month in months:
    #     capatilized_month = month.capitalize()
    #     month_path = reverse("monthly-challenges", args=[month])
    #     list_items += f"<li> <a href=\"{month_path}\">{capatilized_month}</a></li>"
    
    # return HttpResponse(list_items)
    return render(request, "challenges/index.html", {
        "months" : months
    })

def monthly_challenges_by_name(request, month):
    try:
        challenges = monthly_challenges()
        monthly_challenges1 = challenges[month]
        # response_data = f"<h1>{monthly_challenges1}</h1>"
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
        return render(request,"challenges/challenge.html", {
            "text" : monthly_challenges1,
            "month_name" : month
        })
    except:
        raise Http404()

def monthly_challenges_by_number(request, month):
    monthly_challenges1 = list(monthly_challenges().keys())
    if len(monthly_challenges1) < month:
        return HttpResponseNotFound("Invalid Month")
    
    redirect_month = monthly_challenges1[month-1]
    redirect_path = reverse("monthly-challenges", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
