import socket
import modules.portScan as portScan



hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
scanner = portScan.PortScanner(ip_address)

ports = scanner.portscan(1,1000,"openPorts.txt")


print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")
print(f"ports: {ports}")