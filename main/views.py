from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from .models import Post

import stripe
stripe.api_key = "sk_test_51Mp2llG92vk5YkSuQxjvt7gDEivGTxbsZ3ho8roVdi7omgYctlzSFRThE4oSSOna5FI0u2XtGbEKEIyUIpt8ebF400V3yVWsIt"

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    
    return render(request, 'main/index.html', context)
    # return render(request, 'main/index.html', context)
def about(request):
    return render(request, 'main/about.html', {'title': 'About'})
def setcard(request):
    return render(request, 'main/setcard.html', {'title': 'Setcard'})
def autogram(request):
    return render(request, 'main/autogram.html', {'title': 'Autogram'})
def help(request):
    return render(request, 'main/help.html', {'title': 'Help'})
def portalhelp(request):
    return render(request, 'main/portalhelp.html', {'title': 'Portal Hilfe'})
def gallery(request):
    return render(request, 'main/gallery.html', {'title': 'Trailer'})
def booking(request):
    return render(request, 'main/booking.html', {'title': 'Booking'})

def school(request):
    return render(request, 'main/school.html', {'title': 'school'})
def coffee(request):
    return render(request, 'main/coffee.html', {'title': 'coffee'})
def vanilla(request):
    return render(request, 'main/vanilla.html', {'title': 'vanilla'})
def poesiealbum(request):
    return render(request, 'main/poesiealbum.html', {'title': 'Poesiealbum'})
def community(request):
    return render(request, 'main/community.html', {'title': 'Community'})
def events(request):
    return render(request, 'main/events.html', {'title': 'Events'})
def schulbesuche(request):
    return render(request, 'main/index.html', {'title': 'Schulbesuche'})
def projects(request):
    return render(request, 'main/projects.html', {'title': 'Projects'})
# def book(request):
#     return render(request, 'main/landingpage.html', {'title': 'Buch'})
   
# def book(request):
#      return render(request, 'main/landingpage_test.html', {'title': 'Buch'})

# def book(request):
#      return render(request, 'main/landingpage_responsive.html', {'title': 'Buch'})
def book(request):
     return render(request, 'main/landingpage_new_version.html', {'title': 'Buch'})


     
def donate(request):
    return render(request, 'main/donate.html', {'title': 'Spende'})

def charge(request):
    amount = 5
    if request.method == 'POST':
        print('Data:', request.POST)

    return redirect(reverse('success', args=[amount]))

def successMsg(request, args):
    amount = args
    return render(request, 'main/success.html', {'amount': amount})

def chat(request):
    return render(request, 'main/chat.html', {'title': 'Chat'})
