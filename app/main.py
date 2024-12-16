import sys
import os


def valid_command(command):
    valid_commands = ["exit", "echo", "type"]
    return True if command in valid_commands else False


def invalid_command(command: str):
    print(f"{command}: not found")


def evaluate(input_list: list):

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
                    type(input_list[1])


def exit(status: int):
    if status in [0, 1]:
        sys.exit(status)


def echo(args: list):
    print(" ".join(args))


def check_command_path(directory, command):
    """
    Checks all files under a given directory.

    Args:
        directory: The path to the directory.

    Prints:
        The path of each file found in the directory and its subdirectories.
    """
    # print("directory=", directory)
    # print("command=", command)

    for root, _, files in os.walk(directory):
        for file in files:
            if file == command:
                file_path = os.path.join(root, file)
                # print("file_path=", file_path)
                return file_path


def type(command: str):
    # all_vars = os.environ
    
    paths = os.environ['PATH'].split(':')
    builtin_commands = ["exit", "echo", "type"]

    # print("allvars=", all_vars)
    # print("paths=", paths)
    
    # if not valid_command(command):
    #     invalid_command(command)
    # else:

    if command in builtin_commands:
        print(f"{command} is a shell builtin")
        return

    for path in paths:
        # print("path=", path)
        # print("split=", path.split('/'))
        # print("last=", path.split('/')[-1])
        command_path = check_command_path(path, command)
        if command_path:
            print(f"{command} is {command_path}")
            return
    invalid_command(command)
        

def main():
    while True:

        # Uncomment this block to pass the first stage
        sys.stdout.write("$ ")

        # Wait for user input
        command = input()
        input_list = command.strip().split()

        # match command:
        #     case "exit":
        #         command += " 0"

        evaluate(input_list)
        

if __name__ == "__main__":
    main()
