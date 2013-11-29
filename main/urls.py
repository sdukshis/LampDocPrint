from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from main.views import ContractorList
from main.views import ContractorCreate, ContractorUpdate, ContractorDelete

urlpatterns = patterns('main.views',
    url(r'^$', 'home'),
    url(r'contractors/$', login_required(ContractorList.as_view()),
                              name="contractors"),
    url(r'^contractor/add/$', login_required(ContractorCreate.as_view()),
                              name='contractor_add'),
    url(r'^contractor/(?P<pk>\d+)/$', login_required(ContractorUpdate.as_view()),
                              name='contractor_update'),
    url(r'^contractor/(?P<pk>\d+)/delete$', login_required(ContractorDelete.as_view()),
                              name='contractor_delete'),
)

