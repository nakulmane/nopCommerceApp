import configparser

config = configparser.RawConfigParser()
config.read('.\\configurations\\config.ini')


class ReadConfig:
    @staticmethod
    def getAppUrl():
        url = config.get('common info', 'baseUrl')
        return url

    @staticmethod
    def getUserName():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password
