from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    'january': 'Lose 10 pounds',
    'february': 'Run 5k with cats',
    'march': 'Learn Django by the end of the month',
    'april': 'Cut your hair',
    'may': 'Don\'t forget mother\'s day',
    'june': 'Finish the semester strong',
    'july': 'Enjoy the summer holidays',
    'august': 'This is a mid month',
    'september': 'Celebrate the national holidays',
    'october': 'Be spooky',
    'november': 'Eat cake',
    'december': None
}

# Create your views here.


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, 'challenges/index.html', {
        "months": months
    })


def monthly_challange_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        raise Http404()

    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, 'challenges/challenge.html', {
            "month": month,
            "challenge": challenge_text
        })
    except:
        raise Http404()
