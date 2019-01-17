import sqlite3
import configparser
from DataAccess.Log import Logger

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class DataBaseConnection():
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        try:
            self.Engine = create_engine(
                'sqlite:///HourRegistration.db', echo=True)
            self.Base = declarative_base()
            session = sessionmaker(bind=self.Engine)
            self.Session = session()
            Logger.LogInfo('DataBase Connection Established')
        except Exception as e:
            Logger.LogError(str(e))
