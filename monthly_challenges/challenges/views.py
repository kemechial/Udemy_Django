from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.
'''
def january(request):
    return HttpResponse("It works!")

def february(request):
    return HttpResponse("This works, too!")

'''
month_index = ["###","january", "february", "march", "april", "may"]

monthly_challenges = {"january" : "eat some cake",
                      "february" : "do some exercise", "march" : "no idea",
                      "april" : None,
                      "may" : "summer is close!",
                      "june" : "eat some ice cream",
                      "july" : "too hot..."}
'''
def index(request):
    months_list=""

    for m in monthly_challenges.keys():
        month_path = reverse("month-challenge", args=[m])
        months_list += f"<li><a href = \"{month_path}\" >{m.capitalize()}</a></li>"
    response_data = f"<ul>{months_list}</ul>"
    return HttpResponse(response_data)

'''
def index(request):
    months = list(monthly_challenges.keys())   
    return render(request, "challenges/index.html", 
                {"months" : months})


def monthly_challenge_number(request, month):
    #forward_month = month_index[month]
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month!")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    #return HttpResponseRedirect("/challenges/" + months[month-1]) This is hard coded! not good...
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    if month in monthly_challenges.keys():
        challenge_text = monthly_challenges[month]
        response_text = f"<h1>{challenge_text}</h1>"
        """
        response_text = render_to_string("challenges/challenge.html")
        return HttpResponse(response_text)
        """
        return render(request, "challenges/challenge.html",{"month_name": month, "text" : challenge_text})
    else:
        #return HttpResponseNotFound("<div><b>This is not a valid month!</b></div>")
        
        response_data =  render_to_string("404.html")
        return HttpResponseNotFound(response_data)
    
    #alternative raise http404()
