from BusinessEntities.RecordType import RecordType
from DataAccess.DataBaseConnection import DataBaseConnectionEntityFramework
import sqlite3

db = DataBaseConnectionEntityFramework()
recordType = RecordType()
recordType.REC_Description = 'test'
#recordType.REC_ExterneID = 'test2'
db.Base.metadata.create_all(db.Engine)

try:
    db.Session.add(recordType)
    db.Session.commit()
except sqlite3.IntegrityError as e:
    print(e)
