from django.conf.urls import patterns, url
from knitting import views
urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^registration/$', views.register_view, name='registration'),
        url(r'^course1/$', views.course1, name='DigitalKnitting'),
        url(r'^test/$', views.test, name='Test'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^resume/$', views.resume, name='resume'),

        )