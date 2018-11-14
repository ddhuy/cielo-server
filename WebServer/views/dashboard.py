import json

from Cielo.cielo_errno import EID

from WebServer.models import BoardInfo
from WebServer.serializers import BoardInfoSerializer
from WebServer.views import BasePage


class DashboardPage(BasePage):
    template_name = 'dashboard.html'

    def __init__(self):
        super(DashboardPage, self).__init__()
        self._func_dict = {
            'GetBoards': self.__get_boards,
            'InsertBoard': self.__insert_board,
            'UpdateBoard': self.__update_board,
            'DeleteBoard': self.__delete_board,
        }

    @staticmethod
    def __get_boards(request):
        board_serial = request.POST.get('Serial', None)
        if board_serial is None:
            return EID.OK, BoardInfoSerializer(BoardInfo.objects, many = True).data
        else:
            return EID.OK, BoardInfoSerializer(BoardInfo.objects(Serial = board_serial), many = True).data

    @staticmethod
    def __insert_board(request):
        board_data = request.POST.get('Data', None)

        try:
            board_data = json.loads(board_data)
        except Exception as ex:
            return EID.BAD_REQUEST, str(ex)

        try:
            board_info = BoardInfo(**board_data).save()
            return EID.OK, BoardInfoSerializer(board_info).data
        except Exception as ex:
            return EID.INTERNAL_SERVER_ERROR, str(ex)

    @staticmethod
    def __update_board(request):
        board_id = request.POST.get('ID', None)
        board_serial = request.POST.get('Serial', None)
        board_data = request.POST.get('Data', None)

        try:
            board_data = json.loads(board_data)
        except Exception as ex:
            return EID.BAD_REQUEST, str(ex)

        try:
            if board_id:
                board_info = BoardInfo.objects.get(id = board_id)
                board_info.modify(**board_data)
                return EID.OK, BoardInfoSerializer(board_info).data
            elif board_serial:
                board_info = BoardInfo.objects.get(Serial = board_serial)
                board_info.modify(**board_data)
                return EID.OK, BoardInfoSerializer(board_info).data
            else:
                return EID.BAD_REQUEST, 'Could not update Board with empty ID and Serial'
        except Exception as ex:
            return EID.INTERNAL_SERVER_ERROR, str(ex)

    @staticmethod
    def __delete_board(request):
        board_id = request.POST.get('ID', None)
        board_serial = request.POST.get('Serial', None)

        try:
            if board_id:
                return EID.OK, BoardInfo.objects(id = board_id).delete()
            elif board_serial:
                return EID.OK, BoardInfo.objects(Serial = board_serial).delete()
            else:
                return EID.BAD_REQUEST, 'Could not update Board with empty ID and Serial'
        except Exception as ex:
            return EID.INTERNAL_SERVER_ERROR, str(ex)
