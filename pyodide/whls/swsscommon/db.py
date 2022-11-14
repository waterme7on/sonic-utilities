from abc import abstractmethod

class DBClient:
    def __init__(self):
        self.Client = None

    '''operatioin'''
    @abstractmethod
    def connect(self, db_name):
        # connect to database
        pass

    @abstractmethod
    def close(self, db_name):
        # close the connection
        pass

    @abstractmethod
    def select(self, db):
        # select a database in redis
        pass

    @abstractmethod
    def get_table(slef, table):
        # get all entries in the table
        pass

    @abstractmethod
    def delete_table(slef, table):
        # delete the tables 
        pass    

    @abstractmethod
    def flushdb(self):
        pass


    '''key related commands'''
    @abstractmethod
    def keys(self, key):
        pass

    @abstractmethod
    def exists(self, key):
        pass
    
    @abstractmethod
    def delete(self, *args):
        pass

    @abstractmethod
    def scan(self, *args, **kwargs):
        pass


    
    '''hash related commands'''
    @abstractmethod
    def hset(self, key, field, value):
        pass

    @abstractmethod
    def hmset(self, multiHash):
        pass

    @abstractmethod
    def hget(self, key, field):
        pass

    @abstractmethod
    def hgetall(self, key):
        return None


    @abstractmethod
    def hexists(self, key, field):
        pass



    '''key related commands'''
    @abstractmethod
    def set(self, db_name, _hash, key, val, blocking=False):
        pass

    @abstractmethod
    def incr(self, key):
        pass

    @abstractmethod
    def decr(self, key):
        pass


class RedisClientNaive(DBClient):
    def __init__(self):
        pass

    def get_table(self, table):
        return {'test': {'auto_restart': ['111','112','113']}}
    
    def connect(self, db_name):
        pass

    def close(self, db_name):
        pass

    def select(self, db):
        # select a database in redis
        pass

    def delete_table(slef, table):
        # delete the tables
        pass    

    def flushdb(self):
        pass


    '''key related commands'''
    def keys(self, key):
        pass

    def exists(self, key):
        pass
    
    def delete(self, *args):
        pass

    def scan(self, *args, **kwargs):
        pass


    
    '''hash related commands'''
    def hset(self, key, field, value):
        pass

    def hmset(self, multiHash):
        pass

    def hget(self, key, field):
        pass

    def hgetall(self, key):
        return None

    def hexists(self, key, field):
        pass


    '''key related commands'''
    def set(self, db_name, _hash, key, val, blocking=False):
        pass

    def incr(self, key):
        pass

    def decr(self, key):
        pass
