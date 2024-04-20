import json

def handle_server_response(server_socket, connections_map):
    while True:
        json_data = server_socket.recv(1024).decode()

        if not json_data:
            break
    
        data = json.loads(json_data)

        identifier = data["identifier"]
        client_socket = connections_map[identifier]

        client_socket.sendall(json_data.encode())

        print(f"Data sent to the client with the identifier: {identifier}")