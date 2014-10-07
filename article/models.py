# -*- coding: utf-8 -*-
from django.db import models
from  django.contrib.auth.models import User
# перед тем, как создать базц данных, нужно
# нужно описать переменные, например название фильма, текст, афторы и т.л.as
# описать их тип, int, char
# в конструкторе Meta написать название таблицы
# manage.py syncdb СОЗДАНИЕ БАЗЫ ДАННЫХ
# после этого переходим в views
import random, datetime
#from pytils import translit





class Article(models.Model):
    class Meta():
        db_table = "article"


    def randomName(self, filename):
        name1 = random.randint(1,10000)
        name2 = random.randint(1,10000)
        #newName ='' + str(datetime.datetime.today()) + filename
        newName = ''.join(["article_img/", str(name1) , "_", str(name2) , "_", str(datetime.date.today()), ".jpg"])
        return newName

    article_title = models.CharField(max_length=200)  # название статьи
    article_text = models.TextField()
    article_likes = models.IntegerField(default=0)
    article_date = models.DateTimeField()
    article_user = models.ForeignKey(User)
    article_img = models.ImageField(null=True, blank=True, default='default.jpg', upload_to=randomName)

    def _get_image_url(self):
        return self.article_img


class Comments(models.Model):
    class Meta():
        db_table = "comments"

    comments_date = models.DateTimeField()
    comments_text = models.TextField(verbose_name="написать комментарий")
    comments_article = models.ForeignKey(Article)
    comments_user = models.ForeignKey(User)
