import json
from uuid import uuid4

def handle_client_request(client_socket, server_socket, data, connections_map):
    identifier = str(uuid4())
    connections_map[identifier] = client_socket

    print(f"Connection created with identifier: {identifier}")

    sent_data = {
        "identifier": identifier,
        **data
    }

    server_socket.sendall((json.dumps(sent_data)).encode())