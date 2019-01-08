from tkinter import *
from tkinter import ttk, messagebox
from BusinessLogic import BLProject, BLRecordType, BLTimeRecordView, BLTimeRecord, TimeRecordValidation, BLDayView, Cache, Globals
from BusinessEntities import TimeRecord, TimeRecordStatusEnum, DayView, Project, RecordType
import sqlite3
from DataAccess.Log import Logger
# import time
# import datetime


class RecordTypeEditForm:
    def __init__(self, conn, recordType=None):
        master = Tk()
        self.Connection = conn
        self.RecordTypeExterneID = StringVar(master)
        self.RecordTypeOmschrijving = StringVar(master)

        self.Master = master
        self.Master.title("Record Type Edit Form")

        if recordType == None:
            self.BusinessEntity = None
        else:
            self.BusinessEntity = recordType
            self.RecordTypeOmschrijving.set(recordType.Description)
            self.RecordTypeExterneID.set(recordType.ExterneId)

        self.RecordTypeOmschrijvingLabel = Label(
            master, text='RecordType Omschrijving: ')
        self.RecordTypeOmschrijvingLabel.grid(row=0, column=0)

        self.RecordTypeExterneIDLabel = Label(
            master, text='RecordType Externe ID: ')
        self.RecordTypeExterneIDLabel.grid(row=1, column=0)

        self.RecordTypeOmschrijvingEntry = Entry(
            master, textvariable=self.RecordTypeOmschrijving)
        self.RecordTypeOmschrijvingEntry.grid(row=0, column=1)

        self.RecordTypeExterneIDEntry = Entry(
            master, textvariable=self.RecordTypeExterneID)
        self.RecordTypeExterneIDEntry.grid(row=1, column=1)

        self.OKButton = Button(master, text="OK", command=self.Confirm)
        self.OKButton.grid(row=6, column=0, sticky='NSEW')

        self.CancelButton = Button(master, text="Cancel", command=self.Quit)
        self.CancelButton.grid(row=6, column=1, sticky='NSEW')

    def Show(self):
        self.Master.mainloop()

    def Quit(self):
        self.Master.destroy()

    def Confirm(self):
        try:
            if self.BusinessEntity == None:
                recordType = RecordType.RecordType(
                    None, self.RecordTypeOmschrijving.get(), self.RecordTypeExterneID.get())
                bl = BLRecordType.BLRecordType(self.Connection)
                bl.Create(recordType)
            else:
                recordType = self.BusinessEntity
                recordType.Description = self.RecordTypeOmschrijving.get()
                recordType.ExterneId = self.RecordTypeExterneID.get()
                bl = BLRecordType.BLRecordType(self.Connection)
                bl.Update(recordType)
            self.Master.quit()
        except Exception as e:
            Logger.LogError(str(e))
            return
