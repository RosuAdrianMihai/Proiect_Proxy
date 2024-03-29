import socket
import json
from actions.write import write_to_file

server_address = ('127.0.0.1', 12345)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(server_address)

action = ""
while action != "read" and action != "write":
    action = input("Write 'read' to read from a file and 'write' to write to a file: ")

file_name = input("File name: ")

try:
    data = {
        "action": action,
        "file_name": file_name,
        "content": write_to_file() if action == "write" else ""
    }

    json_data = json.dumps()

    client_socket.send(json_data)
except:
    print("Client error")
finally:
    client_socket.close()
    print("Connection closed")