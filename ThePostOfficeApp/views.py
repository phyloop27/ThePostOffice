from .forms import *
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.db import transaction

def landing(request):
    return render(request, 'landing_page.html')

def login(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def customerDetails(request):
    customer_list = Name.objects.select_related("address").all()
    return render(request, "customer_details.html", {"customer_list": customer_list})

def postedItems(request):
    parcel_list = Parcel.objects.select_related("address").all()
    letter_list = Letter.objects.select_related("address").all()
    return render(request, "posted_items.html", {"parcel_list": parcel_list, "letter_list" : letter_list})


def formName(request):
    if request.method == "POST":
        name_form = NameForm(request.POST)
        address_form = AddressForm(request.POST)

        if name_form.is_valid() and address_form.is_valid():
            with transaction.atomic():
                name = name_form.save()
                address = address_form.save(commit=False)
                # sharing pk here -
                address.name = name
                address.save()

            return redirect("formLetter", name_id=name.pk)
    else:
        name_form = NameForm()
        address_form = AddressForm()

    return render(request,"form_name.html",
                  {"name_form": name_form, "address_form": address_form})


def formLetter(request, name_id):
    #print('formLetter name_id:', name_id)
    # pulling name_id from the input to aline letter to address
    address = get_object_or_404(Address, pk=name_id)

    if request.method == "POST":
        form = PostLetterForm(request.POST)
        if form.is_valid():
            # creating letter object
            Letter.objects.create(
                address = address,
                letter_sent = form.cleaned_data["letter_sent"],
                class_field = form.cleaned_data["class_field"],
            )

            return redirect("formSuccess")
    else:
        form = PostLetterForm()
    return render(request, "form_letter.html", {"form": form, "name_id" : name_id})


def formParcel(request, name_id):
    #print('formParcel name_id:', name_id)
    # pulling name_id from the input to aline letter to address
    address = get_object_or_404(Address, pk=name_id)

    if request.method == "POST":
        form = PostParcelForm(request.POST)
        if form.is_valid():

            # create Parcel object
            Parcel.objects.create(
                address = address,
                courier = form.cleaned_data["courier"],
                parcel_sent = form.cleaned_data["parcel_sent"],
                service = form.cleaned_data["service"],
                weight = form.cleaned_data["weight"],
            )

            return redirect("formSuccess")
    else:
        form = PostParcelForm()
    return render(request, "form_parcel.html", {"form": form, "name_id" : name_id})


def formSuccess(request):
    return render(request, 'form_success.html')


def delete(request, identifier):
    # Deleting record using 'pk' Values
    customer = get_object_or_404(Name, pk=identifier)
    if request.method == "POST":
        customer.delete()
        return redirect("customerDetails")
    return render(request, "delete.html", {"customer": customer})

def update(request, identifier):
    customer = get_object_or_404(Name, identifier=identifier)
    address = get_object_or_404(Address, pk=customer.pk)

    if request.method == "POST":
        name_form = NameForm(request.POST, instance=customer)
        address_form = AddressForm(request.POST, instance=address)

        if name_form.is_valid() and address_form.is_valid():
            with transaction.atomic():
                name_form.save()
                address_form.save()
            return redirect("customerDetails")
    else:
        name_form = NameForm(instance=customer)
        address_form = AddressForm(instance=address)

    return render(request,"update.html",{
            "name_form": name_form,
            "address_form": address_form,
            "customer": customer,
            "is_edit": True,
        })



