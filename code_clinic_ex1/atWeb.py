from datetime import date
from urllib import request

__version__ = '0.0.1'

def get_data_for_date(date):
    '''
    Returns an generator object of data of the specific date
    '''

    # use correct accessor methods based on date
    return _get_data_from_github(date)
    

def _get_data_from_github(date):
    pass