__author__ = 'Kozlova Ekaterina'

def strToSock(ip_addr):
    try:
        ip_addr = ip_addr.split(':')
        return ip_addr[0], ip_addr[1]
    except Exception:
        return "Error"

strToSock.test = [
        { 'in': ("192.168.77.2:80"), 'grade': 3 },
        { 'in': ("192.168.77.2:8000"), 'grade': 3 },
        { 'in': ("error"), 'grade': 2 },
        { 'in': ['192.168.177.2:7080'], 'grade': 2}
]