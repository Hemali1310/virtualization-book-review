"""book_review_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from application.views import home_page, login_page, signup_page, browse_page, book_review_page, user_profile, author_profile, subscription, payment_page, edit_profile, delete_review

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('login/', login_page),
    path('signup/', signup_page),
    path('browse/<int:user_id>/', browse_page),
    path('book_review/<int:user_id>/<int:id>/', book_review_page),
    path('book_review/<int:user_id>/<int:id>/delete_review/<int:review_id>', delete_review),
    path('user_profile/<int:user_id>/', user_profile),
    path('author_profile/<int:author_id>/', author_profile),
    path('subscription/', subscription),
    path('payment/', payment_page),
    path('edit_profile/<int:user_id>/', edit_profile),
    path('<path:unknown_path>', TemplateView.as_view(template_name='Error404.html')) 
]
