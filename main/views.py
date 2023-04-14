from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.conf import settings

from django.urls import reverse
from django.http import JsonResponse, HttpResponse
from .models import Post, Contact

from .forms import ContactForm

# import stripe
# stripe.api_key = "sk_test_51Mp2llG92vk5YkSuQxjvt7gDEivGTxbsZ3ho8roVdi7omgYctlzSFRThE4oSSOna5FI0u2XtGbEKEIyUIpt8ebF400V3yVWsIt"

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
    return render(request, 'main/school_visiting.html', {'title': 'Schulbesuche'})
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

def contact(request):
    # if request.method == 'POST':
    #     form = ContactForm(request.POST)

    #     if form.is_valid():
   

    #         vorname = form.cleaned_data['vorname']
    #         nachname = form.cleaned_data['nachname']
    #         email = form.cleaned_data['email']
    #         nachricht = form.cleaned_data['nachricht']
    #         subject = 'LAW INFO'
    #         from_email = settings.EMAIL_HOST_USER
    #         recipient_list = settings.RECIPIENT_LIST

           

    #         html = render_to_string('main/emails/contactform.html', {
    #             'vorname': vorname,
    #             'nachname': nachname,
    #             'email': email,
    #             'nachricht': nachricht
    #         })

    #         # send_mail(subject, nachricht, 'noreply@law.de', ['jmkaggwa@gmail.com'], html_message=html)
    #         send_mail(subject, nachricht,  from_email,  recipient_list, fail_silently=False, html_message=html)

    #         # return redirect('contact')
    # else:
    #      form = ContactForm()

    # return render(request, 'main/contact.html', {'title': 'Kontak', 'form': form})

    # vorname = models.CharField(max_length=100)
    # nachname = models.CharField(max_length=100)
    # email = models.EmailField()
    # unternehmen = models.CharField(max_length=100)
    # nachricht = models.TextField()
    if request.method == 'POST':
        contact = Contact()
        contact.vorname = request.POST.get('vorname')
        contact.nachname = request.POST.get('nachname')
        contact.email = request.POST.get('email')
        contact.unternehmen = request.POST.get('unternehmen')
        contact.nachricht = request.POST.get('nachricht')
        contact.save()
        return HttpResponse("<h1>Thanks for contact us!</h1>")


    return render(request, 'main/contact_new.html', {'title': 'Kontak'})

def impressum(request):
    return render(request, 'main/impressum.html', {'title': 'impressum'})

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
