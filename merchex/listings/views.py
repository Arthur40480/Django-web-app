from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from listings.models import Band
from listings.models import Announcement
from listings.forms import ContactUsForm, BandForm, AnnouncementForm
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
def create_new_band(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return HttpResponseRedirect(reverse('band-detail', kwargs={'id': band.id}))
    else:
        form = BandForm()

    return render(request,
                  'listings/band_add.html',
                  {'form': form})
def band_update(request, id):
    band = Band.objects.get(id=id)

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('band-detail', kwargs={'id': band.id}))
    else:
        form = BandForm(instance=band)

    return render(request,
                  'listings/band_update.html',
                  {'form': form})

def band_delete(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        band.delete()
        return HttpResponseRedirect(reverse('band-list'))

    return render(request,
                  'listings/band_delete.html',
                  {'band': band})

def about(request):
    return render(request,
                  'listings/about.html')

def listings_list(request):
    announcements = Announcement.objects.all()
    return render(request,
                  'listings/listings.html',
                  {'announcement': announcements})

def listings_detail(request, id):
    announcement = Announcement.objects.get(id=id)
    return render(request,
                  'listings/listings_detail.html',
                  {'announcement': announcement})

def create_new_listing(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            announcement = form.save()
            return HttpResponseRedirect(reverse('listing-detail', kwargs={'id': announcement.id}))
    else:
        form = AnnouncementForm()

    return render(request,
                  'listings/listings_add.html',
                  {'form': form})

def listing_update(request, id):
    listing = Announcement.objects.get(id=id)
    if request.method == 'POST':
        form = AnnouncementForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listing-detail', kwargs={'id': listing.id}))
    else:
        form = AnnouncementForm(instance=listing)

    return render(request,
                  'listings/listing_update.html',
                  {'form': form})

def listing_delete(request, id):
    listing = Announcement.objects.get(id=id)
    if request.method == 'POST':
        listing.delete()
        return HttpResponseRedirect(reverse('listing-list'))

    return render(request,
                  'listings/listing_delete.html',
                  {'listing': listing})
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

