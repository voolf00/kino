from django.conf.urls import patterns, include, url




urlpatterns = patterns('',

    url(r'^addfilm', 'film.views.filmAdd'),

    url(r'page/(\d+)', 'film.views.films'),
    url(r'^get/(\d+)/users/edit', 'film.views.editFilmUsers'),
    url(r'^get/(\d+)/users/delete', 'film.views.filmUsersDel'),
    url(r'^get/(\d+)/users/add', 'film.views.addFilmUsers'),
    url(r'^get/(\d+)/users', 'film.views.filmUsers'),


    url(r'^get/(\d+)/edit', 'film.views.editFilm'),
    url(r'^get/(\d+)/delete', 'film.views.filmDel'),
    url(r'^get/(\d+)', 'film.views.film'),
    url(r'^', 'film.views.films'),
    #url(r'^articles/all$', 'article.views.articles'),
    #url(r'^articles/like/(?P<article_id>\d+)', 'article.views.like'),
    url(r'^', 'film.views.indexFilm'),


)
