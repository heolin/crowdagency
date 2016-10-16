from django.conf.urls import url

from clients import api

app_name = "api-clients"

urlpatterns = [
    url(r'api/clients/$', api.ClientList.as_view(), name='clients'),
    url(r'api/clients/(?P<pk>[0-9]+)$', api.ClientDetail.as_view(), name='clients'),
]
