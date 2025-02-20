try:
    from django.urls import reverse
except ImportError:
    from django.urls import reverse
from urllib.parse import quote


def login_link(request):
    """
    This assumes your login link is the Shibboleth login page for your server
    and uses the 'target' url parameter.
    """
    full_path = quote(request.get_full_path())
    login = reverse("shibboleth:login")
    ll = f"{login}?target={full_path}"
    return {"login_link": ll}


def logout_link(request, *args):
    """
    This assumes your login link is the Shibboleth login page for your server
    and uses the 'target' url parameter.
    e.g: https://school.edu/Shibboleth.sso/Login
    """
    try:
        from app_settings import LOGOUT_REDIRECT_URL
    except ImportError:
        from .app_settings import LOGOUT_REDIRECT_URL
    # LOGOUT_REDIRECT_URL specifies a default logout page that will always be used when
    # users logout from Shibboleth.
    target = LOGOUT_REDIRECT_URL or quote(request.build_absolute_uri())
    logout = reverse("shibboleth:logout")
    ll = f"{logout}?target={target}"
    return {"logout_link": ll}
