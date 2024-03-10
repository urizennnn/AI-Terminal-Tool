import re


def extract_model_value(file_path='openai.txt'):
    # Read the text file
    with open(file_path, "r") as file:
        content = file.read()

    # Split the text into lines
    lines = content.split("\n")

    # Search for the line containing 'model='
    for line in lines:
        if "model=" in line:
            # Extract the value after '='
            model_value = line.split("=")[1].strip()
            return model_value

    # Return None if 'model=' is not found
    return None


def extract_api_key_value(file_path='openai.txt'):
    # Read the text file
    with open(file_path, "r") as file:
        content = file.read()

    # Split the text into lines
    lines = content.split("\n")

    # Search for the line containing 'OPENAI_API_KEY='
    for line in lines:
        if "OPENAI_API_KEY=" in line:
            # Extract the value after '='
            model_value = line.split("=")[1].strip()
            return model_value

    # Return None if 'OPENAI_API_KEY=' is not found
    return None

