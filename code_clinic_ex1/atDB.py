﻿from datetime import date, datetime, timedelta
from tkinter import messagebox
import sqlite3
import atWeb

__version__ = '0.0.1'

class atDB():
    '''
    A database class to track all information
    '''

    def __init__(self, **kwargs):
        self.filename = kwargs.get('filename', 'lpo.db')
        self.table = kwargs.get('tablename', 'Weather')
        sql = '''CREATE TABLE IF NOT EXISTS {} 
                (Date Text, Time Text, Status Text, Air_Temp Float, Baromatric_Press Float, Wind_Speed Float)'''.format(self._dbtable)
        self._db.execute(sql)

    
    def get_data_for_range(self, start, end):
        '''
        Given the start and end dates, download the data for the year range
        Delete the data between start and end dates
        Insert the data from the downloaded
        '''
        years_to_download = []
        for i in range(start.year, end.year + 1): years_to_download.append

        for year in years_to_download:
            pass



    ### setting filename property
    @property
    def filename(self):
        return self._dbFilename

    @filename.setter
    def filename(self, fn):
        self._dbFilename = fn
        self._db = sqlite3.connect(fn)
        self._db.row_factory = sqlite3.Row

    @filename.deleter
    def filename(self):
        self.close()

    def close(self):
        self._db.close()
        del self._dbFilename

    @property
    def tablename(self):
        return self._dbTable

    @tablename.setter
    def tablename(self, t):
        self._dbTable = t

    @tablename.deleter
    def tablename(self):
        del self._dbTable

