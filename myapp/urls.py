from django.conf.urls import patterns, url

from myapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^admin/$', views.admin),
    url(r'^post(\d+)/$', views.post, name='post'),
    url(r'^add_post/$', views.add_post, name='add_post'),
    url(r'^add_comment/$', views.add_comment, name='add_comment'),
)