# -*- coding: utf-8 -*-

from django.db import models

class Channel(models.Model):
    channel = models.IntegerField()
    def __str__(self):
        return str(self.channel)

class Mote(models.Model):
    MoteId = models.CharField(max_length=100)
    adresse = models.CharField(max_length=42)
    board = models.CharField(max_length=42)
    data = models.CharField(max_length=42)
    viewed = models.DateTimeField(auto_now_add=True, auto_now=False, 
                                verbose_name="Date de déploiement")
    moteChannel = models.ForeignKey(Channel)
    
    def __str__(self):
        return self.board+' '+self.MoteId
class Contact(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.TextField()
    photo = models.ImageField(upload_to="photos/")
    
    def __str__(self):
           return self.nom