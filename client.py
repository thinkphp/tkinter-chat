import socket
import tkinter as tk
import threading  # Added import statement

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

def send_message():
    message = text_box.get()
    text_box.delete(0, tk.END)
    client_socket.sendall(message.encode())

root = tk.Tk()
text_box = tk.Entry(root)
text_box.pack()
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()
receive_box = tk.Text(root)
receive_box.pack()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

def receive_messages():
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        receive_box.insert(tk.END, data.decode() + '\n')

receive_thread = threading.Thread(target=receive_messages)
receive_thread.daemon = True
receive_thread.start()

root.mainloop()
