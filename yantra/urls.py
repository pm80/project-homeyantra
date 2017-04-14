from django.conf.urls import url
from yantra import views
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
app_name = 'yantra'
urlpatterns = [
    url(r'^$', views.signup, name='signup'),
    url(r'^signup_fun/$', views.signup_fun, name='signup_fun'),
    url(r'^database/$', views.database, name='database'),
    url(r'^complete/$', views.f1, name='complete'),
    url(r'^error/$', views.fError, name='error'),
]
#if settings.DEBUG:
#    urlpatterns += [
#    url(r'^media/(?P<path>.*)$', serve, {
#    'document_root': settings.MEDIA_ROOT,
#    }),
#    ]

