from datetime import date, datetime, timedelta
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
        self.tablename = kwargs.get('tablename', 'Weather')
        sql = '''CREATE TABLE IF NOT EXISTS {} 
                (Date Text, Time Text, Status Text, Air_Temp Float, Baromatric_Press Float, Wind_Speed Float)'''.format(self._dbTable)
        self._db.execute(sql)

    
    def get_data_for_range(self, start, end):
        '''
        Given the start and end dates, download the data for the year range
        Delete the data between start and end dates
        Insert the data from the downloaded
        '''

        #Delete existing data
        self._db.execute('DELETE FROM {} WHERE DATE BETWEEN {} AND {}'.format(self._dbTable, start.strftime('%Y%m%d'), end.strftime('%Y%m%d')))
        self._db.commit()

        years_to_download = []
        for i in range(start.year, end.year + 1): years_to_download.append(i)

        data_for_all_years = []
        for year in years_to_download: data_for_all_years.append(list(atWeb.get_data_for_date(year)))
        
        for entry in data_for_all_years:
            if datetime.strptime(entry['Date'], '%Y_%m_%d').date() >= start and datetime.strptime(entry['Date'], '%Y_%m_%d').date() <= end:
                self._db.execute('''INSERT INTO {} (Date, Time, Status, Air_Temp, Barometric_Press, Wind_Speed) 
                                    VALUES (?, ?, ?, ?, ?, ?)'''.format(self._dbTable), (entry['Date'].replace('_', ''),
                                                                                         entry['Time'],
                                                                                         'Complete',
                                                                                         entry['Air_Temp'],
                                                                                         entry['Barometric_Press'],
                                                                                         entry['Wind_Speed']))
                self._db.commit()

        cursor = self._db.execute('SELECT Air_Temp, Barometric_Press, Wind_Speed FROM {} WHERE Date BETWEEN {} AND {}'.format(self._dbTable, 
                                                                                                                              start.strftime('%Y%m%s'),
                                                                                                                              end.strftime('%Y%m%s')))
        for row in cursor:
            yield dict(row)

    def clear(self):
        '''
        Clear out the database by dropping the table
        '''
        self._db.execute('DROP TABLE IF EXISTS {}'.format(self._dbTable))


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

