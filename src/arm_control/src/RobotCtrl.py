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



TM = TM_Robot([])

def sample():

    # init = [x,y,z,rx,ry,rz]
    # TM.SetIO(0,TM.HIGH)
    # TM.Move_TM(init[0], init[1] , init[2], init[3], init[4], init[5],Move_type='PTP_J',Speed=3.0,blend_Mode = True)
    
    init = [302.228,504.204,64.892,-180,0,90]
    init2 = [302.226,204.198,64.892,-180,0,90]


    TM.Move_TM(init[0], init[1] , init[2], init[3], init[4], init[5],Move_type='PTP_T',Speed=100.0,blend_Mode = True)
    TM.Move_TM(init2[0], init2[1] , init2[2], init2[3], init2[4], init2[5],Move_type='PTP_T',Speed=100.0,blend_Mode = True)



if __name__ == '__main__':
    print("robot control start...")
    try:
        rospy.init_node('queue_tag_demo', disable_signals=True)
        TM.Run()
        sample()
        # rospy.spin()
    except KeyboardInterrupt as e:
        print("Shutdown")