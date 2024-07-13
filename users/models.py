from django.db import models
from book.models import Book
from django.contrib.auth.models import User

class UserBooks(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class BasketBooks(models.Model):
    book = models.ForeignKey(Book, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)



    def set_total_price(instance, obj):
        obj.total_price = obj.book.price * obj.count