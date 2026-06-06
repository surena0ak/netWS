import socket
import modules.portScan as portScan
import modules.userScan as userScan



host_name = socket.gethostname()
ip_address = socket.gethostbyname(host_name)
scanner = portScan.PortScanner(ip_address)

ports = scanner.portscan(1, 65535, "openPorts.txt" ,2 ,1000)

print(F"user scanning for port {135} used by : {userScan.scan_users(135)}")

print(f"Hostname: {host_name}")
print(f"IP Address: {ip_address}")
print(f"ports: {ports}")