from terminal.input import get_argument_from_terminal, run_terminal_command
from ai.ai_command import generate_command
from ai.ai_reply_storage import RedisDatabase
import datetime

redis_db = RedisDatabase()

user_command = get_argument_from_terminal()

MAX_ITE = 5

for _ in range(MAX_ITE):
    ai_command = generate_command(user_command)
    if "stop" in ai_command.lower():
        print(terminal_output)
        redis_db.delete_all_data()
        break
    
    terminal_output = run_terminal_command(ai_command)

    current_datetime = datetime.datetime.now()
    data = {ai_command: terminal_output}

    redis_db.add_item(str(current_datetime), str(data))

    user_command = user_command + "[" + terminal_output.lower() + "]"

    print("AI Command: ", ai_command, "\nTerminal Output: ", terminal_output)

redis_db.delete_all_data()
