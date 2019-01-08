import sqlite3
from BusinessEntities import RecordType


class DARecordType:
    def __init__(self, conn):
        self.Cursor = conn.Connection.cursor()
        self.Connection = conn.Connection

    def GetAll(self):
        self.Cursor.execute("SELECT * FROM tblRecordType")
        rows = self.Cursor.fetchall()
        Projects = []
        for row in rows:
            project = RecordType.RecordType(
                row[0], row[1], row[2].replace("\n", ""))
            Projects.append(project)
        return Projects

    def GetRecordTypeIDFromDescription(self, recordTypeName):
        sql = "select REC_ID from tblRecordType where REC_Description = ?"
        self.Cursor.execute(sql, (recordTypeName,))
        result = []
        for row in self.Cursor.fetchall():
            result.append(row[0])
        if len(result) == 0:
            return None
        else:
            return int(result[0])

    def GetRecordTypeExterneID(self, recordTypeID):
        sql = "select REC_ExterneID from tblRecordType where REC_ID = ?"
        self.Cursor.execute(sql, (recordTypeID,))
        result = []
        for row in self.Cursor.fetchall():
            result.append(row[0])
        if len(result) == 0:
            return None
        else:
            return result[0]

    def Create(self, recordType):
        self.Cursor.execute("INSERT INTO tblRecordType (REC_Description,REC_ExterneID) values(?,?)",
                            (recordType.Description, recordType.ExterneId))
        self.Connection.commit()

    def Update(self, recordType):
        self.Cursor.execute("Update tblRecordType set REC_Description=?,REC_ExterneID=? where REC_ID=?",
                            (recordType.Description, recordType.ExterneId, recordType.ID))
        self.Connection.commit()

    def DeleteByID(self, recordTypeID):
        self.Cursor.execute(
            "delete from tblRecordType where REC_ID = ?", (str(recordTypeID),))
        self.Connection.commit()
