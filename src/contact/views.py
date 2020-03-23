from django.shortcuts import render, redirect
from .models import Contact
from django.http import HttpResponseRedirect

def contact(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        new_contact = Contact()
        new_contact.name = name
        new_contact.email = email
        new_contact.phone = phone
        new_contact.message = message
        new_contact.save()
        return HttpResponseRedirect('/contact/')
    return render(request, 'contact-us.html', {})
