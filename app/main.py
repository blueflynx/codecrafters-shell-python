import sys
import os

def valid_command(command):
    valid_commands = ["exit", "echo", "type", "ls", "abcd"]

    return True if command in valid_commands else False

def evaluate(command: list):

    

    if not valid_command(command[0]):
            invalid_command("".join(command[0]))
    else:
        match command[0]:
            case "exit":
                if len(command) > 1:
                    exit(int(command[1]))
                else:
                    exit(0)
            case "echo":
                if len(command) > 1:
                    echo(command[1:])
                else:
                    echo("")
            case "type":
                if len(command) > 1:
                    type(command[1])

def type(command: str):
    all_vars = os.environ
    paths = os.environ['PATH'].split(':')

    print("allvars=", all_vars)
    print("paths=", paths)
    
    if valid_command(command):
        for path in paths:
            # print("path=", path)
            # print("split=", path.split('/'))
            # print("last=", path.split('/')[-1])
            if command[-1] == path.split('/')[-1]:
                print(f"{command} is {path}")
                return
        print(f"{command} is a shell builtin")
    else:
        invalid_command(command)

def invalid_command(command: str):
    print(f"{command}: not found")

def exit(status: int):
    if status in [0, 1]:
        sys.exit(status)

def echo(args: list):
    print(" ".join(args))


def main():
    while True:

        # Uncomment this block to pass the first stage
        sys.stdout.write("$ ")

        # Wait for user input
        command = input().strip().split()

        # match command:
        #     case "exit":
        #         command += " 0"

        evaluate(command)
        

if __name__ == "__main__":
    main()
