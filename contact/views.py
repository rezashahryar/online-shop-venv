from django.shortcuts import render
from .models import Contact
from django.contrib import messages
from .forms import ContactForm


# Create your views here.

def contact(request):
    contact_form = ContactForm
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, "با موفقیت ارسال شد")
    else:
        contact_form = ContactForm()

    context = {
        "form": contact_form,
    }
    return render(request, "contact/contact.html", context)
