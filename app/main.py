import re
import sys
import os
import subprocess
from pathlib import Path


PATHS = os.environ['PATH'].split(os.pathsep)
BUILTIN_COMMANDS = {"exit", "echo", "type", "pwd", "cd"}
QUOTE_SYMBOLS = {"\'", "\"",}

def valid_command(command: str) -> bool:
    valid_commands = {"exit", "echo", "type", "run", "pwd", "cd"}
    return True if command in valid_commands else False


def invalid_command(command: str) -> None:
    print(f"{command}: not found")


def evaluate(input_list: list) -> None:
    # print("input_list=", input_list)
    if executable_path:=get_command_path(input_list[0]):
        executable_args = input_list[1:]
        # print("exepath=", executable_path)
        # print("executable_args=", executable_args, " type=", type(executable_args))
        run_exe(executable_path, *executable_args)
        return

    if not valid_command(input_list[0]):
            invalid_command("".join(input_list[0]))
    else:
        match input_list[0]:
            case "exit":
                if len(input_list) > 1:
                    exit(int(input_list[1]))
                else:
                    exit(0)
            case "echo":
                if len(input_list) > 1:
                    echo(input_list[1:])
                else:
                    echo("")
            case "type":
                if len(input_list) > 1:
                    type_cmd(input_list[1])
            case "pwd":
                print(os.getcwd())
            case "cd":
                change_directory(input_list[1])                

def change_directory(directory: str) -> None:
    try:
        if directory == "~":
            os.chdir(os.path.expanduser("~"))
        else:
            os.chdir(directory)
    except FileNotFoundError:
        print(f"cd: {directory}: No such file or directory")
    except NotADirectoryError:
        print(f"cd: {directory}: Not a directory")
    except PermissionError:
        print(f"cd: {directory}: Permission denied")

def run_exe(executable_path, *args) -> subprocess.CalledProcessError | None:
    # print("executable_path=", executable_path)
    # print("executable_args=", args, " type=", type(*args))
    try:
        result = subprocess.run([executable_path, *args], capture_output=True, text=True, check=True)
        if result.stderr:
            print("Stderr:", result.stderr)
        else:
            sys.stdout.write(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running executable: {e}")
        print("Stdout:", e.stdout)
        print("Stderr:", e.stderr)
        raise  # Re-raise the exception after printing the error information
    except FileNotFoundError:
        print(f"Executable not found: {executable_path}")
        return None


def exit(status: int):
    if status in [0, 1]:
        sys.exit(status)


def echo(args: list):
    print(" ".join(args))


def get_command_path(command) -> str | None:
    for path in PATHS:
        for root, _, files in os.walk(path):
            # print('root=', root)
            # print('files=', files)
            if command in files:
                return os.path.join(root, command)
    return None


def type_cmd(command: str) -> str | None:
    if command in BUILTIN_COMMANDS:
        print(f"{command} is a shell builtin")
        return

    if command_path:=get_command_path(command):
        print(f"{command} is {command_path}")
    else:
        invalid_command(command)
        
def check_directory_exists_pathlib(path_str):
    """Checks if a directory exists using pathlib."""
    path = Path(path_str)
    return path.is_dir()

def extract_quoted_string(text):
    """Extracts a string enclosed in either single or double quotes."""
    match = re.search(r'["\'](.*?)["\']', text) #non-greedy match
    matches = re.findall(r'["\'](.*?)["\']', text)
    return matches if matches else None

def parse_command(command: str) -> list:
    # print("command=", command)
    temp = []
    temp.append(command.split()[0])
    temp = temp + extract_quoted_string(command)
    print("temp=", temp)
    return temp

def main():
    while True:
        sys.stdout.write("$ ")

        command = input()
        # print("actual_command:", command)
        if any(symbol in command for symbol in QUOTE_SYMBOLS):
            input_list = parse_command(command)
        else:
            input_list = command.strip().split()
        
        # print("input_list=", input_list) 
        evaluate(input_list)


if __name__ == "__main__":
    main()
