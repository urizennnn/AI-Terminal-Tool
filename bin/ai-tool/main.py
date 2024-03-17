from terminal.input import get_argument_from_terminal, run_terminal_command
from ai.ai_command import generate_command
from ai.ai_reply_storage import RedisDatabase

import datetime
import os
import signal
from terminal.interruption import cleanup

redis_db = RedisDatabase()
user_command = str(get_argument_from_terminal())
signal.signal(signal.SIGINT, cleanup)

OS = os.name
MAX_ITE = 5

# print(is_connected)
if OS == 'nt':
    OS = 'Windows'
# print(OS)

for _ in range(MAX_ITE):
    ai_command = generate_command(user_command, OS)

    if "stop" in ai_command:
        redis_db.delete_all_data()
        break

    terminal_output = run_terminal_command(ai_command)
    current_datetime = datetime.datetime.now()
    data = {ai_command: terminal_output}
    redis_db.add_item(str(current_datetime), str(data))
    user_command = user_command + "[" + terminal_output.lower() + "]"
    print("AI Command: ", ai_command, "\nTerminal Output: ", terminal_output)

redis_db.delete_all_data()
