from django.urls import path
from users.views import login_view, register_view, logout_views, account_main_view, account_about_view, account_books_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_views, name='logout'),
    path('account/', account_main_view, name='account'),
    path('account/about/', account_about_view, name='account-about'),
    path('account/books/', account_books_view, name='account-books'),
]