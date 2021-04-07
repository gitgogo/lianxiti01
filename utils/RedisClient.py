import redis

pool = redis.ConnectionPool(max_connections=100, host='127.0.0.1', port='6379', password='', decode_responses=True)
con = redis.StrictRedis(host='', port='', password='', decode_responses=True)
# decode_responses=True，写入的 k-v中的 Value 为 string 类型，不加则写入的为字节类型。
con_pool = redis.StrictRedis(connection_pool=pool)
con_pool.set('name', 'wonda')
# ex：过期时间（秒）
# px：过期时间（毫秒）
# nx：如果设置为True，则只有name不存在时，当前set操作才执行
# xx：如果设置为True，则只有name存在时，当前set操作才执行
con_pool.hgetall('name')
print(con_pool.get('name'))


class RDSClient:
    def __init__(self, host, port, pwd):
        self.pool = redis.ConnectionPool(max_connections=100,
                                         host='127.0.0.1',
                                         port='6379',
                                         password='',
                                         decode_responses=True)
        self.con = redis.StrictRedis(connection_pool=self.pool)

    def get(self, k):
        result = -1
        try:
            result = self.con.get(k)
        except Exception as e:
            print(e)
        self.con.close()
        return result
