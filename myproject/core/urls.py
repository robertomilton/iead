from django.conf.urls import url
from myproject.core import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^persons/$', views.person_list, name='persons'),
]
