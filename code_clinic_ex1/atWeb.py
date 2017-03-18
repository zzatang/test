from datetime import date
from urllib import request

__version__ = '0.0.1'

Based_URL = 'https://raw.githubusercontent.com/lyndadotcom/LPO_weatherdata/master/Environmental_Data_Deep_Moor_'

def get_data_for_date(date):
    '''
    Returns an generator object of data of the specific date
    '''

    # use correct accessor methods based on date
    return _get_data_from_github(date)
    

def _get_data_from_github(date):
    '''
    Access Github to download whole year data
    '''
    # build the url based on year
    url = '{}{}.txt'.format(Based_URL, date.year)
    print('Fetching online data for {} full year'.format(date.year))

    try:
        year_data = request.urlopen(url).read().decode(encoding='utf_8').split('\n')
    except:
        raise ValueError(date)
    else:
        year_data.pop(0) #remove header line

    for line in year_data:
        elements = line.split()

        yield dict(Date = elements[0],
                   Time = elements[1],
                   Status = 'COMPLETE',
                   Air_Temp = elements[2],
                   Barometric_Press = elements[3],
                   Wind_Speed = elements[8])

    
