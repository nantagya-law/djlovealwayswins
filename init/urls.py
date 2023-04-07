
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from donateapp.views import (
#     CreateChechoutSessionView,
#     DonatePageView,
#     DonateLandingPageView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('donateapp.urls')),
    # path('donate', DonatePageView.as_view(), name='donate-page'),
    # path('landingpage', DonateLandingPageView.as_view(), name='landing-page'),
    # path('create-checkout-session/', CreateChechoutSessionView.as_view(), name='create-checkout-session'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
