from terminal.input import get_argument_from_terminal, run_terminal_command
from ai.ai_command import generate_command
from ai.ai_reply_storage import RedisDatabase
import datetime
import os

user_command = str(get_argument_from_terminal())
OS = os.name
# MAX_ITE = 5
# print(is_connected)

if OS == 'nt':
    OS='Windows'


# print(OS)
ai_command = generate_command(user_command, OS)
    
terminal_output = run_terminal_command(ai_command)
current_datetime = datetime.datetime.now()
data = {ai_command: terminal_output}


user_command = user_command + "[" + terminal_output.lower() + "]"

print("AI Command: ", ai_command, "\nTerminal Output: ", terminal_output)

