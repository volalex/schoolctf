from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
from schoolctf import settings

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'schoolctf.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       #main
                       url(r'^$', 'scoreboard.views.index'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^summernote/', include('django_summernote.urls')),

                       #login and registration urls
                       url(r'accounts/registration', 'scoreboard.views.registration'),
                       url(r'^accounts/login/$', 'django.contrib.auth.views.login'),

                       #news urls
                       url(r'news/(\d)/$', 'scoreboard.views.detail_news'),

                       #main urls
                       url(r'tasks/$', 'scoreboard.views.tasks'),
                       url(r'tasks/(\d)/$', 'scoreboard.views.task_detail'),
                       url(r'tasks/solve/(\d)/$', 'scoreboard.views.task_solve')


) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
