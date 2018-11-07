# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from mongoengine import Document, fields

#from WebServer.models.BoardInfo import BoardInfo
#from WebServer.models.RackInfo import RackInfo

CONTROL_SERVER_STT_ACTIVE = 'A'
CONTROL_SERVER_STT_REMOVED = 'D'
CONTROL_SERVER_STATUSES = (
    (CONTROL_SERVER_STT_ACTIVE, 'ACTIVE'),
    (CONTROL_SERVER_STT_REMOVED, 'Removed'),
)
CONTROL_SERVER_STT_DEFAULT = CONTROL_SERVER_STT_ACTIVE

class ControlServer ( Document ) :
    meta = {'collection': 'ControlServers'}

    Name = fields.StringField(null = False, blank = False, required = True, unique = True)
    IP = fields.StringField(null = False, blank = False)
    Port = fields.StringField(null = False, blank = False)
    Status = fields.StringField(null = False, blank = False, choices = CONTROL_SERVER_STATUSES, default = CONTROL_SERVER_STT_DEFAULT)
    #Racks = fields.ListField(fields.EmbeddedDocumentField(RackInfo))
    #Boards = fields.ListField(fields.EmbeddedDocumentField(BoardInfo))

    def __str__ ( self ) :
        return '[%s][%s][%s:%s]' % (self.Status, self.Name, self.IP, self.Port)

print('CONTROL SERVER')
