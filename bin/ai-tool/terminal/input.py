import sys
from subprocess import run, PIPE, CalledProcessError


def get_argument_from_terminal():
    # Check if at least one argument is provided
    if len(sys.argv) < 2:
        print("Usage: python main.py <argument>")
        sys.exit(1)

    # Return the first argument (index 1, as index 0 is the script name)
    return sys.argv[1]


def run_terminal_command(command):
    try:
        result = run(command, shell=True, check=True, stderr=PIPE)
        if result.stdout is not None:
            output = result.stdout.decode("utf-8")
        else:
            output = ""
        return f"Command '{command}' executed successfully. Output: {output}"
    except CalledProcessError as e:
        return f"Error executing command '{command}': {e.stderr.decode('utf-8')}"
