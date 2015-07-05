from django.conf.urls import patterns, url, include
from swop import views
from django.conf import settings
from django.conf.urls.static import static
from swop.views import ProfileDetailView, ProfileImageView, ProfileImageIndexView

urlpatterns = patterns('',
    url(r'^imageindex/', ProfileImageIndexView.as_view(), name='home'),
    url(r'^$', views.swopengine, name='swop'),

    url(r'^upload/', ProfileImageView.as_view(), name='profile_image_upload'),
    url(r'^uploaded/(?P<pk>\d+)/$', ProfileDetailView.as_view(),
        name='profile_image'),


) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
urlpatterns = patterns('swop.views',
    url(r'^list/$', 'list', name='list'),
    url(r'^$', 'swopengine', name='swop'),

)


urlpatterns=patterns('',
                     url(r'^$', views.swopengine, name='index')
                     )
'''