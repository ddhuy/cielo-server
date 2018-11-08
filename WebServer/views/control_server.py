import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from Cielo.cielo_errno import EID
from Cielo.cielo_logger import LOG

from WebServer.models import ControlServer
from WebServer.serializers import ControlServerSerializer
from WebServer.views import BasePage

class ControlServerPage ( BasePage ) :
    template_name = 'control_server.html'

    def __init__ ( self ) :
        super(ControlServerPage, self).__init__()
        self._funcdict = {
            'GetControlServers': self.__GetControlServers,
            'InsertControlServer': self.__InsertControlServer,
            'UpdateControlServer': self.__UpdateControlServer,
            'DeleteControlServer': self.__DeleteControlServer,
        }

    def __GetControlServers ( self, request, *args, **kwargs ) :
        return EID.OK, ControlServerSerializer(ControlServer.objects, many = True).data

    def __InsertControlServer ( self, request, *args, **kwargs ) :
        Data = request.POST.get('Data', None)
        if (not Data) :
            return EID.BAD_REQUEST, 'Could not insert empty Control Server'

        try :
            Data = json.loads(Data)
        except Exception as ex:
            return EID.BAD_REQUEST, str(ex)

        try :
            Server = ControlServer(**Data).save()
            return EID.OK, ControlServerSerializer(Server).data
        except Exception as ex:
            return EID.INTERNAL_SERVER_ERROR, str(ex)

    def __UpdateControlServer ( self, request, *args, **kwargs ) :
        ID = request.POST.get('ID', None)
        if (not ID) :
            return EID.BAD_REQUEST, 'Could not update Control Server with empty ID'
        Data = request.POST.get('Data', None)
        if (not Data) :
            return EID.BAD_REQUEST, 'Could not update Control Server with empty Data'

        try :
            Data = json.loads(Data)
        except Exception as ex:
            return EID.BAD_REQUEST, str(ex)

        try :
            Server = ControlServer.objects.get(id = ID)
            b = Server.modify(**Data)
            return EID.OK, ControlServerSerializer(Server).data
        except Exception as ex:
            return EID.INTERNAL_SERVER_ERROR, str(ex)

    def __DeleteControlServer ( self, request, *args, **kwargs ) :
        ID = request.POST.get('ID', None)
        if (not ID) :
            return EID.BAD_REQUEST, 'Could not update Control Server with empty ID'
        try :
            return EID.OK, ControlServer.objects(id = ID).delete()
        except Exception as ex:
            return EID.INTERNAL_SERVER_ERROR, str(ex)
