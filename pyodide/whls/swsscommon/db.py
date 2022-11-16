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


from base import send_redis_command

# \sonic-buildimage\src\sonic-swss-common\common\database_config.json
db_dict = {
    "APPL_DB": "0",
    "ASIC_DB": "1",
    "COUNTERS_DB": "2",
    "LOGLEVEL_DB": "3",
    "CONFIG_DB": "4",
    "PFC_WD_DB": "5",
    "FLEX_COUNTER_DB": "5",
    "STATE_DB": "6",
    "SNMP_OVERLAY_DB": "7",
    "RESTAPI_DB": "8",
    "GB_ASIC_DB": "9",
    "GB_COUNTERS_DB": "10",
    "GB_FLEX_COUNTER_DB": "11",
    "CHASSIS_APP_DB": "12",
    "CHASSIS_STATE_DB": "13",
    "APPL_STATE_DB": "14",
}


class RedisClient(DBClient):
    def __init__(self):
        self.Client = None

    '''operatioin'''
    # @abstractmethod(callable)
    def connect(self, db_name):
        # connect to database
        db = db_dict[db_name]
        self.select(db)

    # @abstractmethod(callable)
    def close(self, db_name):
        # close the connection
        self.select("0")

    # @abstractmethod(callable)
    def select(self, db):
        # select a database in redis
        status, msg, data = send_redis_command("select", db)
        return data

    # @abstractmethod(callable)
    def get_table(self, table):
        # get all entries in the table

        # \sonic-buildimage\src\sonic-yang-models\tests\files\sample_config_db.json
        # Is this right?
        return self.hgetall(table)

    # @abstractmethod(callable)
    def delete_table(self, table):
        #
        # delete the tables

        # \sonic-buildimage\src\sonic-yang-models\tests\files\sample_config_db.json
        # Is this right?
        return self.delete(table)

    # @abstractmethod(callable)
    def flushdb(self):
        status, msg, data = send_redis_command("flushdb")
        return data


    '''key related commands'''
    # @abstractmethod(callable)
    def keys(self, key):
        # Is this right?
        status, msg, data = send_redis_command("keys", "*")
        return data

    # @abstractmethod(callable)
    def exists(self, key):
        status, msg, data = send_redis_command("exists", key)
        return data

    # @abstractmethod(callable)
    def delete(self, *args):
        status, msg, data = send_redis_command("del", args)
        return data

    # @abstractmethod(callable)
    def scan(self, *args, **kwargs):
        # https://redis.io/commands/scan/
        # Is this right?
        status, msg, data = send_redis_command("scan", args)
        return data



    '''hash related commands'''
    # @abstractmethod(callable)
    def hset(self, key, field, value):
        # https://redis.io/commands/hset/
        status, msg, data = send_redis_command("hset", key, field, value)
        return data

    # @abstractmethod(callable)
    def hmset(self, multiHash):
        # https://redis.io/commands/hmset/
        # deprecated, replaced by hset, and don't know how to use the arg: multiHash
        # Is this right?
        pass

    # @abstractmethod(callable)
    def hget(self, key, field):
        # https://redis.io/commands/hget/
        status, msg, data = send_redis_command("hget", key, field)
        return data

    # @abstractmethod(callable)
    def hgetall(self, key):
        # https://redis.io/commands/hgetall/
        status, msg, data = send_redis_command("hgetall", key)
        print("[DEBUG]", status, msg, data)
        return data

    # @abstractmethod(callable)
    def hexists(self, key, field):
        # https://redis.io/commands/hexists/
        status, msg, data = send_redis_command("hexists", key, field)
        return data



    '''key related commands'''
    # @abstractmethod(callable)
    def set(self, db_name, _hash, key, val, blocking=False):
        # Is this right?
        db = db_dict[db_name]
        self.select(db)

        status, msg, data = send_redis_command("set", key, val)
        return data

    # @abstractmethod(callable)
    def incr(self, key):
        # https://redis.io/commands/incr/
        status, msg, data = send_redis_command("incr", key)
        return data

    # @abstractmethod(callable)
    def decr(self, key):
        # https://redis.io/commands/decr/
        status, msg, data = send_redis_command("decr", key)
        return data

