import socket
import threading
from lib.handle_client_request import handle_client_request
from lib.handle_server_response import handle_server_response

connections_map = {}

def handle_connection(client_socket, server_address):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(server_address)

    client_to_server = threading.Thread(target=handle_client_request, args=(client_socket, server_socket, connections_map))
    server_to_client = threading.Thread(target=handle_server_response, args=(server_socket, connections_map))

    client_to_server.start()
    server_to_client.start()

    client_to_server.join()
    server_to_client.join()

    client_socket.close()
    server_socket.close()

server_address = ('127.0.0.1', 8080)
proxy_address = ('127.0.0.1', 9090)

proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
proxy_socket.bind(proxy_address)
proxy_socket.listen(3)

print(f"Proxy server running on {proxy_address}")

while True:
    connection, client_address = proxy_socket.accept()

    try:
        proxy_thread = threading.Thread(target=handle_connection, args=(connection, server_address))
        proxy_thread.start()
    except:
        print("Proxy error")