from django.urls import path

from .views import ShibbolethLoginView
from .views import ShibbolethLogoutView
from .views import ShibbolethView

app_name = "shibboleth"

urlpatterns = [
    path("login/", ShibbolethLoginView.as_view(), name="login"),
    path("logout/", ShibbolethLogoutView.as_view(), name="logout"),
    path("", ShibbolethView.as_view(), name="info"),
]
