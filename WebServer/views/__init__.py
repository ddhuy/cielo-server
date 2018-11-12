# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Register your views here.
from WebServer.views.base import BasePage
from WebServer.views.control_server import ControlServerPage
from WebServer.views.dashboard import DashboardPage
from WebServer.views.home import HomePage
__all__ = [
    'BasePage',
    'ControlServerPage',
    'DashboardPage',
    'HomePage',
]
