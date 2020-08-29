from django import forms
from .models import *

class CreateReviewForm(forms.ModelForm):
    accuracy = forms.IntegerField(max_value=5, min_value=1)
    communication = forms.IntegerField(max_value=5, min_value=1)
    cleanliness = forms.IntegerField(max_value=5, min_value=1)
    value = forms.IntegerField(max_value=5, min_value=1)

    class Meta:
        model = Review
        fields = ("review", "accuracy", "communication", "cleanliness", "value")
        
        def save(self, *args, **kwargs):
            review = super().save(commit=False)
            return review