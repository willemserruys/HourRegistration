from tkinter import ttk, messagebox, filedialog, Toplevel, StringVar, Label, Entry, Button
from BusinessLogic import BLExcel, BLTimeRecordView, Globals

import numpy as np
import matplotlib.pyplot as plt

from python_linq import From

import plotly
import plotly.plotly as py
import plotly.graph_objs as go


class ExportToGraphsForm:
    def __init__(self, conn):
        plotly.tools.set_credentials_file(
            username='wpserruy', api_key='lDDsb4klBruI5B76RAI5')
        plotly.tools.set_config_file(world_readable=True,
                                     sharing='public')
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
        self.CreateGraph(timeRecords, fromDate, toDate)

    def Show(self):
        self.Master.mainloop()

    def CreateGraph(self, timeRecords, fromdate, todate):
        # Make a fake dataset:
        records = (From(timeRecords).groupBy(
            lambda x: x.Project,
            transform=lambda x: x.Minutes
        ))

        bars = []
        height = []
        for record in records:
            bars.append(record.key)
            height.append(From(record).sum(lambda x: x)/60)
        print(bars)
        print(height)

        data = [go.Bar(
            x=bars,
            y=height
        )]

        py.plot(data, filename="data from " + fromdate + "-" + todate)
