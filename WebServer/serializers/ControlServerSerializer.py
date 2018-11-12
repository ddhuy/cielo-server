from rest_framework_mongoengine import serializers

from WebServer.models import ControlServer

class ControlServerSerializer ( serializers.DocumentSerializer ) :
    class Meta:
        model = ControlServer
        fields = '__all__'
