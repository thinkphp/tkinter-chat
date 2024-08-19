import socket
import threading

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

clients = []

def handle_client(conn, addr):
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        for client in clients:
            if client != conn:
                client.sendall(data)
    conn.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('Server listening...')
    while True:
        conn, addr = s.accept()
        clients.append(conn)
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()
