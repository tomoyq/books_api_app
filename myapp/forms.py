from django import forms

class SerchForm(forms.Form):
    title = forms.CharField(label='タイトル', max_length=200, required=True)