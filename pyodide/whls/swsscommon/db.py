from abc import abstractmethod

class DBClient:
    def __init__(self):
        self.Client = None

    '''operatioin'''
    @abstractmethod(callable)
    def connect(self, db_name):
        # connect to database
        pass

    @abstractmethod(callable)
    def close(self, db_name):
        # close the connection
        pass

    @abstractmethod(callable)
    def select(self, db):
        # select a database in redis
        pass

    @abstractmethod(callable)
    def get_table(slef, table):
        # get all entries in the table
        pass

    @abstractmethod(callable)
    def delete_table(slef, table):
        # delete the tables 
        pass    

    @abstractmethod(callable)
    def flushdb(self):
        pass


    '''key related commands'''
    @abstractmethod(callable)
    def keys(self, key):
        pass

    @abstractmethod(callable)
    def exists(self, key):
        pass
    
    @abstractmethod(callable)
    def delete(self, *args):
        pass

    @abstractmethod(callable)
    def scan(self, *args, **kwargs):
        pass


    
    '''hash related commands'''
    @abstractmethod(callable)
    def hset(self, key, field, value):
        pass

    @abstractmethod(callable)
    def hmset(self, multiHash):
        pass

    @abstractmethod(callable)
    def hget(self, key, field):
        pass

    @abstractmethod(callable)
    def hgetall(self, key):
        return None


    @abstractmethod(callable)
    def hexists(self, key, field):
        pass



    '''key related commands'''
    @abstractmethod(callable)
    def set(self, db_name, _hash, key, val, blocking=False):
        pass

    @abstractmethod(callable)
    def incr(self, key):
        pass

    @abstractmethod(callable)
    def decr(self, key):
        pass


class RedisClientNaive(DBClient):
    def __init__(self):
        pass

    def get_table(self, table):
        return {'test': {'0': ['111','112','113']}}
    
    def connect(self, db_name):
        pass

    def close(self, db_name):
        pass

