from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class RecordType(Base):
    __tablename__ = "tblRecordType"
    REC_Id = Column(Integer, primary_key=True)
    REC_Description = Column(String(50), nullable=False)
    REC_ExterneID = Column(String(50), nullable=False)

    # def __init__(self, Id, description, externeId):
    #     self.ID = Id
    #     self.Description = description
    #     self.ExterneId = externeId

    def __str__(self):
        return self.Description + '     ' + self.ExterneId
