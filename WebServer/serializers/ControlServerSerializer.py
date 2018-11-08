from rest_framework import serializers

from WebServer.models import ControlServer

class ControlServerSerializer ( serializers.HyperlinkedModelSerializer ) :
    class Meta:
        model = ControlServer
        fields = '__all__'
