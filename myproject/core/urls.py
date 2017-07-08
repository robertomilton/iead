from django.conf.urls import url
from myproject.core import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^person/$', views.person_list, name='person_list'),
    url(r'^person/(?P<pk>\d+)/$', views.person_detail, name='person_detail'),
]
