from BusinessEntities.RecordType import RecordType
from DataAccess.DataBaseConnection import DataBaseConnectionEntityFramework

db = DataBaseConnectionEntityFramework()
recordType = RecordType()
recordType.REC_Description = 'test'
recordType.REC_ExterneID = 'test2'
db.Base.metadata.create_all(db.Engine)
db.Session.add(recordType)
db.Session.commit()
