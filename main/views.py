from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'main/index.html', context)
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
def trailer(request):
    return render(request, 'main/trailer.html', {'title': 'Trailer'})
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
def gallery(request):
    return render(request, 'main/gallery.html', {'title': 'Gallery'})
def projects(request):
    return render(request, 'main/projects.html', {'title': 'Projects'})
def book(request):
    return render(request, 'main/landingpage.html', {'title': 'Buch'})
    #return render(request, 'main/book.html', {'title': 'Buch'})
def donate(request):
    return render(request, 'main/donate.html', {'title': 'Spende'})
def chat(request):
    return render(request, 'main/chat.html', {'title': 'Chat'})
