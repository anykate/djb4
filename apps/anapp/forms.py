from django import forms
from bootstrap4.widgets import RadioSelectButtonGroup


class MyForm(forms.Form):
    date = forms.DateField()
    required_css_class = "bootstrap4-req"

    # def clean(self):
    #     cleaned_data = super().clean()
    #     raise forms.ValidationError(
    #         "This error was added to show the non field errors styling.")
    #     return cleaned_data
