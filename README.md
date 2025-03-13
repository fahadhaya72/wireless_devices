# wireless_devices
Network and Bluetooth Scanner

Overview

This Python script scans for:

WiFi Devices: Detects all devices connected to the same WiFi network and attempts to retrieve their public IP addresses.

Bluetooth Devices: Scans for nearby Bluetooth devices using Bleak.

Features

✅ Retrieve your WiFi network's public IP.✅ Scan and list all connected WiFi devices (IP & MAC Address).✅ Attempt to retrieve each device's public IP address.✅ Scan for Bluetooth devices in range.✅ Works on Windows, Linux, and macOS.

Installation

1️⃣ Install Python (if not already installed)

Make sure you have Python 3.x installed. You can download it from python.org.

2️⃣ Install Dependencies

Run the following command to install the required libraries:

pip install -r requirements.txt

Or install them manually:

pip install scapy bleak requests

Usage

Run the script using:

python network_scanner.py

Expected Output

Getting WiFi Public IP...
Your WiFi Public IP: 192.168.X.X

Scanning WiFi Network...
Connected WiFi Devices:
Local IP: 192.168.X.10, MAC: XX:XX:XX:XX:XX:XX, Public IP: 34.56.78.90
...

Scanning Bluetooth Devices...
Discovered Bluetooth Devices:
Name: Headphones, MAC: XX:XX:XX:XX:XX:XX
...

Notes

Administrator/root privileges may be required for network scanning.

Bluetooth scanning uses Bleak, a cross-platform Bluetooth library.

License

This project is licensed under the MIT License.

📌 Created by FHD 🚀
