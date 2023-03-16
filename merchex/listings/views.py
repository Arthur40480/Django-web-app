from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Announcement

def hello(request):
    bands = Band.objects.all()
    announcements = Announcement.objects.all()
    return HttpResponse(f"""
        <h1>Hello Django !</h1>
        <p>Mes groupes préférés sont :
        <ul>
            <li>{bands[0].name}</li>
            <li>{bands[1].name}</li>
            <li>{bands[2].name}</li>
        </ul>
        
        <p> Voici les différentes annonces :</p>
        <ul>
            <li>{announcements[0].title}</li>
            <li>{announcements[1].title}</li>
            <li>{announcements[2].title}</li>
        </ul>
""")

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch!</p>')

def listings(request):
    return HttpResponse('<h1>Voici notre liste des articles</h1>')

def contact(request):
    return HttpResponse('<h1>Remplissez le formulaire pour nous contactez</h1>')

