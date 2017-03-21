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
        self.table = kwargs.get('tablename', 'Weather')