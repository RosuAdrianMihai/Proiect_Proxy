import socket
import json
from controllers.write import write_to_file
from controllers.read import read_from_file

server_address= ('127.0.0.1', 12345)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(server_address)

server_socket.listen(3)

print(f"Waiting for connection {server_address}")

while True:
    connection, client_address = server_socket.accept()

    try:
        json_data = connection.recv(1024).decode()
        data = json.loads(json_data)
        
        response = write_to_file(data["file_name"], data["content"]) if data["action"] == "write" else read_from_file(data["file_name"])

        connection.sendall(response.encode())
        
        print(f"Sent:\n{response}")
    except:
        print("Server error")
    finally:
        connection.close()
        print("Connection closed")