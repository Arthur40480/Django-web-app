from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Announcement
from listings.forms import ContactUsForm
from django.core.mail import send_mail


def band_list(request):
    bands = Band.objects.all()
    return render(request,
                  'listings/band_list.html',
                  {'bands': bands})

def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request,
                  'listings/band_detail.html',
                  {'band': band})

def about(request):
    return render(request,
                  'listings/about.html')

def listings(request):
    announcements = Announcement.objects.all()
    return render(request,
                  'listings/listings.html',
                  {'announcement': announcements})

def listings_detail(request, id):
    announcement = Announcement.objects.get(id=id)
    return render(request,
                  'listings/listings_detail.html',
                  {'announcement': announcement})

def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message de {form.cleaned_data["name"] or "Anonyme"} via Merchex Contact Us Form',
                message=form.cleaned_data["message"],
                from_email=form.cleaned_data["email"],
                recipient_list=["admin@merchex.xyz"]
            )
    else:
        print("La méthode de requête est :", request.method)
        print("Les données POST sont :", request.POST)
        form = ContactUsForm()

    return render(request,
                'listings/contact.html',
                {'form': form})

