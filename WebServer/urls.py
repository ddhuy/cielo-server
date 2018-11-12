from django.conf.urls import url

import WebServer.views

urlpatterns = [
    url(r'^$', WebServer.views.HomePage.as_view(), name = 'home'),
    url(r'^control_server/', WebServer.views.ControlServerPage.as_view(), name = 'control_server'),
    url(r'^dashboard/', WebServer.views.DashboardPage.as_view(), name = 'dashboard'),
]
