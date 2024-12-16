import sys

def evaluate(command: list):

    valid_commands = ["exit", "echo", "type"]

    if command[0] not in valid_commands:
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
                    type(command[1], valid_commands)

def type(command: str, valid_commands: list):
    if command in valid_commands:
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
