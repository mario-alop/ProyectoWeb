from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(required=True, max_length=150)
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)