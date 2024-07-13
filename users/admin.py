from django.contrib import admin
from .models import UserBooks, BasketBooks
from book.admin import Book
from django.contrib.auth.admin import UserAdmin


admin.site.register([UserBooks, BasketBooks])

#@admin.register(UserBooks)
#class UserBooksAdmin(admin.ModelAdmin):
#    list_display = ('id', 'book', 'user')


#@admin.register(BasketBooks)
#class BasketBooksAdmin(admin.ModelAdmin):
#    list_display = ('id', 'user', 'book')




