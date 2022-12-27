from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
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
    'december': 'Don\'t be a grinch'
}

# Create your views here.


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        month_path = reverse('month-challenge', args=[month])
        list_items += f'<li><a href="{month_path}">{month.capitalize()}</a></li>'

    response_data = f"""
        <ul>
            {list_items}
        </ul>
    """

    return HttpResponse(response_data)


def monthly_challange_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('<h1>Invalid month</h1>')

    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f'<h1>{challenge_text}<h1>'
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")
