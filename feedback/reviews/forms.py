from django import forms

from .models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label='Your name', max_length=80, error_messages={
#         'required': 'Your name must not be empty',
#         'max_length': 'Names must not have more than 80 characters'
#     })
#     review_text = forms.CharField(label='Your feedback', widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label='Your rating', min_value=1, max_value=6)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        labels = {
            'user_name': 'Your name',
            'review_text': 'Your feedback',
            'rating': 'Your rating'
        }
        error_messages = {
            'user_name': {
                'required': 'Your name must not be empty',
                'max_length': 'Names must not have more than 80 characters'
            }
        }
