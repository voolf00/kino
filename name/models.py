from django.db import models
from film.models import Film
from django.contrib.auth.models import User


class Profession (models.Model):
    class Meta():
        db_table = "profession"
        verbose_name = "Профессия"
        verbose_name_plural = "Профессии"
    proffesion_name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.proffesion_name


class Name (models.Model):
    class Meta():
        db_table = 'name'
        verbose_name = "Имя"
        verbose_name_plural = "Имена"

    name_first = models.CharField(max_length=256, default="", blank=True)
    name_last = models.CharField(max_length=256, default="", blank=True)
    profession = models.ManyToManyField(Profession,default="", blank=True, related_name='profession', verbose_name=u'Специальность')
    name_sex = models.IntegerField(max_length=1, blank=True, default=0)
    name_birthday = models.DateField(blank=True, null=True)
    name_mobile = models.IntegerField(max_length=30, blank=True, null=True)
    name_website = models.CharField(max_length=256, blank=True, null=True, default="")
    name_works_id = models.ManyToManyField(Film, related_name='film', verbose_name=u'Имя')
    name_add_user_id = models.ForeignKey(User, related_name="User", verbose_name=u'Добавил')
    name_user_id = models.ForeignKey(User, related_name='user', verbose_name=u'Пренадлежит', null=True, blank=True)

    #name_city
    def __unicode__(self):
        return self.name_first



