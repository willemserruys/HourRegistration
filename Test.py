from BusinessEntities.RecordType import RecordType
from BusinessEntities.TimeRecord import TimeRecord
from BusinessEntities.TimeRecordStatus import TimeRecordStatus
from BusinessEntities.Project import Project
from DataAccess.DataBaseConnection import DataBaseConnection
from DataAccess.DAProject import DAProject
import sqlite3

db = DataBaseConnection()
timeRecord = TimeRecord()
timeRecordStatus = TimeRecordStatus()
recordType = RecordType()
recordType.Description = "test"
recordType.ExterneID = "test"
timeRecord.Description = "test"
timeRecord.RecordTypeID = 200
timeRecord.StatusID = 1
timeRecord.ProjectID = 1
db.Base.metadata.create_all(db.Engine)


try:
    # db.Session.add(recordType)
    # db.Session.add(timeRecord)
    # db.Session.commit()
    # print(timeRecord.Status)
    # print(timeRecord.Project)
    proj = DAProject(db.Session)
    for pr in proj.GetProjectIDFromDescription('TestProject'):
        print(pr)
except sqlite3.IntegrityError as e:
    print(e)
