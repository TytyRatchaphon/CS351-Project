import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 5555))

    # Receive and print the server's initial response
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Server response: {response}")

    while True:
        # User input to send a message to the server
        message = input("Enter your message (type 'bye' to disconnect): ")
        client_socket.send(message.encode('utf-8'))

        if message.lower() == 'bye':
            print("Disconnected from the server.")
            break

        # Receive and print the server's response
        server_response = client_socket.recv(1024).decode('utf-8')
        print(f"Server response: {server_response}")

    client_socket.close()

if __name__ == "__main__":
    start_client()
