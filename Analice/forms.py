from django import forms

class TextForm(forms.Form):
    url = forms.URLField(max_length=200)

class SearchForm(forms.Form):
    id = forms.TimeField()