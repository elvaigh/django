# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404
from datetime import datetime
from sonsorMenager.models import Mote,Channel,Contact
from forms import NouveauContactForm

def home(request):    
    return render(request, 'sonsorMenager/base.html', locals())

def view_sensor(request, id_sensor):
    """ 
    Vue qui affiche un article selon son identifiant (ou ID, ici un numéro)
    Son ID est le second paramètre de la fonction (pour rappel, le premier
    paramètre est TOUJOURS la requête de l'utilisateur)
    """
    return HttpResponse(
        "Vous avez demandé le capteur #{0} !".format(id_sensor)    
    )


def connexion(request):
    # Il veut des articles ? Soyons fourbe et redirigeons-le vers djangoproject.com
    return redirect(accueil)

def date_actuelle(request):
    return render(request, 'sonsorMenager/date.html', {'date': datetime.now()})


def addition(request, nombre1, nombre2):    
    total = int(nombre1) + int(nombre2)

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'sonsorMenager/add.html', locals())

def accueil(request):
	# Nous sélectionnons tous nos capteurs
	return render(request,'sonsorMenager/accueil.html',{'motes': Mote.objects.all()})
def lire(request, id):
    return render(request, 'sonsorMenager/lire.html', {'mote': get_object_or_404(Mote,id=id)})
def nouveau_contact(request):
    sauvegarde = False
    form = NouveauContactForm(request.POST or None, request.FILES)
    if form.is_valid():
        contact = Contact()
        contact.nom = form.cleaned_data["nom"]
        contact.adresse = form.cleaned_data["adresse"]
        contact.photo = form.cleaned_data["photo"]
        contact.save()
        sauvegarde = True

    return render(request, 'sonsorMenager/contact.html', {
        'form': form, 
        'sauvegarde': sauvegarde
    })

def voir_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'sonsorMenager/voir_contacts.html', {'contacts': contacts})