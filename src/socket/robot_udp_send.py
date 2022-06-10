
# py3
import socket
import numpy as np
import struct

UDP_IP = "192.168.1.71"
UDP_PORT = 8787

point = np.zeros(7,np.float32) # px,py,pz,rx,ry,rz,v
point = [162.14,435.47,321.36,178.20,2.61,162.09,100]
point = [-157.09,435.93,317.14,179.01,2.37,162.09,100]
message = b""
for i in range(7):
    message += struct.pack('f', point[i])

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % message)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock.sendto(message, (UDP_IP, UDP_PORT))