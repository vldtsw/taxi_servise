from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django import forms

from taxi.models import Driver


class DriverCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Driver
        fields = UserCreationForm.Meta.fields + ("license_number",
                                                 "first_name",
                                                 "last_name")

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]

        if len(license_number) != 8:
            raise ValidationError("Number should consist 8 characters")

        if not license_number[:3].isupper() or not license_number[:3].isalpha():
            raise ValidationError("First 3 characters must be uppercase letters")

        if not license_number[3:].isdigit():
            raise ValidationError("Last 5 characters must be digits")

        return license_number


class CarSearchForm(forms.Form):
    title = forms.CharField(
        max_length=15,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by model..."})
    )
