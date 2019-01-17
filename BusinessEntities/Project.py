from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Project(Base):
    __tablename__ = "tblProject"
    ID = Column(Integer, primary_key=True)
    Description = Column(String, nullable=False)
    ExterneID = Column(String, nullable=False)
    Button = Column(Integer, nullable=True)
    Actief = Column(Integer, nullable=False)

    def __str__(self):
        addString = ''
        if not str(self.Button) == 'None':
            addString = '       ' + str(self.Button)
        return self.Description + addString
