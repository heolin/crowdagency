from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('users.urls', namespace="users")),
    url(r'^', include('users.urls_api', namespace="api-users")),
    url(r'^', include('tasks.urls', namespace="tasks")),
    url(r'^', include('tasks.urls_api', namespace="api-tasks")),
    url(r'^', include('clients.urls_api', namespace="api-clients")),
    url(r'^', include('clients.urls', namespace="clients")),
    url(r'^convert/', include('lazysignup.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

