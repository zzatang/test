import sqlite3

__version__ = '0.0.1'

class atDB:
    def __init__(self, **kwargs):
        '''
            db = atDB( table = '', filename = '')
        '''
        self.filename = kwargs.get('filename')
        self.table = kwargs.get('table', '')

    def sql_do(self, sql, params = ()):
        '''
            sql_do(sql[, params])
            perform non-select query
        '''
        self._db.execute(sql, params)
        self._db.commit()


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
