def write_to_file(file_name, content):
    try: 
        with open(f"../files/{file_name}", "w") as file:
            file.write(content)

        return f"The content was successfully written to {file_name}"
    except:
        return f"Error writing to {file_name}"