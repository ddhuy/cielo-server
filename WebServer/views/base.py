import time, httplib

from django.http import JsonResponse
from django.views.generic import TemplateView
from rest_framework.renderers import JSONRenderer

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from Cielo.cielo_logger import LOG
from Cielo.cielo_errno import EID

@method_decorator(csrf_exempt, name = 'dispatch')
class BasePage ( TemplateView ) :
    def __init__ ( self ) :
        self._funcdict = {}
        # self._JSONRenderer = JSONRenderer()

    def post ( self, request, *args, **kwargs ) :
        LOG.info(request.POST)
        req_action = request.POST.get('Action', '')
        for action in self._funcdict :
            if (action == req_action) :
                s = time.clock()
                errno, post_resp = self._funcdict[action](request, *args, **kwargs)
                e = time.clock()
                LOG.info('[%s][%d] time: %f', action, errno, e - s)
                # json_resp = self._JSONRenderer.render(post_resp)
                return JsonResponse(status = httplib.OK, data = {'Errno': errno, 'Data': post_resp})
        return JsonResponse(status = httplib.OK, data = {'Errno': EID.NOT_FOUND, 'Data': 'Request method not found'})
