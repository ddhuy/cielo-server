# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Register your serializers here
from WebServer.serializers.BoardInfoSerializer import BoardInfoSerializer
from WebServer.serializers.ControlServerSerializer import ControlServerSerializer
from WebServer.serializers.RackInfoSerializer import RackInfoSerializer
__all__ = [
    'BoardInfoSerializer',
    'ControlServerSerializer',
    'RackInfoSerializer',
]
