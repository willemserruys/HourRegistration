class TimeRecordView:
        __tablename__ = "vwTimeRecord"
        ID = Column()
        StartHour = startHour
        EndHour = endHour
        Project = project
        RecordType = recordType
        Description = description
        Status = status
        Date = date
        OneNoteLink = oneNoteLink
        Km = km

    def __str__(self):
        return str(self.StartHour) + '     ' + str(self.EndHour) + '       ' + self.Project
