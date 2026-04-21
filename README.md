# 🖥️ Python Remote Desktop (LAN)

A simple remote desktop application built using Python sockets that streams the host machine’s screen to a client over a local network (LAN).

---

## 🚀 Features

* 📡 Real-time screen streaming
* 🌐 Works over Local Area Network (WiFi/LAN)
* ⚡ Lightweight and easy to run
* 🧠 Beginner-friendly implementation

---

## 📦 Requirements

Install dependencies using:

```bash
pip install opencv-python numpy pyautogui pillow
```

Or use a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate   # Windows
pip install opencv-python numpy pyautogui pillow
```

---

## 📁 Project Structure

```
remote-desktop-python/
├── server.py      # Host machine (screen sender)
├── client.py      # Viewer machine (screen receiver)
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

### 🖥️ Step 1: Start Server (Host)

Run on the machine you want to share:

```bash
python server.py
```

You will see output like:

```
[+] Server started
[+] Connect using IP: 192.168.1.5:9999
```

---

### 💻 Step 2: Start Client (Viewer)

Run on another device in the same network:

```bash
python client.py
```

Enter the IP shown on the server:

```
192.168.1.5
```

---

## ⚠️ Limitations

* ❌ Works only on same network (LAN)
* ❌ No encryption (not secure for public use)
* ❌ No mouse/keyboard control
* ❌ Basic compression (may have lag)

---

## 🛠️ Future Improvements

* 🎮 Add mouse and keyboard control
* 🔐 Add encryption for secure communication
* 🌍 Enable internet-based connection
* ⚡ Optimize performance and reduce latency
* 🖥️ Add GUI interface

---

## 🧠 How It Works

* Server captures screen using `pyautogui`
* Frames are compressed using `OpenCV`
* Data is sent via TCP sockets
* Client receives, decodes, and displays frames in real time


---

## 📄 License

This project is open-source and available under the MIT License.

