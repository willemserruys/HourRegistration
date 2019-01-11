from tkinter import ttk, messagebox, filedialog, Toplevel, StringVar, Label, Entry, Button
from BusinessLogic import BLExcel, BLTimeRecordView, Globals

import numpy as np
import matplotlib.pyplot as plt

from python_linq import From


class ExportToGraphsForm:
    def __init__(self, conn):
        master = Toplevel()
        self.Master = master
        self.Connection = conn
        self.DateFrom = StringVar()
        self.DateTo = StringVar()

        self.Master.title("Export To Graphs")

        self.ExplanationLabel = Label(
            master, text='Export to graph between dates')
        self.ExplanationLabel.grid(row=0, column=0, columnspan=2)

        self.DateFromLabel = Label(
            master, text='Select FROM date (yyyy-mm-dd):')
        self.DateFromLabel.grid(row=1, column=0)

        self.DateFromTextBox = Entry(master, textvariable=self.DateFrom)
        self.DateFromTextBox.grid(row=1, column=1, sticky='NSEW')

        self.DateFromLabel = Label(master, text='Select TO date (yyyy-mm-dd):')
        self.DateFromLabel.grid(row=2, column=0)

        self.DateToTextBox = Entry(master, textvariable=self.DateTo)
        self.DateToTextBox.grid(row=2, column=1, sticky='NSEW')

        self.OKButton = Button(master, text="OK", command=self.Confirm)
        self.OKButton.grid(row=3, column=0, sticky='NSEW')

    def Confirm(self):
        fromDate = self.DateFrom.get()
        toDate = self.DateTo.get()
        blTrV = BLTimeRecordView.BLTimeRecordView(self.Connection)
        timeRecords = blTrV.GetAllBetweenDates(fromDate, toDate)
        self.CreateGraph(timeRecords)

    def Show(self):
        self.Master.mainloop()

    def CreateGraph(self, timeRecords):
        # Make a fake dataset:
        records = (From(timeRecords).groupBy(
            lambda x: x.Project,
            transform=lambda x: x.Minutes
        ))

        bars = []
        height = []
        for record in records:
            bars.append(record.key)
            height.append(From(record).sum(lambda x: x))
        print(bars)
        print(height)
        y_pos = np.arange(len(bars))

        # Create bars
        plt.bar(y_pos, height)

        # Create names on the x-axis
        plt.xticks(y_pos, bars)

        # Show graphic
        plt.show()
