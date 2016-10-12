from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from users.serializers import UserSerializer

from crowdhub.api import BaseListView, BaseDetailView


class UserList(BaseListView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetail(BaseDetailView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserCurrentDetail(BaseDetailView):
    serializer_class = UserSerializer

    def get(self, request):
        return Response(self.serializer_class(request.user).data)


class AuthTokenDetail(BaseDetailView):

    def get(self, request, format=None):
        token, created  = Token.objects.get_or_create(user=request.user)
        content = {
            'user_id': request.user.id,
            'user': request.user.username,
            'auth': request.auth,
            'token' : token.key,
            'created' : created,
        }
        return Response(content)

