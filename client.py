import socket
import cv2
import pickle
import struct

SERVER_IP = input("Enter server IP: ")
PORT = 9999

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, PORT))

data = b""
payload_size = struct.calcsize("Q")

print("[+] Connected to server")

try:
    while True:
        while len(data) < payload_size:
            packet = client_socket.recv(4096)
            if not packet:
                break
            data += packet

        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("Q", packed_msg_size)[0]

        while len(data) < msg_size:
            data += client_socket.recv(4096)

        frame_data = data[:msg_size]
        data = data[msg_size:]

        buffer = pickle.loads(frame_data)
        frame = cv2.imdecode(buffer, cv2.IMREAD_COLOR)

        cv2.imshow("Remote Screen", frame)

        if cv2.waitKey(1) == 27:
            break

except Exception as e:
    print("[-] Error:", e)

client_socket.close()
cv2.destroyAllWindows()