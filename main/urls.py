from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.conf import settings

from main.views import *

urlpatterns = patterns('main.views',
    url(r'^$', 'home'),
    url(r'^contractors/$', login_required(ContractorList.as_view()),
                              name="contractors"),
    url(r'^contractor/add/$', login_required(ContractorCreate.as_view()),
                              name='contractor_add'),
    url(r'^contractor/(?P<pk>\d+)/$', login_required(ContractorUpdate.as_view()),
                              name='contractor_update'),
    url(r'^contractor/(?P<pk>\d+)/delete$', login_required(ContractorDelete.as_view()),
                              name='contractor_delete'),
    url(r'^lamps/$', login_required(LampList.as_view()),
                              name="lamps"),
    url(r'^lamp/add/$', login_required(LampCreate.as_view()),
                              name='lamp_add'),
    url(r'^lamp/(?P<pk>\d+)/$', login_required(LampUpdate.as_view()),
                              name='lamp_update'),
    url(r'^lamp/(?P<pk>\d+)/delete$', login_required(LampDelete.as_view()),
                              name='lamp_delete'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
