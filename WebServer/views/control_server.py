import json

from Cielo.cielo_errno import EID

from WebServer.models import ControlServer
from WebServer.serializers import ControlServerSerializer
from WebServer.views import BasePage


class ControlServerPage(BasePage):
    template_name = ''

    def __init__(self):
        super(ControlServerPage, self).__init__()
        self._func_dict = {
            'GetControlServers': self.__get_control_servers,
            'InsertControlServer': self.__insert_control_server,
            'UpdateControlServer': self.__update_control_server,
            'DeleteControlServer': self.__delete_control_server,
        }

    @staticmethod
    def __get_control_servers(request):
        server_id = request.POST.get('ID', None)
        if server_id is None:
            return EID.OK, ControlServerSerializer(ControlServer.objects, many = True).data
        else:
            return EID.OK, ControlServerSerializer(ControlServer.objects(id = server_id)).data

    @staticmethod
    def __insert_control_server(request):
        data = request.POST.get('Data', None)
        if not data:
            return EID.BAD_REQUEST, 'Could not insert empty Control Server'

        try:
            data = json.loads(data)
        except Exception as ex:
            return EID.BAD_REQUEST, str(ex)

        try:
            server = ControlServer(**data).save()
            return EID.OK, ControlServerSerializer(server).data
        except Exception as ex:
            return EID.INTERNAL_SERVER_ERROR, str(ex)

    @staticmethod
    def __update_control_server(request):
        server_id = request.POST.get('ID', None)
        if not server_id:
            return EID.BAD_REQUEST, 'Could not update Control Server with empty ID'
        data = request.POST.get('Data', None)
        if not data:
            return EID.BAD_REQUEST, 'Could not update Control Server with empty Data'

        try:
            data = json.loads(data)
        except Exception as ex:
            return EID.BAD_REQUEST, str(ex)

        try:
            server = ControlServer.objects.get(id = server_id)
            server.modify(**data)
            return EID.OK, ControlServerSerializer(server).data
        except Exception as ex:
            return EID.INTERNAL_SERVER_ERROR, str(ex)

    @staticmethod
    def __delete_control_server(request):
        server_id = request.POST.get('ID', None)
        if not server_id:
            return EID.BAD_REQUEST, 'Could not update Control Server with empty ID'

        try:
            return EID.OK, ControlServer.objects(id = server_id).delete()
        except Exception as ex:
            return EID.INTERNAL_SERVER_ERROR, str(ex)
