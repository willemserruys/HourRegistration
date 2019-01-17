from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()


class RecordType(Base):
    __tablename__ = "tblRecordType"
    ID = Column(Integer, primary_key=True)
    Description = Column(String, nullable=False)
    ExterneID = Column(String, nullable=False)

    def __str__(self):
        return self.Description + '     ' + self.ExterneId
