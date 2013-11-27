from django.conf.urls import patterns, url

urlpatterns = patterns('main.views',
    url(r'^$', 'home'),
    url(r'^contractor/(?P<id>\d+)/$', 'contractor'),
    url(r'^contractor/list/$', 'list_contractor'),
    url(r'^contractor/add/$', 'add_contractor'),
)

