import psutil

def scan_users(port):
    user =[]
    for conn in psutil.net_connections():
        if conn.laddr.port == port:
            try:
                user.append(psutil.Process(conn.pid).username())
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
    return user
    