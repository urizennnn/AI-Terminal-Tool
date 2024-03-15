import anthropic
from dotenv import load_dotenv
import os
from ai.ai_reply_storage import RedisDatabase
from variable_file_reader import extract_api_key_value, extract_model_value

# Load environment variables from .env file
load_dotenv()

# Set Anthropic API key
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY") or extract_api_key_value()

def generate_command(user_command, os):
    # Initialize Anthropic client
    client = anthropic.Anthropic(api_key=anthropic_api_key)

    # Use Anthropic to generate content
    message = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1024,
        system=f"""You will generate a {os} command a terminal understands based on the user command given and the data available, you will translate their command essentially. For example, "create a folder named rodeo" and you will return a command "mkdir rodeo". If there is a success message, simply return 'stop'. Do not return any other thing apart from the command. If there is an error in the data given Please handle errors gracefully and provide a helpful command in case of failure. Example of error is user command is "create a new folder called terminal" and all the data available is "5:00 : mkdir terminal, mkdir: cannot create directory 'terminal': File exists'", You will assess the situation and return a new command like "dir" to check what is in the directory which will store the contents in a redis database, you will then be prompted again with the data available which will now be '5:00 : command: mkdir terminal, output: mkdir: cannot create directory 'terminal': File exists, 5:01 : command: dir, output: terminal, ai. After seeing this data you will know that a file named terminal already exists and then you will change the name of the folder created to something like "terminal1". ONLY RETURN THE COMMAND, DO NOT RETURN AN EXPLANATION.MAKE SURE IT IS A WINDOWS COMMAND. If there is a success message, simply return 'stop'. DO NOT RETURN YOUR REASONING PROCESS FOR AN OUTPUT SIMPLY RETURN THE COMMAND. ---------------------------""",
        messages=[
            {
                "role": "user",
                "content": f"The user command is {user_command}, the current data is empty",
            },
        ]
    )

    # Extract the generated command from the response
    generated_command = message.content[0].text.strip()
    print(generated_command)
    return generated_command