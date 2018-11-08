from django.conf.urls import url

import WebServer.views

urlpatterns = [
    url(r'^control_server/', WebServer.views.ControlServerPage.as_view(), name = 'control_server'),
]
