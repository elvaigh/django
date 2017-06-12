# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^accueil$', views.accueil),
    url(r'^sensor/(\d+)$', views.view_sensor),  # Vue d'un article
    url(r'^connexion$', views.connexion),  # Vue d'un article
    url(r'^date$', views.date_actuelle),
    url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/$', views.addition),
    url(r'^$', views.accueil, name='accueil'),
    url(r'^capteur/(\d+)$', views.lire, name='lire'),
    url(r'^contact$', views.nouveau_contact, name='nouveau_contact'),
    url(r'^voir$', views.voir_contacts, name='voir_contacts'),

]