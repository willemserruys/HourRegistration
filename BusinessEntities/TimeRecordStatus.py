from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from BusinessEntities.RecordType import RecordType
from DataAccess.DataBaseConnection import DataBaseConnection


class TimeRecordStatus(DataBaseConnection.Base):
    __tablename__ = "TimeRecordStatus"
    ID = Column(Integer, primary_key=True)
    Description = Column(String, nullable=False)
    __timerecord__ = relationship("TimeRecord")

    def __str__(self):
        return self.Description
