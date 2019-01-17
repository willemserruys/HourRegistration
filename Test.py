from BusinessEntities.RecordType import RecordType
from BusinessEntities.TimeRecord import TimeRecord
from BusinessEntities.Project import Project
from DataAccess.DataBaseConnection import DataBaseConnection
import sqlite3

db = DataBaseConnection()
recordType = RecordType()
timeRecord = TimeRecord()

db.Base.metadata.create_all(db.Engine)
timeRecord.ProjectID = 2
timeRecord.RecordTypeID = 200
timeRecord.Description = "Test"
timeRecord.StatusID = 1


try:
    db.Session.add(recordType)
    db.Session.add(timeRecord)
    db.Session.add(project)
    db.Session.commit()
except sqlite3.IntegrityError as e:
    print(e)
