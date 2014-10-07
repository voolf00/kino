__author__ = 'Voolf'
from django.forms import ModelForm
from article.models import Comments, Article

class CommentForm(ModelForm):
    class Meta():
        model = Comments
        fields = ['comments_text']
        #итак, форма создаеттся в несколько этапов
        # из библиотеки джанго подгружется модел форм
        # далее ипортируется модели базы данных, чтобы связать форму с базой,
        # чтобы ничего не напутать
        # послкольку в в базу данных отправлаются 2 переменные:
        # текст коментария и номер к статье, то чтобы в форме
        # отображалась только форма с текстом нужно написать в Fields
        # то, что хотим показать. т.е. comments_text

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['article_title','article_text', 'article_img']