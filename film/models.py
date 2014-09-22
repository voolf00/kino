# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
import datetime
import random
#from django.conf import settings
# from PIL import Image
# from imagekit.models.fields import ImageSpecField
#import imagekit.processors

# Create your models here.

class Jenre (models.Model):
    class Meta():
       # db_table = "jenre"
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    jenre_name =     models.CharField(max_length=256, verbose_name="название жанра транслитом")
    jenre_title = models.CharField(max_length=256, verbose_name="Название жанра")

    def __unicode__(self):
        return self.jenre_title #возвращает в место полученого объекта заголовог из базы


class Status (models.Model):
    status_film_name = models.CharField(verbose_name='состояние фильма', max_length=30)
    class Meta():
        verbose_name = 'Статусы'
        verbose_name_plural = 'Статус'
    def __unicode__(self):
        return self.status_film_name

class Film (models.Model):
    class Meta():
        db_table = "film"
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

    film_name = models.CharField(max_length=300) #*
    film_english_name = models.CharField(max_length=300, default="")
    film_jenres = models.ManyToManyField(Jenre, related_name="film", verbose_name=u"Жанр") #*
    film_text = models.TextField() #*
    film_year = models.IntegerField(default=datetime.datetime.today().year)
    film_date_public = models.DateTimeField(auto_now=False, auto_now_add=True)
    film_user = models.ForeignKey(User, related_name="film", verbose_name="Пользвоатель")
    film_award = models.TextField(default="-", blank=True)
    film_like = models.IntegerField(default=0, blank=True, null=True, verbose_name="лайки")
    film_sided_site = models.IntegerField(default=0)# или 0 или 1 или 2 отсутсвует, youtube,vimeo
    film_sided_id = models.CharField(max_length=200)
    film_country = models.CharField(max_length=200, default="-") #*
    film_status = models.ForeignKey(Status, default=2)
    film_money_create = models.IntegerField(default=0, blank=True)
    film_is_moderator = models.BooleanField(default=False, blank=True)
    film_image = models.ImageField(upload_to="film_photo", default="/media/filmImg/default.jpg", blank=True)

    def __unicode__(self):
        return self.film_name


class AboutCreatedUser (models.Model):
    class Meta():
        db_table = "about_created_user"
        verbose_name = "Создатель"
        verbose_name_plural = "Создатели"
    film_id = models.ForeignKey(Film)
    film_rejisser = models.CharField(max_length=256, default="-", blank=True)
    film_scenarii = models.CharField(max_length=256, default="-", blank=True)
    film_produsser = models.CharField(max_length=256, default="-", blank=True)
    film_operatior = models.CharField(max_length=256, default="-", blank=True)
    film_compozitor = models.CharField(max_length=256, default="-", blank=True)
    film_montaj = models.CharField(max_length=256, default="-", blank=True)
    film_actors = models.TextField(default="-", blank=True)

    def __unicode__(self):
        return self.film_id




class Film_comment (models.Model):
    class Meta():
        db_table = "film_comment"
    film_comment_date = models.DateTimeField()
    film_comment_text = models.TextField(verbose_name="написать комментарий")
    film_comment_link = models.ForeignKey(Film)
    film_comment_user = models.ForeignKey(User)


