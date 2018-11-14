# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from WebServer.views import BasePage


class HomePage(BasePage):
    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name)
