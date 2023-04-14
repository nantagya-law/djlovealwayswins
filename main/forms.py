from django import forms


class ContactForm(forms.Form):
    vorname = forms.CharField(max_length=100)
    nachname = forms.CharField(max_length=100)
    email = forms.EmailField()
    nachricht = forms.CharField(widget=forms.Textarea)
