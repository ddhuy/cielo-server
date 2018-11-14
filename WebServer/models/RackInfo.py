# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from mongoengine import Document, fields

from WebServer.models.ControlServer import ControlServer

RACK_STT_ACTIVE = 'A'
RACK_STT_INACTIVE = 'I'
RACK_STATUSES = (
    (RACK_STT_ACTIVE, 'Active'),
    (RACK_STT_INACTIVE, 'Inactive'),
)
RACK_STT_DEFAULT = RACK_STT_INACTIVE

RACK_TYPE_ = ''
RACK_TYPES = (
)
RACK_TYPE_DEFAULT = RACK_TYPE_


class RackInfo(Document):
    Name = fields.StringField(max_length = 255, required = True, null = False, blank = False)
    Type = fields.StringField(max_length = 255, required = True, null = False, blank = False,
                              choices = RACK_TYPES, default = RACK_TYPE_DEFAULT)
    Status = fields.StringField(max_length = 255, required = True, null = True, blank = True,
                                choices = RACK_STATUSES, default = RACK_STT_DEFAULT)
    Server = fields.ReferenceField(ControlServer)

    def __str__(self):
        return '%s:%s:%s' % (self.Status, self.Type, self.Name)
