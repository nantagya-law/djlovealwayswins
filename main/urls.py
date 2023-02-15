from django.urls import path
from . import views

urlpatterns = [
    path('/', views.home, name='main-root'),
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
    path('gallery/', views.gallery, name='main-gallery'),
    path('projekte/', views.projects, name='main-projects'),
    path('buch/', views.book, name='main-book'),
    path('spende/', views.donate, name='main-donate'),
    path('chat/', views.chat, name='main-chat'),
]
