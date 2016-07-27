from django.contrib import admin
from .models import book, laber, note ,UserProfile

# Register your models here.
admin.site.register(book)
admin.site.register(laber)
admin.site.register(note)
admin.site.register(UserProfile)