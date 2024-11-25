from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

# Create your views here.
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')  # Redirect to the success view
        else:
            # If form is invalid, send an error message
            messages.error(request, "The form is invalid. Please try again.")
            return render(request, 'contact/contact.html', {'form': form})  # Render the form again with error    
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})

# Add the contact_success view
def contact_success(request):
    return render(request, 'contact/success.html')