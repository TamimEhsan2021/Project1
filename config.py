import configparser

config = configparser.ConfigParser()
config['DEFAULT'] = {'DATABASE_TYPE': '',
                     'DBAPI': '',
                     'HOST': '',
                     'USER': '',
                     'PASSWORD': '',
                     'DATABASE': '',
                     'PORT': ''}
with open('sqlconfig.ini', 'w') as configfile:
    config.write(configfile)