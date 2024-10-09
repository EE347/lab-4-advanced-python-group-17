
import csv

def write_names_to_csv():
    # Open the CSV file in append mode
    with open('task5.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
       
        while True:
            # Ask for the user's name
            name = input("Enter a name (or type 'quit' to stop): ")
           
            # Check if the user wants to quit
            if name.lower() == 'quit':
                break
           
            # Write the name to the CSV file
            writer.writerow([name])

def read_names_from_csv():
    # Open the CSV file in read mode
    with open('task5.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
       
        # Print each name from the file
        for row in reader:
            if row:
                print(row[0])

if __name__ == '__main__':
    # Write names to the CSV file
    write_names_to_csv()
   
    # Read and print the names from the CSV file
    print("\nNames stored in the file:")
    read_names_from_csv()