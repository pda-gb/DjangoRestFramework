from rest_framework.viewsets import ModelViewSet

from apps.user.models import User
from apps.user.serializers import UserModelSerializer


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
