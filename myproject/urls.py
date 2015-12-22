from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import index

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
     url(r'^$', index), 
     url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', i),
    url(r'^admin/', include(admin.site.urls)),
)
