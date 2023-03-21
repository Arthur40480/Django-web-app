from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Announcement


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
    return render(request,
                  'listings/contact.html')

