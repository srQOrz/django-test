from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^user/(?P<user_name>[\S]*)/$', views.user, name='user'),
	url(r'^(?P<blog_id>[0-9]+)/$',views.detail, name='detail'),
]
