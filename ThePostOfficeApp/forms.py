from django import forms
from .models import *

Letter_choices = [
    ("Select Class", "Select Class"),
    ("1st Class Post", "1st Class Post"),
    ("2nd Class Post", "2nd Class Post"),
]

Courier_choices = [
        ("Select Courier", "Select Courier"),
        ("Evri", "Evri"),
        ("DPD", "DPD"),
        ("Parcel Force", "Parcel Force"),
    ]

Parcel_service = [
        ("Select Service", "Select Service"),
        ("Standard Delivery", "Standard Delivery"),
        ("Next-Day", "Next-Day"),
    ]

class NameForm(forms.ModelForm):
    class Meta:
        model = Name
        fields = ["first_name", "last_name"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
        }

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["house_no", "house_name", "street", "town", "post_code"]
        widgets = {
            "house_no": forms.NumberInput(attrs={"class": "form-control"}),
            "house_name": forms.TextInput(attrs={"class": "form-control"}),
            "street": forms.TextInput(attrs={"class": "form-control"}),
            "town": forms.TextInput(attrs={"class": "form-control"}),
            "post_code": forms.TextInput(attrs={"class": "form-control"}),
        }

class PostLetterForm(forms.ModelForm):
    class_field = forms.ChoiceField(choices=Letter_choices, label="Postage Class",widget=forms.Select(attrs={"class": "form-select"}))
    letter_sent = forms.DateField(required=True,widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}))
    class Meta:
        model = Letter
        fields = ("letter_sent", "class_field")


class PostParcelForm(forms.ModelForm):
    courier = forms.ChoiceField(choices=Courier_choices,label="Chose Courier",widget=forms.Select(attrs={"class": "form-select"}) )
    parcel_sent = forms.DateField(required=True,widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}))
    service = forms.ChoiceField(choices=Parcel_service,label="Chose Service",widget=forms.Select(attrs={"class": "form-select"}) )
    weight = forms.DecimalField(max_digits=5, decimal_places=2, required=True)
    class Meta:
        model = Parcel
        fields = ("courier", "parcel_sent", "service", "weight")