from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#书名 封面图 评分 作者 出版社 译者 出版年 页数 定价 装帧 ISBN 标签 简介 目录 id
class book(models.Model):
    title = models.CharField(max_length = 100)
    cover_url = models.URLField()
    score = models.FloatField()
    author = models.CharField(max_length = 100)
    publisher = models.CharField(max_length = 100, blank = True)
    translator = models.CharField(max_length = 100, blank = True)
    publisher_date = models.CharField(max_length = 30, blank = True)
    page = models.CharField(max_length = 30, blank = True)
    price = models.CharField(max_length = 30, blank = True)
    binding = models.CharField(max_length = 30, blank = True)
    Isbn = models.CharField(max_length = 100, blank = True)
    label = models.CharField(max_length = 100, blank = True)
    content_intro = models.CharField(max_length = 1000, blank = True)
    directory = models.CharField(max_length = 1000, blank = True)
    book_id = models.IntegerField()
    score_star = models.CharField(max_length=100, default='')


    def __str__(self):
        return self.title

class laber(models.Model):
    title = models.CharField(max_length = 30)
    def __str__(self):
        return self.title

class note(models.Model):
    time = models.CharField(max_length = 50, default="")
    author = models.CharField(max_length = 30)
    book_title = models.CharField(max_length = 100)
    content = models.CharField(max_length = 1000, blank=False)
    page = models.IntegerField()
    chapter = models.CharField(max_length = 100, blank=False)

    def __str__(self):
        return self.author

class comment_reply(models.Model):
    author = models.CharField(max_length=30)
    content = models.CharField(max_length=250)
    time = models.CharField(max_length=50)
    comment_id = models.CharField(max_length=100, default="")
    def __str__(self):
        return self.author

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    address = models.CharField(max_length = 100, blank=True)
    def __str__(self):
        return self.user.username

class Comment(models.Model):
    comment_user = models.CharField(max_length = 30)
    comment_book = models.CharField(max_length = 30)
    comment_title = models.CharField(max_length = 30)
    comment_rate = models.CharField(max_length = 30)
    comment_content = models.CharField(max_length = 300)
    comment_id = models.CharField(max_length=100, default="")
    comment_time = models.CharField(max_length = 100, blank=True)
    def __str__(self):
        return self.comment_user
