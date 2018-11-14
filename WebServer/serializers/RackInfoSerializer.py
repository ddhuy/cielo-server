from rest_framework import serializers

from WebServer.models import RackInfo


class RackInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RackInfo
        fields = '__all__'
