from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    profile_user = models.ForeignKey(User, related_name='profile')
    profile_avatar = models.ImageField(upload_to='avatars', blank=True)
    class Meta():
        db_table = 'Profile'
        verbose_name = 'Профили'
        verbose_name_plural = 'профиль'
    def __unicode__(self):
        return self.profile_user.get_full_name() #возвращает в место полученого объекта заголовог из базы
