import sys
from ai.ai_reply_storage import RedisDatabase


def cleanup(signum,frame):
    redis_db = RedisDatabase()


    all_data = redis_db.get_all_data()



    print("\nInterruption detected. Deleting AI memory...")

    redis_db.delete_all_data()

    sys.exit(1)
