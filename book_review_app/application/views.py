from django.shortcuts import render

from application.models import Category, Books, Author, Publisher, AuthorBooks, BooksPublisher

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
    book_list = {}
    for category in Category.objects.all():
        books = Books.objects.filter(category=category.category_id)
        book_list[category.category_name] = list()
        if len(books) != 0:
            for book in books:
                book_list[category.category_name].append({
                    "id": book.book_id,
                    "title": book.book_title,
                    "description": book.book_description,
                    "image": book.cover_image_url,
                })
    return render(request, "browse.html", {"books": book_list})


def book_review_page(request, id):
    book = Books.objects.filter(pk=id).get()

    # Getting Authors
    authors = []
    for authbook in AuthorBooks.objects.filter(books_book=id):
        author = Author.objects.get(pk = authbook.author_author.author_id)
        authors.append("\""+author.first_name+" "+author.last_name+"\"")
    if len(authors)==0:
        authors = ["None"]

    # Getting Publishers
    publishers = []
    for bookPub in BooksPublisher.objects.filter(books_book=id):
        publisher = Publisher.objects.get(pk = bookPub.books_book.book_id)
        publishers.append("\""+publisher.publisher_name+"\" ("+publisher.email+") ")
    if len(publishers)==0:
        publishers = ["None"]

    return render(request, "book_review_page.html", {
        "book": book,
        "rating": 4, 
        "authors": authors, 
        "publishers": publishers
    })


def user_profile(request):
    return render(request, "user_profile.html")


def author_profile(request):
    return render(request, "author_profile.html")


def subscription(request):
    return render(request, "subscription.html")


def payment_page(request):
    return render(request, "payment_page.html")