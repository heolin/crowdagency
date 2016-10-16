from django.conf.urls import url

from clients import views, api


urlpatterns = [
    url(r'^$', views.list, name="list"),
    url(r'clients/$', views.list, name="list"),
    url(r'clients/(?P<client_id>[0-9]+)$', views.view, name="view"),
    url(r'clients/(?P<client_id>[0-9]+)/survey$', views.survey, name="survey"),
]
