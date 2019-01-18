from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from DataAccess.DataBaseConnection import DataBaseConnection
from sqlalchemy.orm import relationship


class RecordType(DataBaseConnection.Base):
    __tablename__ = "tblRecordType"
    ID = Column(Integer, primary_key=True)
    Description = Column(String, nullable=False)
    ExterneID = Column(String, nullable=False)
    __timerecord__ = relationship("TimeRecord")

    def __str__(self):
        return self.Description + '     ' + self.ExterneID
