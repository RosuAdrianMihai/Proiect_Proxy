import socket

server_address= ('127.0.0.1', 12345)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(server_address)

server_socket.listen(3)

print(f"Waiting for connection {server_address}")

while True:
    connection, client_address = server_socket.accept()

    try:
        json_data = connection.recv(1024)
        print(json_data)
    except:
        print("Server error")
    finally:
        connection.close()
        print("Connection closed")