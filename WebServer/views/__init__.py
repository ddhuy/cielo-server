# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Register your views here.
from WebServer.views.base import BasePage
from WebServer.views.control_server import ControlServerPage
__all__ = [
    'BasePage',
    'ControlServerPage',
]
