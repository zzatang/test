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
            db.sql_do(sql[, params])
            perform non-select query
        '''
        self._db.execute(sql, params)
        self._db.commit()

    def sql_query(self, sql, params = ()):
        '''
            db.sql_query(sql[, params])
            run the sql with the parameters. 
            returns a generator 
        '''
        c = self._db.cursor()
        c.execute(sql, params)
        for r in c:
            yield r

    def sql_query_row(self, sql, params = ()):
        '''
            db.sql_query_row(sql[, params])
            run the sql with the parameters.
            return one row
        '''
        c = self._db.cursor()
        c.execute(sql, params)
        return c.fetchone()

    def sql_query_value(self, sql, params = ()):
        '''
            db.sql_query_value(sql[, params])
            run the sql with the parameters
            return a single value
        '''
        c = self._db.cursor()
        c.execute(sql, params)
        return c.fetchone()[0]

    def getrec(self, id):
        '''
            db.getrec(id)
            return single row by id
        '''
        query = 'SELECT * FROM {} WHERE id = ?'.format(self._dbTable)
        c = self._db.execute(query, (id,))
        return c.fetchone()

    def getrecs(self):
        '''
            db.getrecs()
            return all rows, return a generator
        '''
        query = 'SELECT * FROM {}'.format(self._dbTable)
        c = self._db.execute(query)
        for r in c:
            yield r

    def countrecs(self):
        '''
            db.countrecs()
            return number of records
        '''
        query = 'SELECT COUNT(*) FROM {}'.format(self._dbTable)
        c = self._db.execute(query)
        return c.fetchone()[0]

    def delete(self, id):
        '''
            db.delete(id)
            delete a row by id
        '''
        query = 'DELETE FROM {} WHERE id = ?'.format(self._dbTable)
        self._db.execute(query, (id,))
        self._db.commit()

    def insert(self, rec):
        '''
            db.insert(rec)
            insert a single record into table
            rec is a dict
        ''' 
        klist = sorted(rec.keys())
        values = [rec[k] for k in klist]
        query = 'INSERT INTO {} ({}) VALUES = ({})'.format(self._dbTable, ', '.join(klist), ', '.join('?' for k in klist))
        c = self._db.execute(query, values)
        self._db.commit()
        return c.lastrowid
        
    def update(self, id, rec):
        '''
            db.update(id, rec)
            update a record by id
            rec is a dict
        '''
        

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
    def table(self):
        return self._dbTable

    @table.setter
    def table(self, t):
        self._dbTable = t

    @table.deleter
    def table(self):
        del self._dbTable