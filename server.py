import socket
import cv2
import pickle
import struct
import pyautogui
import numpy as np

HOST = "0.0.0.0"
PORT = 9999

# 🔥 Get local IP (LAN IP)
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

# Alternative (more reliable for some systems)
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    local_ip = s.getsockname()[0]
    s.close()
except:
    pass

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"[+] Server started")
print(f"[+] Connect using IP: {local_ip}:{PORT}")
print(f"[+] Waiting for connection...")

conn, addr = server_socket.accept()
print(f"[+] Connected by {addr}")

try:
    while True:
        # Capture screen
        img = pyautogui.screenshot()
        frame = np.array(img)

        # Compress frame
        _, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 50])

        data = pickle.dumps(buffer)
        message = struct.pack("Q", len(data)) + data

        conn.sendall(message)

except Exception as e:
    print("[-] Error:", e)

conn.close()
server_socket.close()