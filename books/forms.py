from django import forms
from books.models import Review


class ReviewForm(forms.ModelForm):
    stars_given = forms.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = Review
        fields = ("stars_given", "comment")