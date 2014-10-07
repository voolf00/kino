from django.conf.urls import patterns, include, url
from kKino import settings
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings


# import article
admin.autodiscover()

if settings.DEBUG:
    urlpatterns = patterns('',
        (r'^media/(.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )

urlpatterns += patterns('',
                       # Examples:
                       # url(r'^$', 'KmKProject.views.home', name='home'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'basic/', include('article.urls')),
                       url(r'^auth/', include('loginsys.urls')),
                       url(r'^film/', include('film.urls')),
                       url(r'^articles/', include('article.urls')),

                       url(r'^', 'film.views.indexFilm'),


)
# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

