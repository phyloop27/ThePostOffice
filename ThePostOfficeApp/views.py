from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def landing(request):
    return render(request, 'landing_page.html')

def login(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def customerDetails(request):
    return render(request, 'customer_details.html')

def postedItems(request):
    return render(request, 'posted_items.html')

def prices(request):
    return render(request, 'prices.html')

def postOfficeSales(request):
    return render(request, 'post_office_sales.html')

def formName(request):
    if request.method == "POST":
        form = FormName(request.POST) # This should be calling the '(form name)' From forms.py
        if form.is_valid():
            form.save()
            return redirect("formAddress") # Next webpage to render to
    else:
        form = FormName() # This should be calling the '(form name)' From forms.py
    return render(request, "form_name.html", {"form": form})

def formAddress(request):
    if request.method == "POST":
        form = FormAddress(request.POST) # This should be calling the '(form name)' From forms.py
        if form.is_valid():
            form.save()
            return redirect("formPostage") # Next webpage to render to
    else:
        form = FormAddress() # This should be calling the '(form name)' From forms.py
    return render(request, 'form_address.html', {"form": form})

def formPostage(request):
    return render(request, 'form_postage.html')

def formSuccess(request):
    return render(request, 'form_success.html')

def delete(request):
    return render(request, 'delete.html')

def update(request):
    return render(request, 'update.html')