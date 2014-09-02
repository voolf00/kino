from django.http.response import HttpResponse, Http404
from django.template.loader import get_template #получение шаблона
from django.template import Context # отвечает за переменные
from django.shortcuts import render_to_response, redirect
from article.models import Article, Comments
from django.core.exceptions import ObjectDoesNotExist
from article.forms import CommentForm, ArticleForm
from  django.core.context_processors import csrf
from django.core.paginator import Paginator
from  django.contrib import auth
import datetime
import time


# Create your views here.

def template_three(request):
    view  = "tempmate_three"
    return render_to_response('article.html',{"name":view})

# все новости
# работа с базой
# пагинаторы
def freeDateArticles (col):
    all_articles = Article.objects.all()
    current_page = all_articles.order_by("-article_date")[0:col]
    return current_page

def articles (request, page_number = 1):
    all_articles = Article.objects.all()
    current_page = Paginator(all_articles, 4)
    args = {}
    args.update(csrf(request))
    args['articleForm'] = ArticleForm
    args['title'] = 'article'
    args['articles'] = current_page.page(page_number)
    args['username'] = auth.get_user(request).username
    args['is_superUser'] = auth.get_user(request).is_superuser

    return render_to_response('articles.html', args)

# читать новость
# работа с базой и с формой коментариев
def article (request, article_id, comments_page_number=1):
    comment_form = CommentForm
    arqs = {}
    arqs.update(csrf(request))
    arqs['article'] = Article.objects.get(id = article_id)
    arqs['title'] = 'article'
    all_comments = Comments.objects.filter(comments_article_id = article_id)
    current_page_comments = Paginator(all_comments, 4)
    arqs['comments'] = current_page_comments.page(comments_page_number)
    arqs['comment_form'] = comment_form
    arqs['username'] = auth.get_user(request).username
    arqs['is_superUser'] = auth.get_user(request).is_superuser
    return render_to_response('article.html', arqs)

def editArticle(request, article_id):
    arqs = {}
    arqs.update(csrf(request))
    arqs['username'] = auth.get_user(request).username
    arqs['title'] = 'article'
    arqs['article_id'] = article_id
    arqs['is_superUser'] = auth.get_user(request).is_superuser
    if auth.get_user(request).is_superuser == 1:
        if request.POST:
            form = ArticleForm(request.POST)
            if form.is_valid():
                article_edit = form.save( commit=False)
                #article_edit.article_title = Article.objects.get(id = article_id).article_title
                #article_edit.article_text = Article.objects.get(id = article_id).article_text
                article_edit.id = Article.objects.get(id = article_id).id
                article_edit.article_user_id = auth.get_user(request).id
                article_edit.article_date = datetime.datetime.today()
                form.save()
                return redirect('/articles/get/'+str(article_edit.id))
            else:
                arqs['error'] = "huina"
                #return redirect('/',arqs)
        else:
            article_form = ArticleForm
            arqs['form'] = article_form
            arqs['article_title'] = Article.objects.get(id = article_id).article_title
            arqs['article_text'] = Article.objects.get(id = article_id).article_text
            return render_to_response('editArticle.html', arqs)
    else:
        arqs['error'] = 'addArticle'
    return render_to_response('error.html',arqs)

def addArticle (request):
    arqs = {}
    arqs.update(csrf(request))
    arqs['title'] = 'article'
    arqs['username'] = auth.get_user(request).username
    arqs['is_superUser'] = auth.get_user(request).is_superuser
    if auth.get_user(request).is_superuser == 1:
        if request.POST:
            form = ArticleForm(request.POST) #в скобка пишется при загрузке файлов request.FILES
            if form.is_valid():
                article_add = form.save(commit=False)
                # article_add.article_title = Article.objects.get(request).article_title
                #article_add.article_text = Article.objects.get(request).article_text
                article_add.article_user_id = auth.get_user(request).id
                article_add.article_date = datetime.datetime.today()
                form.save()
                return redirect('/articles/get/'+str(article_add.id))
            else:
                arqs['error'] = "huina"
                # return redirect('/',arqs)
        else:
            article_form = ArticleForm
            arqs['form'] = article_form
            return render_to_response('addArticle.html', arqs)
    else:
        arqs['error'] = 'addArticle'
    return render_to_response('error.html',arqs)


# доббовление коментариев
# куки и сессии
def addComment (request, article_id):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)# запрещаем сохранять сейчас
            comment.comments_article = Article.objects.get(id = article_id)
            comment.comments_user_id = auth.get_user(request).id
            comment.comments_date = datetime.datetime.today()
            form.save()
            #request.session.set_expiry(1)
            #request.session['pouse'] = True
    return redirect('/articles/get/%s' % article_id)

# добавить лайк
#куки и ссесии
def like (request, article_id):
    try:
        if article_id in request.COOKIES:
            redirect('/')
        else:
            article = Article.objects.get(id=article_id)
            article.article_likes += 1
            article.save()
            response = redirect("/") # становиться объектом класса
            response.set_cookie(article_id, "test") # используем объект для своих нужд
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')

def delArticle(request, article_id):
    if auth.get_user(request).is_superuser:

        delete_article = Article.objects.get(id = article_id)
        delete_comments_article = Comments.objects.filter(comments_article_id = article_id)
        delete_article.delete()
        delete_comments_article.delete()
        return redirect('/')
    else:
        return render_to_response('error.html', {'error':'delete_article'})