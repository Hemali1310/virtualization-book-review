from django.shortcuts import render


# Create your views here.
def home_page(request):
    data = {}
    data["title"] = "Test Page"
    return render(request, "home.html", data)


def login_page(request):
    return render(request, "login_page.html")


def signup_page(request):
    return render(request, "signup_page.html")


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