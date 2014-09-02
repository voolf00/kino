from django.contrib import admin
from article.models import Article, Comments
# Полностью отвечает за админкту, то, как оно будет выглядеть
class ArticleInlile(admin.StackedInline):
    model = Comments
    extra = 2

class ArticleAdmin (admin.ModelAdmin): # редактирование алминки указываем, что будет видно
    fields = ['article_title', 'article_text', 'article_date']
    inlines = [ArticleInlile]

admin.site.register(Article, ArticleAdmin) # регестрируем в админку новый элемент и настройки. т.е. классы
