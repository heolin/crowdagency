from django.conf.urls import url

from tasks import views

urlpatterns = [
    url(r'tasks/$', views.list, name="list"),
    url(r'tasks/(?P<task_id>[0-9]+)$', views.view, name="view"),
]
