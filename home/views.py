from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

from .forms import DetailsForm
from .tasks import send_email


def home(request):
    return render(request, "home/home.html", {"title": "Home"})


def about(request):
    return render(request, "home/about.html")


def contact(request):
    if request.method == "POST":
        form = DetailsForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data.get("description")
            sender = form.cleaned_data.get("email")
            subject = f"Inquire at pixenweb from {sender}."
            form.save()
            send_mail(subject, message, sender, ["infopixenweb@gmail.com"])
            # send_email.delay(sender,message)
            messages.success(
                request,
                "Thank you for contacting pixenweb.We will get back to you shortly via email.",
            )
            return redirect("home")
        else:
            return redirect("contact")
    else:
        form = DetailsForm()
        context = {"title": "contact", "form": form}
    return render(request, "home/contact.html", context)


def pricing(request):
    return render(request, "home/pricing.html", {"title": "pricing"})

