from BusinessEntities.RecordType import RecordType
from BusinessEntities.TimeRecord import TimeRecord
from BusinessEntities.Project import Project
from DataAccess.DataBaseConnection import DataBaseConnection
import sqlite3

db = DataBaseConnection()
timeRecord = TimeRecord()
recordType = RecordType()
recordType.Description = "test"
recordType.ExterneID = "test"
timeRecord.Description = "test"
timeRecord.RecordTypeID = 200
timeRecord.StatusID = 1
timeRecord.ProjectID = 1
db.Base.metadata.create_all(db.Engine)


try:
    db.Session.add(recordType)
    db.Session.add(timeRecord)
    db.Session.commit()
except sqlite3.IntegrityError as e:
    print(e)
