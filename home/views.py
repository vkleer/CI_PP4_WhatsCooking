import os
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import BadHeaderError, send_mail


def HomePage(request):
    return render(request, 'index.html')


def UserProfile(request, pk):
    user = User.objects.get(username=pk)

    if request.user == user:
        return render(request, 'profile.html', {
            'user': user
        })

    else:
        messages.error(
            request,
            'You can only access your own profile.'
        )
        return redirect('home')


def DeleteUser(request, pk):
    user = User.objects.get(username=pk)

    if request.method == 'POST':
        user.delete()
        messages.info(
            request,
            'Your account has been deleted. Feel free to come back any time!'
        )
        return redirect('home')


def Contact(request):
    if request.method == 'POST':
        contact_message = request.POST['contact-message']

        if request.user.is_authenticated:
            contact_name = request.user.username
            contact_email = request.user.email

            if request.user.email:
                contact_email = request.user.email
            else:
                contact_email = request.POST['contact-email']
        else:
            contact_name = request.POST['contact-name']
            contact_email = request.POST['contact-email']

        if contact_name and contact_message and contact_email:
            try:
                send_mail(
                    "What's Cooking - Message from " + contact_name +
                    ' (' + contact_email + ')',
                    contact_message,
                    contact_email,
                    [os.environ.get('EMAIL_HOST_USER')],
                )
            except BadHeaderError:
                messages.error(
                    request,
                    'Invalid header found.'
                )
        messages.success(
            request,
            'Your contact form has been submitted - thank you ' +
            contact_name + '!'
        )
        return render(request, 'contact.html', {
            'contact_name': contact_name
        })
    else:
        return render(request, 'contact.html')
