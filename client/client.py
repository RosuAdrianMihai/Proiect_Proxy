import socket
import json
from actions.write import write_to_file

server_address = ('127.0.0.1', 8080)
proxy_address = ('127.0.0.1', 9090)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(proxy_address)

action = ""
while action != "read" and action != "write":
    action = input("Write 'read' to read from a file and 'write' to write to a file: ")

file_name = input("File name: ")

try:
    data = {
        "action": action,
        "file_name": file_name,
        "content": write_to_file() if action == "write" else "",
        "server_address": server_address
    }

    json_data = json.dumps(data)
    client_socket.sendall(json_data.encode())

    json_result = client_socket.recv(1024).decode()
    result = json.loads(json_result)["result"]

    print(f"Received:\n{result}")
except:
    print("Client error")
finally:
    client_socket.close()
    print("Connection closed")