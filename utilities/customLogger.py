import logging


class logGen:
    @classmethod
    def generateLogs(cls):
        FORMAT = '%(asctime)s: %(levelname)s: %(message)s'
        logging.basicConfig(filename='.//logs//automation.log',
                            format=FORMAT,
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger
