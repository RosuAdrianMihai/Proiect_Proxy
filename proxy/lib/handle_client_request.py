import json
from uuid import uuid4

def handle_client_request(client_socket, server_socket, connections_map):
    identifier = str(uuid4())
    connections_map[identifier] = client_socket

    print(f"Connection created with identifier: {identifier}")

    while True:
        json_data = client_socket.recv(1024).decode()

        if not json_data:
            break

        data = json.loads(json_data)

        data["identifier"] = identifier
        data = json.dumps(data)

        server_socket.sendall(data.encode())