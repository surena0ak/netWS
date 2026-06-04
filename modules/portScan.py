import socket
import threading 
import time


class PortScanner:
    def __init__(self,target):
        self.target = target
        self.progress = 0
        
    def portscan(self, first_port, last_port, save_file_name, time_out,task_count): # its get start and end port and store in test file 
        openPorts = []
        def scan_port (task_name, strat_port, end_port):
            #print(f"task {task_name} is scanning ports from {strat_port} to {end_port}")
            for port in range(int(strat_port), int(end_port) + 1):
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sk:
                    sk.settimeout(1)
                    result = sk.connect_ex((self.target, port))
                    
                    if result == 0 :
                        openPorts.append(port)   
                        self.progress = (port - first_port + 1) / (last_port - first_port + 1) * 100
                        #print(f"task {task_name} - Progress: {self.progress:.2f}% - Port {port} is open")               

        
        tasks=[]
        port_step = last_port/task_count
        for step in range(task_count): 
            tasks.append(threading.Thread(target=scan_port, args=(f"Task {step}", port_step*step, port_step*(step+1))))     
            
            
        for t in tasks:
            t.start()
            
        for t in tasks:
            t.join()
            
        # with open (save_file_name , 'a') as file:  
        #     for port in openPorts:
        #         file.write(f"port : {port} is in use \n")     
            

                    
                    
        return openPorts
                