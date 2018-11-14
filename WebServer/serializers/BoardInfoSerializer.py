from rest_framework_mongoengine import serializers

from WebServer.models import BoardInfo


class BoardInfoSerializer(serializers.DocumentSerializer):
    class Meta:
        model = BoardInfo
        fields = '__all__'
        depth = 2
