import os, sys, json, errno
import logging, logging.config

# Logging configuration
LOGGING = {
    "version" : 1,
    "disable_existing_logger" : False,
    "formatters" : {
        "verbose" : {
            "class" : "logging.Formatter",
            "format" : "[%(asctime)s][%(levelname)7s][%(filename)s:%(lineno)d] - %(message)s",
            "datefmt" : "%Y:%m:%d-%H:%M:%S"
        },
        "simple" : {
            "format" : "[%(filename)s:%(lineno)d] - %(message)s"
        }
    },
    "handlers" : {
        "filelog" : {
            "class" : "Cielo.Cielo_FileHandler.Cielo_TimedRotatingFileHandler",
            "level" : "DEBUG",
            "formatter" : "verbose",
            "filename" : "Logs/cielo-webserver.log",
            "interval" : 1,
            "when" : "h",
            "backupCount" : 24,
            "encoding" : "utf8"
        },
        "console" : {
            "class" : "logging.StreamHandler",
            "level" : "DEBUG",
            "formatter" : "simple",
        }
    },
    "loggers" : {
        # used to log all Django messages
        "django" : {
            "level" : "DEBUG",
            "handlers" : ["console", "filelog"],
            "propagate" : True
        },
        # used to log Cielo messages
        "CIELO" : {
            "level" : "DEBUG",
            "handlers" : ["console", "filelog"],
            "propagate" : True
        },
    },
}

class Cielo_Logger ( object ) :
    logging.config.dictConfig(LOGGING)
    __logger = logging.getLogger('CIELO')

    def __getattr__ ( self, Attr ) :
        try :
            return Cielo_Logger.__logger.__getattr__(Attr)
        except (Exception) as ex :
            return Cielo_Logger.__logger.__getattribute__(Attr)

#################
# Global LOGGER #
#################
LOG = Cielo_Logger()
