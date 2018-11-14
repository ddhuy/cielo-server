import os
import logging


class CieloTimedRotatingFileHandler(logging.handlers.TimedRotatingFileHandler):

    def __init__(self, filename, **kwargs):
        file_path = os.path.dirname(filename)
        if file_path and (not os.path.isdir(file_path)):
            os.makedirs(file_path)
        super(CieloTimedRotatingFileHandler, self).__init__(filename, **kwargs)

    def emit(self, record):
        if not os.path.isfile(self.baseFilename):
            open(self.baseFilename, 'wb').close()
            self.doRollover()
        if self.shouldRollover(record):
            self.doRollover()
        super(CieloTimedRotatingFileHandler, self).emit(record)