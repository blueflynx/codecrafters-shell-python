import sys

def main():
    valid_commands = ["exit 0"]

    while True:

        # Uncomment this block to pass the first stage
        sys.stdout.write("$ ")

        # Wait for user input
        command = input().strip()

        match command:
            case "exit":
                command += " 0"

        if command not in valid_commands:
            print(f"{command}: not found")
        else:
            match command:
                case "exit 0":
                    break

if __name__ == "__main__":
    main()
