from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

""" Create your views here.
 views.py handles the logic
 for rendering and processing the contact form.
 It includes functionality for submitting contact requests
and rendering success or error messages."""


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
        else:
            # If form is invalid, send an error message
            messages.error(
                request, "There was an error. Please try again.")
            return render(
                request, 'contact/contact.html', {'form': form})
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})

# Add the contact_success view


def contact_success(request):
    return render(request, 'contact/success.html')
