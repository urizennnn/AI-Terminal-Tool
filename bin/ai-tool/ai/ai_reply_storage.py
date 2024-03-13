import redis

class RedisDatabase:
    def __init__(self, host="redis", port=6379, db=0):
        # Connect to the Redis server
        self.redis_db = redis.StrictRedis(
            host=host, port=port, db=db, decode_responses=True
        )

    def add_item(self, key, value):
        # Add an item to the Redis database
        self.redis_db.set(key, value)
        # print(f"Added {key}: {value} to the database.")

    def remove_item(self, key):
        # Remove an item from the Redis database
        if self.redis_db.exists(key):
            self.redis_db.delete(key)
            print(f"Removed {key} from the database.")
        else:
            print(f"{key} not found in the database.")

    def get_all_data(self):
        # Get all key-value pairs from the Redis database
        all_keys = self.redis_db.keys()
        all_data = {key: self.redis_db.get(key) for key in all_keys}
        return all_data

    def delete_all_data(self):
        # Delete all keys and their associated values
        self.redis_db.flushall()
        # print("All data deleted from Redis.")
