from django.conf.urls import url

from users import api

app_name = "users"

urlpatterns = [
    url(r'api/users/$', api.UserList.as_view(), name="users"),
    url(r'api/users/authtoken$', api.AuthTokenDetail.as_view(), name="authtoken"),
    url(r'api/users/current', api.UserCurrentDetail.as_view(), name="current"),
    url(r'api/users/(?P<pk>[0-9]+)$', api.UserDetail.as_view(), name="users"),
]
