from django.conf.urls import patterns, url
from blog import views
app_name = 'blog'
urlpatterns = patterns('',
    #url(r'^$', views.index,name='index'),
    url(r'title.html$', views.data,name='second'),
 	url(r'(?P<ob>[0-9]+)/$', views.tail, name='third'),
# 	url(r'$', views.message,name='message'), 
)
