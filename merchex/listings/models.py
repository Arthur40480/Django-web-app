from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Band(models.Model):

    def __str__(self):
        return f'{self.name}'

    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
        FUNKY_MUSIC = 'FM'
        ELECTRO_MUSIC = 'EM'

    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    name = models.fields.CharField(max_length=100)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2023)]
    )
    active = models.fields.BooleanField(default=True)
    official_page = models.fields.URLField(null=True, blank=True)


class Announcement(models.Model):

    class Type(models.TextChoices):
        CLOTHINGS = 'CLO'
        SHOES = 'SHO'
        POSTER = 'POS'
        RECORDS = 'REC'
        MISCELLANEOUS = 'MIS'


    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=500)
    year = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2023)]
    )
    sold = models.fields.BooleanField(default=False)
    type = models.fields.CharField(choices=Type.choices, max_length=5)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
    like_new = models.fields.BooleanField(default=False)

