import os

def read_from_file(file_name):
    try:
        with open(f"{os.getcwd()}\\files\\{file_name}", "r") as file:
           return file.read() 
    except Exception as e:
        print(e)
        return f"Error reading from {file_name}"