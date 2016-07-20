from django.db import models

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

    def __str__(self):
        return self.title