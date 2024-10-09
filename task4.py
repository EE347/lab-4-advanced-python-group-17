def print_names_from_file():
    # Open the file in read mode
    with open('task3.txt', 'r') as file:
        # Read all lines from the file
        names = file.readlines()
   
    # Print each name
    for name in names:
        print(name.strip())  # strip() removes any extra newlines or spaces

if __name__ == '__main__':
    print_names_from_file()