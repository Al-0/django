from django import forms

class ReviewForm(forms.Form):
    user_name = forms.CharField(label='Your name', max_length=80, error_messages={
        'required': 'Your name must not be empty',
        'max_length': 'Names must not have more than 80 characters'
    })
