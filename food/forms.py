from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='Search for Dishes', max_length=120)
