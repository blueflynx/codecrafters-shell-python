import sys

def main():
    valid_commands = []

    while True:

        # Uncomment this block to pass the first stage
        sys.stdout.write("$ ")

        # Wait for user input
        command = input()

        if command not in valid_commands:
            print(f"{command}: not found")
        else:
            match command:
                case "exit":
                    break

if __name__ == "__main__":
    main()
