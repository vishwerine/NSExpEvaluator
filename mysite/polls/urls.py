from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'index/$',views.index2,name='index2'),
	url(r'^$',views.index,name='index'),
	url(r'article/',views.article,name='article'),
	url(r'get/(\d+)/$', views.getarticle, name='getarticle'),
]


