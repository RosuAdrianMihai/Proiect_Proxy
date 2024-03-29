def read_from_file(file_name):
    try:
        with open(f"../files/{file_name}", "r") as file:
           return file.read() 
    except:
        return f"Error reading from {file_name}"