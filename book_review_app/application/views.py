from django.shortcuts import render, redirect
from .models import User, Offer
from django.contrib.auth import authenticate, login
from django.contrib import messages, auth


def home_page(request):
    return render(request, "home.html")


def signup_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        print(username)

        if password != '':

            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists!")
                return redirect('/signup/')

            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists!")
                return redirect('/signup/')

            else:
                user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password, subscription_id=0, fellow_reviewers=0, username=username)
                user.save()
                return redirect('/login/')

    return render(request, "signup_page.html")


def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.filter(username=username, password=password).get()
        print(user)

        if user is not None:
            return redirect('/browse/')
        
        else:
            messages.info(request, 'Invalid email or Password')
            return redirect('/login/')

    return render(request, "login_page.html")


def browse_page(request):
    return render(request, "browse.html")


def book_review_page(request):
    return render(request, "book_review_page.html")


def user_profile(request):
    return render(request, "user_profile.html")


def author_profile(request):
    return render(request, "author_profile.html")


def subscription(request):
    return render(request, "subscription.html")


def payment_page(request):
    return render(request, "payment_page.html")