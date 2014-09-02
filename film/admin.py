from django.contrib import admin
from film.models import Film, Film_comment, Jenre, Status
# Полностью отвечает за админкту, то, как оно будет выглядеть
class FilmInlile(admin.StackedInline):
    model = Film_comment
    extra = 2

class FilmAdmin (admin.ModelAdmin): # редактирование алминки указываем, что будет видно
    #fields = ['film', 'article_text', 'article_date']
    inlines = [FilmInlile]

admin.site.register(Film, FilmAdmin) # регестрируем в админку новый элемент и настройки. т.е. классы

admin.site.register(Jenre)
admin.site.register(Status)