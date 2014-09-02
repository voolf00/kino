# -*- coding: utf-8 -*-
from django.db import models
from  django.contrib.auth.models import User
# перед тем, как создать базц данных, нужно
# нужно описать переменные, например название фильма, текст, афторы и т.л.as
# описать их тип, int, char
# в конструкторе Meta написать название таблицы
# manage.py syncdb СОЗДАНИЕ БАЗЫ ДАННЫХ
# после этого переходим в views
class Article(models.Model):
    class Meta():
        db_table = "article"
    article_title= models.CharField(max_length=200) #название статьи
    article_text = models.TextField()
    article_likes = models.IntegerField(default=0)
    article_date = models.DateTimeField()
    article_user = models.ForeignKey(User)

class Comments (models.Model):
    class Meta():
        db_table = "comments"
    comments_date = models.DateTimeField()
    comments_text = models.TextField(verbose_name="написать комментарий")
    comments_article = models.ForeignKey(Article)
    comments_user = models.ForeignKey(User)
