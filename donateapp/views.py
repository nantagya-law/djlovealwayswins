# import stripe
# from django.conf import settings
# from django.views.generic import TemplateView
# from django.http import JsonResponse
# from django.views import View

# from django.urls import reverse
# from .models import Post

from django.shortcuts import render, redirect

from . models import Donate

# My donation page

def donation_page(request):

    donation = Donate.objects.get(id=1)

    context = {'donation': donation}

    return render(request, 'donateapp/donation-page.html', context=context)



# Payment success

def payment_success(request):
    
   return render(request, 'donateapp/payment-success.html')


# Payment failed

def payment_failed(request):
    
    return render(request, 'donateapp/payment-failed.html')










# stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.

# class DonateLandingPageView(TemplateView):
#     template_name = "donateapp/landing.html"

# class DonatePageView(TemplateView):
#     template_name = "donateapp/donate.html"

# class CreateChechoutSessionView(View):
#     def post(self, request, *args, **kwargs):
#        YOUR_DOMAIN = "http://127.0.0.1:8000"
#        checkout_session = stripe.checkout.Session.create(
#            payment_method_types = ['card'],
#             line_items=[
#                 {
#                     # 'price_data': {
#                     #     'currency': 'euro',
#                     #     'unit_amount': 5,
#                     #     'product_data': {
#                     #         'reason': 'Cybermobbing',
#                     #     },
#                     # },

#                     # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
#                     'price': '{{PRICE_ID}}',
#                     'quantity': 1,
#                 },
#             ],
#             mode='payment',
#             success_url=YOUR_DOMAIN + '/success/',
#             cancel_url=YOUR_DOMAIN + '/cancel/',
#            # automatic_tax={'enabled': True},
#         ) 
#        return JsonResponse({
#            'url': checkout_session.url
#            })

# def donate(request):
#     return render(request, 'main/donate.html', {'title': 'Spende'})