from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .forms import ReviewForm
from .models import Review

# Create your views here.
class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = '/thank-you'
        

# def review(request):
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             # review = Review(
#             #     user_name=form.cleaned_data['user_name'], 
#             #     review_text=form.cleaned_data['review_text'], 
#             #     rating=form.cleaned_data['rating'])
#             form.save()
#             print(form.cleaned_data)
#             return HttpResponseRedirect('/thank-you')
#     else:
#         form = ReviewForm()

#     return render(request, 'reviews/review.html', {
#         'form': form
#     })

# def thank_you(request):
#     return render(request, 'reviews/thank_you.html')

class ThankYouView(TemplateView):
    template_name = 'reviews/thank_you.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'This is a message'
        return context

    
class ReviewsListView(ListView):
    template_name = 'reviews/review_list.html'
    model = Review
    context_object_name = 'reviews'

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=3)
        return data


class ReviewDetailView(DetailView):
    template_name = 'reviews/review_detail.html'
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get('fav_review')
        context["is_favorite"] = favorite_id == str(loaded_review.id)
        return context
    
    

class FavoriteView(View):
    def post(self, request):
        review_id = request.POST['review_id']
        request.session['fav_review'] = review_id
        return HttpResponseRedirect('/reviews/' + review_id)
