from django import forms

class TextForm(forms.Form):
    url = forms.CharField(max_length=200)

class SearchForm(forms.Form):
    mongoId = forms.CharField(max_length=200)