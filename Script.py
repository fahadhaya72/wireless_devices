import os
import socket
import requests
from scapy.all import ARP, Ether, srp
import asyncio
from bleak import BleakScanner  # Replacing PyBluez with Bleak

# Get the public IP of the current WiFi network
def get_public_ip():
    try:
        response = requests.get("https://api64.ipify.org?format=json", timeout=5)
        return response.json().get("ip")
    except Exception as e:
        print(f"Error getting public IP: {e}")
        return None

# Get the local IP of the current machine
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception as e:
        print(f"Error getting local IP: {e}")
        return None

# Scan all devices connected to the WiFi network
def scan_wifi_network():
    local_ip = get_local_ip()
    if not local_ip:
        return []

    network_prefix = ".".join(local_ip.split(".")[:3]) + ".1/24"
    print(f"Scanning network: {network_prefix}")

    arp = ARP(pdst=network_prefix)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    result = srp(packet, timeout=3, verbose=False)[0]

    devices = []
    for sent, received in result:
        devices.append({
            "ip": received.psrc,  # Local IP
            "mac": received.hwsrc  # MAC Address
        })

    return devices

# Get the public IP of each connected WiFi device (if possible)
def get_device_public_ip(ip):
    try:
        response = requests.get(f"https://api64.ipify.org?format=json", headers={"X-Forwarded-For": ip}, timeout=5)
        return response.json().get("ip")
    except:
        return "Unknown"

# Scan for Bluetooth devices using Bleak
async def scan_bluetooth_devices():
    print("\nScanning for Bluetooth devices...")
    devices = await BleakScanner.discover()
    return [{"mac": device.address, "name": device.name or "Unknown"} for device in devices]

if __name__ == "__main__":
    print("\nGetting WiFi Public IP...")
    wifi_public_ip = get_public_ip()
    print(f"Your WiFi Public IP: {wifi_public_ip}\n")

    print("Scanning WiFi Network...")
    wifi_devices = scan_wifi_network()

    if not wifi_devices:
        print("No devices found on WiFi.")
    else:
        print("\nConnected WiFi Devices:")
        for device in wifi_devices:
            public_ip = get_device_public_ip(device["ip"])
            print(f"Local IP: {device['ip']}, MAC: {device['mac']}, Public IP: {public_ip}")

    print("\nScanning Bluetooth Devices...")
    bluetooth_devices = asyncio.run(scan_bluetooth_devices())

    if not bluetooth_devices:
        print("No Bluetooth devices found.")
    else:
        print("\nDiscovered Bluetooth Devices:")
        for device in bluetooth_devices:
            print(f"Name: {device['name']}, MAC: {device['mac']}")
