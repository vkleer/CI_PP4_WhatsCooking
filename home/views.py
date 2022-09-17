from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User


def HomePage(request):
    return render(request, 'index.html')


def UserProfile(request, pk):
    user = User.objects.get(username=pk)

    if request.user == user:
        return render(request, 'profile.html', {
            'user': user
        })

    else:
        messages.error(request,
                       "You can only access your own profile.")
        return redirect('home')
