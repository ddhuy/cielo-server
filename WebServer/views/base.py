import time

from django.http import JsonResponse
from django.views.generic import TemplateView

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from Cielo.cielo_logger import LOG
from Cielo.cielo_errno import EID


@method_decorator(csrf_exempt, name = 'dispatch')
class BasePage(TemplateView):
    def __init__(self):
        super(BasePage, self).__init__()
        self._func_dict = {}

    def post(self, request):
        LOG.info(request.POST)
        req_action = request.POST.get('Action', '')
        for action in self._funcdict:
            if action == req_action:
                s = time.clock()
                errno, post_resp = self._func_dict[action](request)
                e = time.clock()
                LOG.info('[%s][%d] time: %f', action, errno, e - s)
                return JsonResponse(status = EID.OK, data = {'Errno': errno, 'Data': post_resp})
        return JsonResponse(status = EID.OK, data = {'Errno': EID.NOT_FOUND, 'Data': 'Request method not found'})
