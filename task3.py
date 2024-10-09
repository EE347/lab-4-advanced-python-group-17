def add_name_to_file():
    # Ask for the user's name
    name = input("Enter your name: ")

    # Open the file in append mode
    with open('task3.txt', 'a') as file:
        # Write the name to the file followed by a newline character
        file.write(name + '\n')

if __name__ == '__main__':
    # Add names three times
    for _ in range(3):
        add_name_to_file()