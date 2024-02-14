import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 5555))
    server_socket.listen(5)

    print("Server listening on port 5555...")

    client_socket, addr = server_socket.accept()
    print(f"Accepted connection from {addr}")

    # Send a success status code (200 OK) to the client
    success_message = "Hi, This is appeal system.       200 OK - Connection successful"
    client_socket.send(success_message.encode('utf-8'))

    while True:
        # Receive message from the client
        message = client_socket.recv(1024).decode('utf-8')
        print(f"Received message: {message}")

        if message.lower() == 'bye':
            print("Client disconnected.")
            break

        # Send a response back to the client
        response = input("Enter your response: ")
        client_socket.send(response.encode('utf-8'))

    client_socket.close()

if __name__ == "__main__":
    start_server()
