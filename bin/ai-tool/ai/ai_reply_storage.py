import redis
import os
host = str(os.getenv("REDIS_HOST"))
password = str(os.getenv("REDIS_PASSWORD"))
class RedisDatabase:
    def __init__(self, host="redis-13367.c274.us-east-1-3.ec2.cloud.redislabs.com", port=13367, password="IABJr9jMiuXSYAgJx2qdBXdNIAquqKbE", db=0):
        # Attempt to connect to the Redis server
        try:
            self.redis_db = redis.StrictRedis(
                    host=host, port=port, password=password, db=db, decode_responses=True
                    )
            self.connected = True
        except redis.ConnectionError:
            print("Failed to connect to Redis server.")
            self.connected = False

    def is_connected(self):
        # Check if the Redis server is connected
        return self.connected

    def add_item(self, key, value):
        # Add an item to the Redis database
        if self.connected:
            self.redis_db.set(key, value)
        else:
            print("Not connected to Redis server.")

    def remove_item(self, key):
        # Remove an item from the Redis database
        if self.connected:
            if self.redis_db.exists(key):
                self.redis_db.delete(key)
                print(f"Removed {key} from the database.")
            else:
                print(f"{key} not found in the database.")
        else:
            print("Not connected to Redis server.")

    def get_all_data(self):
        all_keys = self.redis_db.keys()
        all_data = {key: self.redis_db.get(key) for key in all_keys}
        return all_data

    def delete_all_data(self):
        self.redis_db.flushall()
