from base import send_redis_command, get_random_id
import json
import re

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


class DBClient:
    def __init__(self):
        self.cid = get_random_id()

    '''operatioin'''
    def connect(self, db_name):
        # connect to database
        db = db_dict[db_name]
        self.select(db)

    def close(self, db_name):
        # close the connection
        self.cid = get_random_id()

    def select(self, db):
        # select a database in redis
        status, msg, data = send_redis_command(self.cid, "select", db)
        return data

    def get_table(self, table):
        # get all entries in the table
        # \sonic-buildimage\src\sonic-yang-models\tests\files\sample_config_db.json
        keys_str = self.keys("CONFIG_DB", table + "*")
        res = {}
        try:
            keys_arr = json.loads(keys_str)
            for key in keys_arr:
                data = self.hgetall(key)
                res[key.split("|")[1]] = data
        except:
            pass
        return res

    def delete_table(self, table):
        #
        # delete the tables

        # \sonic-buildimage\src\sonic-yang-models\tests\files\sample_config_db.json
        # Is this right?
        return self.delete(table)

    def flushdb(self):
        status, msg, data = send_redis_command(self.cid, "flushdb")
        return data

    def raw_to_list(self, data):
        return re.sub("[\[\]\"\']", "", data).split(",")
    '''key related commands'''
    def keys(self, *args):
        db = args[0]
        key = args[1]
        self.connect(db)
        status, msg, data = send_redis_command(self.cid, "keys", key)
        return data

    def exists(self, key):
        status, msg, data = send_redis_command(self.cid, "exists", key)
        return data

    def delete(self, *args):
        status, msg, data = send_redis_command(self.cid, "del", args)
        return data

    def scan(self, *args, **kwargs):
        # https://redis.io/commands/scan/
        # Is this right?
        status, msg, data = send_redis_command(self.cid, "scan", args)
        return data



    '''hash related commands'''
    def hset(self, table, key, data):
        # https://redis.io/commands/hset/\
        ret_str = ""
        for k, v in data.items():
            status, msg, data = send_redis_command(self.cid, "hset", table+"|"+key, k, v)
            ret_str += data
        return ret_str

    def hmset(self, multiHash):
        # https://redis.io/commands/hmset/
        # deprecated, replaced by hset, and don't know how to use the arg: multiHash
        # Is this right?
        pass

    def hget(self, key, field):
        # https://redis.io/commands/hget/
        status, msg, data = send_redis_command(self.cid, "hget", key, field)
        return data

    def hgetall(self, key):
        # https://redis.io/commands/hgetall/
        status, msg, data = send_redis_command(self.cid, "hgetall", key)
        return json.loads(data)

    def hexists(self, key, field):
        # https://redis.io/commands/hexists/
        status, msg, data = send_redis_command(self.cid, "hexists", key, field)
        return data



    '''key related commands'''
    def set(self, db_name, _hash, key, val, blocking=False):
        # Is this right?
        db = db_dict[db_name]
        self.select(db)

        status, msg, data = send_redis_command(self.cid, "set", key, val)
        return data

    def incr(self, key):
        # https://redis.io/commands/incr/
        status, msg, data = send_redis_command(self.cid, "incr", key)
        return data

    def decr(self, key):
        # https://redis.io/commands/decr/
        status, msg, data = send_redis_command(self.cid, "decr", key)
        return data
