from tkinter import ttk, messagebox, Button, Tk, StringVar, Label, Entry, Listbox, END
from BusinessLogic import BLProject, BLRecordType, BLTimeRecordView, BLTimeRecord, TimeRecordValidation, BLDayView, Cache, Globals
from BusinessEntities import TimeRecord, TimeRecordStatusEnum, DayView
import time
from GUI.RecordTypeEditForm import RecordTypeEditForm


class RecordTypeListForm:
    def __init__(self, Cache, conn):
        self.Cache = Cache
        self.Connection = conn

        master = Tk()
        self.Master = master
        master.protocol('WM_DELETE_WINDOW', self.Quit)
        self.Master.title("Record Types")

        self.AddButton = Button(master, text='Add', command=self.Add)
        self.AddButton.grid(row=0, column=0, sticky='NSEW')

        self.EditButton = Button(master, text='Edit', command=self.Edit)
        self.EditButton.grid(row=0, column=1, sticky='NSEW')

        self.DeleteButton = Button(master, text='Delete', command=self.Delete)
        self.DeleteButton.grid(row=0, column=2, sticky='NSEW')

        self.RecordTypesListBox = Listbox(master, width=80)
        self.RecordTypesListBox.grid(
            row=1, column=0, columnspan=10, sticky='NSEW')

        self.FillRecordTypes()

        self.RecordTypesListBox.bind('<Double-1>', lambda x: self.Edit())

    # def CloseWindow(self):
    #     self.Master.quit()

    def Quit(self):
        self.Master.quit()

    def Show(self):
        self.Master.mainloop()

    def FillRecordTypes(self):
        self.RecordTypesListBox.delete(0, END)
        recordTypes = self.Cache.RecordTypes
        for item in recordTypes:
            self.RecordTypesListBox.insert(END, item)

    def Add(self):
        pr = RecordTypeEditForm(self.Connection)
        pr.Show()
        self.Cache.RefreshRecordTypes()
        self.FillRecordTypes()
        pr.Master.destroy()

    def Edit(self):
        sel = self.RecordTypesListBox.curselection()[0]
        recordType = self.GetRecordType(sel)
        pr = RecordTypeEditForm(self.Connection, recordType)
        pr.Show()
        self.Cache.RefreshRecordTypes()
        self.FillRecordTypes()
        pr.Master.destroy()

    def Delete(self):
        sel = self.RecordTypesListBox.curselection()[0]
        project = self.GetRecordType(sel)
        bl = BLRecordType.BLRecordType(self.Connection)
        bl.DeleteByID(project.ID)
        self.Cache.RefreshRecordTypes()
        self.FillRecordTypes()

    def GetRecordType(self, ID):
        return self.Cache.RecordTypes[ID]
