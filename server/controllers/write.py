import os

def write_to_file(file_name, content):
    try: 
        with open(f"{os.getcwd()}\\files\\{file_name}", "w") as file:
            file.write(content)

        return f"The content was successfully written to {file_name}"
    except Exception as e:
        print(e)
        return f"Error writing to {file_name}"