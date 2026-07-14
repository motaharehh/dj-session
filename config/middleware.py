from urllib.parse import urlsplit
from django.contrib import auth
from django.utils.deprecation import MiddlewareMixin
from django.utils.functional import SimpleLazyObject
from session.models import Session
from session.store import SessionStore

def get_user(request):
    if not hasattr(request, "_cached_user"):
        request._cached_user = auth.get_user(request)
    return request._cached_user


class MySessionMiddleware(MiddlewareMixin):

    def process_request(self, request):
        session_key = request.COOKIES.get("sessionid")
        if session_key is None:
            session = Session.create()
        else:
            session = Session.objects.filter(
                session_key=session_key
            ).first()

        if session is None:
            session = Session.create()
        request.session = SessionStore(session)


class AuthenticationMiddleware(MiddlewareMixin):

    def process_request(self, request):
        request.user = SimpleLazyObject(lambda: get_user(request))



