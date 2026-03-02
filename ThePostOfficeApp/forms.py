from django import forms
from .models import *

class FormName(forms.ModelForm):
    nam_identifier = models.AutoField(primary_key=True)
    first_name = forms.CharField(max_length=100, label="First Name")
    last_name = forms.CharField(max_length=100, label="Last Name")

    class Meta:
        model = Names
        fields = ('first_name', 'last_name')

        # Required to assign the form-class to each field for rendering
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
        }

class FormAddress(forms.ModelForm):
    address_id = models.AutoField(primary_key=True)
    nam_identifier = models.ForeignKey('Names', models.DO_NOTHING)
    house_no = models.IntegerField(blank=True, null=True)
    house_name = models.CharField(max_length=120, blank=True, null=True)
    street = models.CharField(max_length=120, blank=True, null=True)
    town = models.CharField(max_length=50, blank=True, null=True)
    post_code = models.CharField(max_length=12, blank=True, null=True)
    #role_field = models.CharField(db_column='role_', max_length=6, blank=True, null=True)  # Field renamed because it ended with '_'.
    date_field = models.DateField(db_column='date_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        model = Address
        fields = ('house_no', 'house_name', 'street', 'town', 'post_code', 'date_field')

        # Required to assign the form-class to each field for rendering
        widgets = {
            "house_no": forms.NumberInput(attrs={"class": "form-control"}),
            "house_name": forms.TextInput(attrs={"class": "form-control"}),
            "street": forms.TextInput(attrs={"class": "form-control"}),
            "town": forms.TextInput(attrs={"class": "form-control"}),
            "post_code": forms.TextInput(attrs={"class": "form-control"}),
            #"role_field": forms.TextInput(attrs={"class": "form-control"}),
            "date_field": forms.DateInput(attrs={"class": "form-control"}),
        }
