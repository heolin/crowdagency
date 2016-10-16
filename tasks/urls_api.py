from django.conf.urls import url

from tasks import api

urlpatterns = [
    url(r'api/protocols/$', api.ProtocolList.as_view(), name="protocols"),
    url(r'api/protocols/(?P<pk>[0-9]+)$', api.ProtocolDetail.as_view(), name="protocols"),
    url(r'api/protocols/(?P<pid>[0-9]+)/tasks$', api.ProtocolTasksList.as_view(), name="protocols-tasks"),

    url(r'api/tasks/$', api.TaskList.as_view(), name="tasks"),
    url(r'api/tasks/(?P<pk>[0-9]+)$', api.TaskDetail.as_view(), name="tasks"),

    url(r'api/tasks/(?P<tid>[0-9]+)/stats$', api.TaskStatsDetail.as_view(), name="tasks-stats"),
    url(r'api/tasks/(?P<tid>[0-9]+)/items$', api.TaskItemsList.as_view(), name="tasks-items"),
    url(r'api/tasks/(?P<tid>[0-9]+)/items/next', api.NextItemDetail.as_view(), name="tasks-items-next"),
    url(r'api/tasks/(?P<tid>[0-9]+)/items/(?P<iid>[0-9a-z]+)$', api.TaskItemsDetail.as_view(), name="tasks-items"),
    url(r'api/tasks/(?P<tid>[0-9]+)/items/(?P<iid>[0-9a-z]+)/stats$', api.TaskItemsDetailStats.as_view(), name="tasks-items-stats"),

    url(r'api/tasks/(?P<tid>[0-9]+)/items/(?P<iid>[0-9a-z]+)/annotations$', api.ItemAnnotationList.as_view(), name="tasks-items-annotations"),
    url(r'api/tasks/(?P<tid>[0-9]+)/items/(?P<iid>[0-9a-z]+)/annotations/(?P<aid>[0-9a-z]+)$', api.ItemAnnotationDetail.as_view(), name="tasks-items-annotations"),
]
