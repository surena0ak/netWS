import socket


class PortScanner:
    def __init__(self,target):
        self.target = target
        self.progress = 0
        
    def portscan(self, first_port, last_port, save_file_name): # its get start and end port and store in test file 
        openPorts = []
        for port in range(first_port,last_port+1):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sk:
                sk.settimeout(1)
                result = sk.connect_ex((self.target, port))
                
                if result == 0 :
                    openPorts.append(port)                  
                    with open (save_file_name, 'a') as file:  
                        file.write(f"port : {port} is in use \n")
            
            self.progress = (port - first_port + 1) / (last_port - first_port + 1) * 100
            print(self.progress)
                    
        return openPorts
                