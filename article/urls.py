from django.conf.urls import patterns, include, url




urlpatterns = patterns('',

    url(r'^3/', 'article.views.template_three'),
    url(r'^$', 'article.views.articles'),
    url(r'^delete/(\d+)', 'article.views.delArticle'),
    url(r'^get/(\d+)/(\d+)', 'article.views.article'),
    url(r'^get/(\d+)', 'article.views.article'),
    url(r'^addarticle', 'article.views.addArticle'),
    url(r'^editarticle/(\d+)', 'article.views.editArticle'),
    url(r'^like/(?P<article_id>\d+)', 'article.views.like'),
    url(r'^addcomment/(?P<article_id>\d+)', 'article.views.addComment'),
    url(r'^page/(\d+)','article.views.articles'),



)
