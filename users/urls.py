from django.conf.urls import url

from users import views

app_name = "users"

urlpatterns = [
    url(r'users/profile$', views.profile, name="profile"),
    url(r'users/login', views.login, name="login"),
    url(r'users/logout', views.logout, name="logout"),
    url(r'users/register', views.register, name="register"),
    url(r'users/profile', views.profile, name="profile"),
]
