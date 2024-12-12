import sys

def main():
    valid_commands = []

    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")

    # Wait for user input
    command = input()

    if command not in valid_commands:
        print(f"{command}: not found")

if __name__ == "__main__":
    main()
