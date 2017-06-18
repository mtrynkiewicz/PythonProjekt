from django.db import models
from django.core.urlresolvers import reverse

class PaczkaGier(models.Model):
    kreator_paczki = models.CharField(max_length=250)
    nazwa_paczki = models.CharField(max_length=100)
    rodzaj_gier = models.CharField(max_length=100)
    logo_paczki = models.FileField()

    def get_absolute_url(self):
        return reverse('games:detail',kwargs = {'pk':self.pk} )

    def __str__(self):
        return self.kreator_paczki + ': ' + self.nazwa_paczki + '-> ' + self.rodzaj_gier
    def getName(self):
        return self.nazwa_paczki

class Gra(models.Model):
    paczka = models.ForeignKey(PaczkaGier,on_delete=models.CASCADE)
    link_do_pobierania = models.CharField(max_length=200)
    nazwa_gry = models.CharField(max_length=200)
    jest_ulubiona=models.BooleanField(default=False)
    def __str__(self):
        return self.nazwa_gry + ': ' + self.paczka.getName() + '-> ' + self.link_do_pobierania




