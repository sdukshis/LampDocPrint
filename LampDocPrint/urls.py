from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LampDocPrint.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', 'main.views.home'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/'}),
    url(r'', include('main.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
)
