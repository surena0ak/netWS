import socket
import modules.portScan as portScan


hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
scanner = portScan.PortScanner(ip_address)

ports = scanner.portscan(1,65535,"openPorts.txt",2, 1000)


print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")
print(f"ports: {ports}")