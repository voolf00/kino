from django.shortcuts import render_to_response, redirect
from django.http.response import Http404
from film.models import Film, Film_comment, AboutCreatedUser
from django.core.exceptions import ObjectDoesNotExist
# from film.forms import
from article.forms import ArticleForm
from django.core.context_processors import csrf
from django.contrib import auth
from django.core.paginator import Paginator
from film.forms import FilmForm, Film_comment_Form, Film_About_created_Users_Form
import datetime, article.views

# Create your views here.

def indexFilm(request):
    args = {}
    args.update(csrf(request))
    args['articles'] = article.views.freeDateArticles(3)

    all_films = Film.objects.all()
    args['username'] = auth.get_user(request).username
    args['top_likes'] = all_films.order_by('-film_like')[0:9]  # order_by сартировка о определенному индексу
    args['add_films'] = all_films.order_by('-film_date_public')[0:2]
    args['title'] = 'film'
    args['articleForm'] = ArticleForm
    return render_to_response('index.html', args)


def films(request, page_number=1):
    all_films = Film.objects.all()
    current_page_films = Paginator(all_films.order_by("-film_date_public"), 4)
    args = {}
    args['title'] = 'film'


    args['films'] = current_page_films.page(page_number)
    args['username'] = auth.get_user(request).username
    args['is_Superuser'] = auth.get_user(request).is_superuser
    return render_to_response("films.html", args)


def film(request, film_id):
    args = {}
    args['title'] = 'film'
    args['film'] = Film.objects.get(id=film_id)
    args['username'] = auth.get_user(request).username
    if auth.get_user(request).id == Film.objects.get(id=film_id).film_user or auth.get_user(request).is_superuser:
        args['private'] = 'true'
    args['add_users'] = AboutCreatedUser.objects.filter(film_id=film_id).exists()
    return render_to_response("film.html", args)


def addFilmUsers(request, film_id):
    args = {}
    args.update(csrf(request))
    args['title'] = 'film'
    args['username'] = auth.get_user(request).username
    args['film_id'] = film_id
    args['film_name'] = Film.objects.get(id=film_id).film_name
    if auth.get_user(request).id == Film.objects.get(id=film_id).film_user or auth.get_user(request).is_superuser:
        if request.POST:
            form = Film_About_created_Users_Form(request.POST)
            if form.is_valid():
                form_users_add = form.save(commit=False)
                form_users_add.film_id_id = Film.objects.get(id=film_id).id
                form.save()
                return redirect('film/get/'+str(film_id) +'/users')
            else:
                args['error'] = 'huina'
                return render_to_response('error.html', args)
        else:
            form = Film_About_created_Users_Form
            args['film_created_users_form'] = form
            return render_to_response('addUsers.html', args)
    else:
        args['error'] ='admin_And_user'
        return render_to_response('error.html', args)

def editFilmUsers(request, film_id):

    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    args['film_id'] = film_id
    args['title'] = 'film'

    if auth.get_user(request).id == Film.objects.get(id=film_id).film_user or auth.get_user(request).is_superuser:
        if request.POST:
            form = Film_About_created_Users_Form(request.POST)
            if form.is_valid():
                edit_form = form.save(commit=False)
                edit_form.id = AboutCreatedUser.objects.get(film_id=film_id).id
                edit_form.film_id_id = Film.objects.get(id=film_id).id

                form.save()
                return redirect('/film/get/'+film_id+'/users')
            else:
                args['error'] = 'huina'
                return render_to_response('error.html', args)
        else:

            form = Film_About_created_Users_Form
            args['film_created_users_form'] = form
            args['film_users'] = AboutCreatedUser.objects.get(film_id = film_id)
            return render_to_response('editUsers.html', args)
    else:
        args['error'] = 'not prava redactiorvania'
        return render_to_response('error.html', args)




def filmUsers(request, film_id):
    args = {}
    args['title'] = 'film'
    args['username'] = auth.get_user(request).username


    if AboutCreatedUser.objects.filter(film_id = film_id).exists()== False:
        return addFilmUsers(request, film_id)
    else:
        args['film'] = Film.objects.get(id=film_id)
        args['film_users'] = AboutCreatedUser.objects.get(film_id=film_id)

    return render_to_response("filmUsers.html", args)


def filmDel(request, film_id):
    if auth.get_user(request).is_superuser or auth.get_user(request).id == Film.objects.get(id=film_id).film_user_id:
        delFilmID = Film.objects.get(id=film_id)
        delCommentFilmID = Film_comment.objects.filter(film_comment_link_id=film_id)
        if AboutCreatedUser.objects.filter(film_id=film_id).exists():

            delAboutFilmUsers = AboutCreatedUser.objects.get(film_id=film_id)
            delAboutFilmUsers.delete()
        delFilmID.delete()
        delCommentFilmID.delete()
        return redirect('/', {'deleted': "delete successfully"})
    else:
        return render_to_response('error.html', {'error': 'deleteFilm'})

def filmUsersDel(request, film_id):
     if auth.get_user(request).is_superuser or auth.get_user(request).id == Film.objects.get(id=film_id).film_user_id:
        delAboutFilmUsers = AboutCreatedUser.objects.get(film_id=film_id)
        delAboutFilmUsers.delete()
        return redirect('/film/get/'+str(film_id))


def filmAdd(request):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    args['title'] = 'film'
    args['userTrue'] = auth.get_user(request).is_anonymous()

    if auth.get_user(request).is_anonymous() == False:
        if request.POST:
            form = FilmForm(request.POST)

            if form.is_valid():

                film_add = form.save(commit=False)
                film_add.film_date_public = datetime.datetime.today()
                film_add.film_user_id = auth.get_user(request).id

                youtube = request.POST.get('film_sided_id').find('youtube.com/')
                vimeo = request.POST.get('film_sided_id').find('vimeo.com/')
                if youtube == -1 and vimeo == -1:
                    youtube = request.POST.get('film_sided_id').find('youtu.be/')
                if youtube != -1:
                    film_add.film_sided_site = 2
                    home = request.POST.get('film_sided_id').find('=')
                    end1 = request.POST.get('film_sided_id').find('&')
                    end2 = request.POST.get('film_sidet_id').finde('#')
                    if end1 != -1:
                        youtube = request.POST.get('film_sided_id')[home + 1:end1]
                        film_add.film_sided_id = youtube
                    if end1 == -1 and end2 == -1:
                        ##t=222
                        youtube = request.POST.get('film_sided_id')[home + 1:]
                        film_add.film_sided_id = youtube
                    if end2 != -1:
                        youtube = request.POST.get('film_sided_id')[home + 1:end2]
                        film_add.film_sided_id = youtube


                if vimeo != -1:
                    film_add.film_sided_site = 3
                    home = request.POST.get('film_sided_id').find('.com/')
                    vimeo = request.POST.get('film_sided_id')[home + 5:]
                    film_add.film_sided_id = vimeo
                if vimeo == -1 and youtube == -1:
                    return render_to_response('error.html', {'error': "Cсылка не верна"})

                film_add.save()
                form.save_m2m()
                return redirect('/film/')
            else:
                args['error'] = "huina"
                args['username'] = 'huina'
                return render_to_response('error.html', args)
        else:
            film_form = FilmForm
            args['film_form'] = film_form
            return render_to_response('addFilm.html', args)

    args['error'] = 'add_User_none'
    return render_to_response('error.html', args)


def editFilm(request, film_id):
    args = {}
    args.update(csrf(request))
    args['title'] = 'film'
    args['username'] = auth.get_user(request).username
    if auth.get_user(request).id == Film.objects.get(id=film_id).film_user or auth.get_user(request).is_superuser:

        if request.POST:
            form = FilmForm(request.POST)
            if form.is_valid():

                film_add = form.save(commit=False)
                film_add.id = Film.objects.get(id = film_id).id
                film_add.film_date_public = datetime.datetime.today()
                film_add.film_user_id = auth.get_user(request).id

                youtube = request.POST.get('film_sided_id').find('youtube.com/')
                vimeo = request.POST.get('film_sided_id').find('vimeo.com/')
                if youtube == -1 and vimeo == -1:
                    youtube = request.POST.get('film_sided_id').find('youtu.be/')
                if youtube != -1:
                    film_add.film_sided_site = 2
                    home = request.POST.get('film_sided_id').find('=')
                    end1 = request.POST.get('film_sided_id').find('&')
                    end2 = request.POST.get('film_sided_id').find('#')
                    if end1 != -1:
                        youtube = request.POST.get('film_sided_id')[home + 1:end1]
                        film_add.film_sided_id = youtube
                    if end1 == -1:
                        youtube = request.POST.get('film_sided_id')[home + 1:]
                        film_add.film_sided_id = youtube
                    if end2 != -1:
                        youtube = request.POST.get('film_sided_id')[home + 1:end2]
                        film_add.film_sided_id = youtube

                if vimeo != -1:
                    film_add.film_sided_site = 3
                    home = request.POST.get('film_sided_id').find('.com/')
                    vimeo = request.POST.get('film_sided_id')[home + 5:]
                    film_add.film_sided_id = vimeo
                if vimeo == -1 and youtube == -1:
                    return render_to_response('error.html', {'error': "Cсылка не верна"})

                film_add.save()
                form.save_m2m()
                return redirect('/film/')
            else:
                args['error'] = "huina"
                args['username'] = 'huina'
                return render_to_response('error.html', args)
        else:
            args['film'] = Film.objects.get(id=film_id)
            return render_to_response("editFilm.html", args)