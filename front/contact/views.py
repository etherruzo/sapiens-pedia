from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            name = form.cleaned_data['name']
            try:
                send_mail(subject, message, email, ['elena.tomas@sapiens-pedia.org'], name)
            except BadHeaderError:
                return HttpResponse('Invalid header found. ')
            return redirect('contact:email_success')

    context = {'form': form}
    template = 'contact/contact.html'
    return render(request, template, context)


def email_success(request):
    context = {}
    template = 'contact/email_success.html'
    return render(request, template, context)
