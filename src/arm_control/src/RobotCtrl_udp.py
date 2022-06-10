# -*- coding: utf-8 -*	
# !/usr/bin/env python

from __future__ import print_function
from contextlib import contextmanager   

print("importing tm robot...")

from TM_Robot import TM_Robot

from tm_msgs.msg import *
from tm_msgs.srv import *
# from cobo_msgs import *
# from cobo_msgs.srv import *

import rospy
import sys
import time
import random
import math

import socket
import struct
import numpy as np

TM = TM_Robot([])

def sample(px,py,pz,rx,ry,rz,v):

    # init = [x,y,z,rx,ry,rz]
    # TM.SetIO(0,TM.HIGH)
    # TM.Move_TM(init[0], init[1] , init[2], init[3], init[4], init[5],Move_type='PTP_J',Speed=3.0,blend_Mode = True)
    
    # init = [162.14,435.47,321.36,178.20,2.61,162.09]
    # TM.Move_TM(init[0], init[1] , init[2], init[3], init[4], init[5],Move_type='PTP_T',Speed=100.0,blend_Mode = True)
    
    TM.Move_TM(px,py,pz,rx,ry,rz,Move_type='PTP_T',Speed=v,blend_Mode = True)

if __name__ == '__main__':
    print("robot control start...")

    # set socket
    UDP_IP = "192.168.1.71"
    UDP_PORT = 8777
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))
    print("socket start...")
    print("UDP target IP: %s" % UDP_IP)
    print("UDP target port: %s" % UDP_PORT)
    point = np.zeros(7,np.float32) # px,py,pz,rx,ry,rz,v

    try:
        # ros node
        rospy.init_node('queue_tag_demo', disable_signals=True)
        TM.Run()

        while 1:
            # socket read
            data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
            print("received message: %s" % data)
            try:
                for i in range(7):
                    point[i] = struct.unpack('f', data[i*4:i*4+4])[0]
                print(point)
            except:
                print("data error...")
            
            # robot move
            sample(point[0],point[1],point[2],point[3],point[4],point[5],point[6])
        # rospy.spin()
    except KeyboardInterrupt as e:
        print("Shutdown")