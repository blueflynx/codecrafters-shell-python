import sys

def exit(status):
    if status in [0, 1]:
        sys.exit(status)

def echo(args: list):
    print(" ".join(args))


def main():
    valid_commands = ["exit"]

    while True:

        # Uncomment this block to pass the first stage
        sys.stdout.write("$ ")

        # Wait for user input
        command = input().strip().split()

        # match command:
        #     case "exit":
        #         command += " 0"

        if command[0] not in valid_commands:
            print(f"{command}: not found")
        else:
            match command[0]:
                case "exit":
                    exit(command[1])
                case "echo":
                    echo(command[1:])

if __name__ == "__main__":
    main()
