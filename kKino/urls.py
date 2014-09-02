from django.conf.urls import patterns, include, url

from django.contrib import admin
#import article
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'KmKProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'basic/', include('article.urls')),
    url(r'^auth/', include('loginsys.urls')),
    url(r'^film/', include('film.urls')),
    url(r'^articles/', include('article.urls')),
    url(r'^', 'film.views.indexFilm'),

)
