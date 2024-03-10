import openai
from dotenv import load_dotenv
import os
from ai.ai_reply_storage import RedisDatabase
from variable_file_reader import extract_api_key_value, extract_model_value

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY") or extract_api_key_value()


def generate_command(user_command):
    # Check if the OpenAI API key is set
    if not openai.api_key:
        raise ValueError("OpenAI API key is not set")

    # Get All Redis Data
    redis_db = RedisDatabase()
    all_data = redis_db.get_all_data()

    # Use OpenAI GPT-3.5-turbo model to generate content
    response = openai.ChatCompletion.create(
        model=extract_model_value(),
        messages=[
            {
                "role": "system",
                "content": """You will generate a command a terminal understands based on the user command given and the data available, you will translate their command essentially. For example, "create a folder named rodeo"
                and you will return a command "mkdir rodeo". If there is a success message, simply return 'stop'. Do not return any other thing apart from the command. If there is an error in the data given Please handle errors gracefully and provide a helpful command in case of failure. Example of error is user command is
                "create a new folder called terminal" and all the data available is "5:00 : mkdir terminal, mkdir: cannot create directory ‘terminal’: File exists'", You will assess the situation and return a new command like "ls" to check what is in the directory which will store
                the contents in a redis database, you will then be prompted again with the data available which will now be '5:00 : command: mkdir terminal, output: mkdir: cannot create directory ‘terminal’: File exists, 5:01 : command: ls, output: terminal, ai. After seeing this data
                you will know that a file named terminal already exists and then you will change the name of the folder created to something like "terminal1". ONLY RETURN THE COMMAND, DO NOT RETURN AN EXPLANATION. If there is a success message, simply return 'stop'. DO NOT RETURN YOUR REASONING PROCESS
                FOR AN OUTPUT SIMPLY RETURN THE COMMAND. ---------------------------
                """,
            },
            {
                "role": "user",
                "content": f"The user command is {user_command}, the current data is {all_data}",
            },
        ],
    )

    # Extract the generated content from the API response
    generated_content = response["choices"][0]["message"]["content"]

    return generated_content
