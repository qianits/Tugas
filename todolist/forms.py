from django import forms

class Input_Form(forms.Form):
    title = forms.CharField(label="Title", max_length=250)
    description = forms.CharField(label="Description", max_length=250)