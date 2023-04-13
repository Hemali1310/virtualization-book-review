from django.shortcuts import render, redirect
from django.contrib import messages
from application.models import Category, Books, Author, Publisher, AuthorBooks, BooksPublisher, User, Review

# Create your views here.
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

        user = User.objects.filter(username=username, password=password)

        if len(user)!=0:
            user = user.get()
            return redirect('/browse/'+str(user.user_id)+'/')
        else:
            messages.info(request, 'Invalid email or Password')
            return redirect('/login/')

    return render(request, "login_page.html")

def browse_page(request, user_id):
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
    return render(request, "browse.html", {"books": book_list, "user_id": user_id})

def book_review_page(request, user_id, id):

    user = User.objects.get(user_id=user_id)
    book = Books.objects.get(book_id=id)

    if request.method == 'POST':
           user_review = request.POST["user_review"]
           total_reviews = Review.objects.count()

           user_review = Review.objects.create(review_id=total_reviews+1, user=user, book=book, reviews=user_review, upvotes=0, downvotes=0)
           user_review.save()

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

    # Geeting Review on book
    reviews = []
    for review in Review.objects.filter(book=book):
        reviews.append({
            "user_id": review.user.user_id,
            "review_id": review.pk,
            "user_image": "https://w7.pngwing.com/pngs/933/97/png-transparent-computer-icons-avatar-heroes-public-relations-necktie-thumbnail.png",
            "user_name": review.user.first_name + " " + review.user.last_name,
            "user_review": review.reviews,
            "upvote": review.upvotes,
            "downvote": review.downvotes,
            "comments": 0
        })

    return render(request, "book_review_page.html", {
        "user_id": user_id,
        "book": book,
        "rating": 4, 
        "authors": authors, 
        "publishers": publishers,
        "reviews": reviews
    })

def delete_review(request, user_id, id, review_id):
    Review.objects.filter(pk=review_id).delete()
    return redirect("/book_review/"+str(user_id)+"/"+str(id)+"/")

def user_profile(request, user_id):
    user = User.objects.filter(pk=user_id).get()
    return render(request, "user_profile.html", {"user": user})


def edit_profile(request, user_id):

    user = User.objects.get(pk=user_id)

    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        
        if username=='' or first_name=='' or last_name=='' or email=='' or password=='':
            messages.info(request, "Please Enter All the values!")
            return redirect('/edit_profile/'+user_id+'/')
        
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.password = password
        user.save()
        messages.success(request, "Profile Successfully Updated!")

    return render(request, "edit_profile.html", {"user": user})

def author_profile(request):
    return render(request, "author_profile.html")


def subscription(request):
    return render(request, "subscription.html")

def payment_page(request):
    return render(request, "payment_page.html")