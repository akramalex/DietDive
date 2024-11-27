from django.urls import path
from . import views


""" Maps the root URL ('') to the contact_view function in views.py
     which displays and handles the contact form
     Maps the '/success/' URL to the contact_success function in views.py
     which renders a success page after the form is successfully submitted"""


urlpatterns = [
    path('', views.contact_view, name='contact'),
    path('success/', views.contact_success, name='contact_success'),
]
