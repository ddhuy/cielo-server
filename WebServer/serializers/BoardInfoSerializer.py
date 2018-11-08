from rest_framework import serializers

from WebServer.models import BoardInfo

class BoardInfoSerializer ( serializers.HyperlinkedModelSerializer ) :
    class Meta:
        model = BoardInfo
        fields = '__all__'
