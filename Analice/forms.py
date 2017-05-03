from django import forms

class TextForm(forms.Form):
    text_content = forms.CharField(label='text',widget=forms.Textarea, max_length=100)