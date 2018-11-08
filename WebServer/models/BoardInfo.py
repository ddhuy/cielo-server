# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from mongoengine import DynamicEmbeddedDocument, EmbeddedDocument, Document, fields

from WebServer.models.ControlServer import ControlServer

####################
# HARDWARE SECTION #
####################
class HardwareSection ( DynamicEmbeddedDocument ) :
    pass

####################
# SOFTWARE SECTION #
####################
class SoftwareSection ( DynamicEmbeddedDocument ) :
    pass

###############
# PUBLIC INFO #
###############
class PublicInfo ( EmbeddedDocument ) :
    Hardware = fields.EmbeddedDocumentField(HardwareSection)
    Software = fields.EmbeddedDocumentField(SoftwareSection)

###############
# BMC SECTION #
###############
class BmcSection ( DynamicEmbeddedDocument ) :
    IP = fields.StringField()
    Username = fields.StringField()
    Password = fields.StringField()
    MaxSOL = fields.StringField()

#################
# POWER SECTION #
#################
class PowerSection ( DynamicEmbeddedDocument ) :
    Type = fields.StringField()
    Vendor = fields.StringField()
    IP = fields.StringField()
    Port = fields.StringField()

################
# PRIVATE INFO #
################
class PrivateInfo ( EmbeddedDocument ) :
    BMC = fields.EmbeddedDocumentField(BmcSection)
    Power = fields.EmbeddedDocumentField(PowerSection)

################
# NOTES INFO #
################
class NoteInfo ( DynamicEmbeddedDocument ) :
    pass

################
# DEVICES INFO #
################
class DeviceInfo ( EmbeddedDocument ) :
    Type = fields.StringField()
    Vendor = fields.StringField()
    Serial = fields.StringField()
    Capacity = fields.StringField()
    Speed = fields.StringField()
    Slot = fields.StringField()
    Revision = fields.StringField()

##############
# BOARD INFO #
##############
BOARD_STT_REMOVED = 'D'
BOARD_STT_FREE = 'F'
BOARD_STT_BUSY = 'B'
BOARD_STATUSES = (
    (BOARD_STT_REMOVED, 'Removed'),
    (BOARD_STT_FREE, 'Free'),
    (BOARD_STT_BUSY, 'Busy'),
)
BOARD_STT_DEFAULT = BOARD_STT_FREE
class BoardInfo ( Document ) :
    meta = {'collection': 'Boards'}
    Serial = fields.StringField(null = False, blank = False, required = True, unique = True)
    Status = fields.StringField(null = False, blank = False, choices = BOARD_STATUSES, default = BOARD_STT_DEFAULT)
    Info = fields.EmbeddedDocumentField(PublicInfo)
    Private = fields.EmbeddedDocumentField(PrivateInfo)
    Devices = fields.ListField(fields.EmbeddedDocumentField(DeviceInfo))
    Note = fields.EmbeddedDocumentField(NoteInfo)
    Server = fields.ReferenceField(ControlServer, required = True)
