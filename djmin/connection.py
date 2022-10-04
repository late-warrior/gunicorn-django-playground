from multiprocessing import Pool
import sqlalchemy.pool as pool
import time

import logging

logger = logging.getLogger('gunicorn.glogging.Logger')

import os

class Conn:

    def rollback(s):
        pass

    def close(a):
        pass

    def __init__(self,a):
        self.a = a

    
def get_connection():
    return Conn({"a": time.time()})

_SNOWFLAKE_CONNECTION_POOL = pool.QueuePool(get_connection, max_overflow=5, pool_size=3)

def get_conn():
    pid = os.getpid()
    print(f"pid={pid}, pool={_SNOWFLAKE_CONNECTION_POOL}")

    return _SNOWFLAKE_CONNECTION_POOL.connect()

def worker_exit(server, worker):
    logger.info("Exiting - releasing pol")
    pid = os.getpid()
    print(f"pid={pid}, exiting pool={_SNOWFLAKE_CONNECTION_POOL}")
    _SNOWFLAKE_CONNECTION_POOL.dispose()