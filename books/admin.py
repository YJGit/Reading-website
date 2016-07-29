from django.contrib import admin
from .models import book, laber, UserProfile, note, Comment, comment_reply

# Register your models here.
admin.site.register(book)
admin.site.register(laber)
admin.site.register(note)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(comment_reply)

