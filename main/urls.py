from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main-home'),
    path('about/', views.about, name='main-about'),
    path('setcard/', views.setcard, name='main-setcard'),
    path('autogram/', views.autogram, name='main-autogram'),
    path('help/', views.help, name='main-help'),
    path('hilfe/', views.portalhelp, name='main-portalhelp'),
    path('poesie/', views.poesiealbum, name='main-poesiealbum'),
    path('booking/', views.booking, name='main-booking'),
    path('school/', views.school, name='main-school'),
    path('coffee/', views.coffee, name='main-coffee'),
    path('vanilla/', views.vanilla, name='main-vanilla'),
    path('community/', views.community, name='main-community'),
    path('events/', views.events, name='main-events'),
    path('schulbesuche/', views.schulbesuche, name='main-schulbesuche'),
    path('projekte/', views.projects, name='main-projects'),
    path('buch/', views.book, name='main-book'),
    path('spende/', views.donate, name='main-donate'),
    path('kontakt/', views.contact, name='main-contact'),
     path('impressum/', views.impressum, name='main-impressum'),
    path('charge/', views.charge, name='main-charge'),
    path('success/<str:args>/', views.successMsg, name='main-success'),
    path('chat/', views.chat, name='main-chat'),
]
