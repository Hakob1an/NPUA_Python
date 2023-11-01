import os

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"Content of '{file_name}':\n{content}")
            return content
    except FileNotFoundError:
        print(f"File '{file_name}' doesn't exist. Please enter a valid filename.")
        return None

def write_to_file(file_name, content):
    try:
        with open(file_name, 'w') as file:
            file.write(content)
            print(f"Content has been written to '{file_name}' successfully.")
    except Exception as e:
        print(f"Error writing to file: {e}")

if __name__ == "__main__":
    file_name = input("Enter the name of the text file you want to open: ")
    
    file_content = read_file(file_name)
    
    if file_content is not None:
        write_option = input("Do you want to write to this file? (yes/no): ").lower()
        if write_option == "yes":
            write_to_file(file_name, file_content)
        elif write_option == "no":
            new_file_name = input("Enter the new file name to write: ")
            new_content = input("Enter the content to write: ")
            write_to_file(new_file_name, new_content)
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
