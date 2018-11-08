import os, logging

class Cielo_TimedRotatingFileHandler ( logging.handlers.TimedRotatingFileHandler ) :
    def __init__ ( self, filename, **kwargs ) :
        filepath = os.path.dirname(filename)
        if (filepath and (not os.path.isdir(filepath))) :
            os.makedirs(filepath)
        super(Cielo_TimedRotatingFileHandler, self).__init__(filename, **kwargs)

    def emit ( self, record ) :
        if (not os.path.isfile(self.baseFilename)) :
            open(self.baseFilename, 'wb').close()
            self.doRollover()
        if (self.shouldRollover(record)) :
            self.doRollover()
        super(Cielo_TimedRotatingFileHandler, self).emit(record)
