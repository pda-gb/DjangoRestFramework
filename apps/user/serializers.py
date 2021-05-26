from rest_framework.serializers import HyperlinkedModelSerializer

from apps.user.models import User


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
