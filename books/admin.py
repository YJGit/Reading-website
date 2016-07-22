from django.contrib import admin
from .models import book, laber, UserProfile

# Register your models here.
admin.site.register(book)
admin.site.register(laber)
admin.site.register(UserProfile)