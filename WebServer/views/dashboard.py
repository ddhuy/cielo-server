import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from Cielo.cielo_errno import EID
from Cielo.cielo_logger import LOG

from WebServer.models import BoardInfo
from WebServer.serializers import BoardInfoSerializer
from WebServer.views import BasePage

class DashboardPage ( BasePage ) :
    template_name = 'dashboard.html'

    def __init__ ( self ) :
        super(DashboardPage, self).__init__()
        self._funcdict = {
            'GetBoards': self.__GetBoards,
            'InsertBoard': self.__InsertBoard,
            'UpdateBoard': self.__UpdateBoard,
            'DeleteBoard': self.__DeleteBoard,
        }

    def __GetBoards ( self, request, *args, **kwargs ) :
        return EID.OK, BoardInfoSerializer(BoardInfo.objects, many = True).data

    def __InsertBoard ( self, request, *args, **kwargs ) :
        Data = request.POST.get('Data', None)

        try :
            Data = json.loads(Data)
        except Exception as ex:
            return EID.BAD_REQUEST, str(ex)

        try :
            Board = BoardInfo(**Data).save()
            return EID.OK, BoardInfoSerializer(Board).data
        except Exception as ex:
            return EID.INTERNAL_SERVER_ERROR, str(ex)

    def __UpdateBoard ( self, request, *args, **kwargs ) :
        ID = request.POST.get('ID', None)
        Serial = request.POST.get('Serial', None)
        Data = request.POST.get('Data', None)

        try :
            Data = json.loads(Data)
        except Exception as ex:
            return EID.BAD_REQUEST, str(ex)

        try :
            if (ID) :
                Board = BoardInfo.objects.get(id = ID)
                b = Board.modify(**Data)
                return EID.OK, BoardInfoSerializer(Board).data
            elif (Serial) :
                Board = BoardInfo.objects.get(Serial = Serial)
                b = Board.modify(**Data)
                return EID.OK, BoardInfoSerializer(Board).data
            else :
                return EID.BAD_REQUEST, 'Could not update Board with empty ID and Serial'
        except Exception as ex:
            return EID.INTERNAL_SERVER_ERROR, str(ex)

    def __DeleteBoard ( self, request, *args, **kwargs ) :
        ID = request.POST.get('ID', None)
        Serial = request.POST.get('Serial', None)
        try :
            if (ID) :
                return EID.OK, BoardInfo.objects(id = ID).delete()
            elif (Serial) :
                return EID.OK, BoardInfo.objects(Serial = Serial).delete()
            else :
                return EID.BAD_REQUEST, 'Could not update Board with empty ID and Serial'
        except Exception as ex:
            return EID.INTERNAL_SERVER_ERROR, str(ex)
