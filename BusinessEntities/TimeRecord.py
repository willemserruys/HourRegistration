from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from BusinessEntities.RecordType import RecordType
from DataAccess.DataBaseConnection import DataBaseConnection


class TimeRecord(DataBaseConnection.Base):
    __tablename__ = "TimeRecord"
    ID = Column(Integer, primary_key=True)
    StartHour = Column(String, nullable=True)
    EndHour = Column(String, nullable=False)
    ProjectID = Column(Integer,  ForeignKey(
        'Project.ID'), nullable=False)
    RecordTypeID = Column(Integer, ForeignKey(
        'RecordType.ID'), nullable=False)
    Description = Column(String, nullable=False)
    StatusID = Column(Integer, ForeignKey(
        'TimeRecordStatus.ID'), nullable=False)
    Minutes = Column(Integer, nullable=True)
    OneNote = Column(String, nullable=True)
    Km = Column(Integer, nullable=True)
    RecordType = relationship(
        "RecordType", back_populates="__timerecord__")
    Status = relationship(
        "TimeRecordStatus", back_populates="__timerecord__")
    Project = relationship(
        "Project", back_populates="__timerecord__"
    )

    def __str__(self):
        return self.Description
