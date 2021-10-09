import rospy
from tm_msgs.msg import *
from tm_msgs.srv import *
import math
import time



class TM_Robot():

    HIGH = 'HIGH'
    LOW = 'LOW'
    
    rospy.wait_for_service('tm_driver/set_positions')
    rospy.wait_for_service('tm_driver/set_event')
    rospy.wait_for_service('tm_driver/set_io')
    set_event = rospy.ServiceProxy('tm_driver/set_event', SetEvent)
    set_positions = rospy.ServiceProxy('tm_driver/set_positions', SetPositions)
    set_io = rospy.ServiceProxy('tm_driver/set_io', SetIO)


    def __init__(self, pose):
        self.Init_Pose = pose

    def callback(data):
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

    def Run(self):
        print('run')
        rospy.Subscriber('tm_driver/sta_response', StaResponse, self.callback)
        # rospy.Subscriber('feedback_states',FeedbackState,self.State_callback)

    def Move_TM(self,x,y,z,rx,ry,rz,Move_type = 'PTP_T',Speed = 1.0,blend_Mode = True,tag = -1):
        blend_percent = 0
        if(blend_Mode == True):
            blend_percent = 100
        if(Move_type == 'PTP_J'):
            print('Send J')
            print([x,y,z,rx,ry,rz])
            S_x = (x / 180.0) * math.pi
            S_y = (y / 180.0) * math.pi
            S_z = (z / 180.0) * math.pi
            
            rad_Rx = (rx / 360.0) * 2 * math.pi
            rad_Ry = (ry / 360.0) * 2 * math.pi
            rad_Rz = (rz / 360.0) * 2 * math.pi
        else:
            S_x = x / 1000.0
            S_y = y / 1000.0
            S_z = z / 1000.0
            
            rad_Rx = (rx / 360.0) * 2 * math.pi
            rad_Ry = (ry / 360.0) * 2 * math.pi
            rad_Rz = (rz / 360.0) * 2 * math.pi


        p = [S_x,S_y,S_z,rad_Rx,rad_Ry,rad_Rz]
            
        print(p)
        if(Move_type == 'LINE_T'):
            state = self.set_positions(SetPositionsRequest.LINE_T, p,Speed, 0.5, blend_percent, True)
            # pass
        elif(Move_type == 'PTP_T'):
            state = self.set_positions(SetPositionsRequest.PTP_T, p,Speed, 0.5, 100, True)
            # pass

        elif(Move_type == 'PTP_J'):
            state = self.set_positions(SetPositionsRequest.PTP_J, p,Speed, 0.5, 100, True)

        if(tag != -1):
                # print('Set tag id : ',tag)
                self.set_event(SetEventRequest.TAG, tag, 0)
   
    def SetIO(self,pin,state = 'HIGH'):
        # print('Set IO : ',pin)
        set_state = SetIORequest.STATE_OFF
        if(state == 'HIGH'):
            set_state = SetIORequest.STATE_ON
        self.set_io(SetIORequest.MODULE_ENDEFFECTOR,SetIORequest.TYPE_DIGITAL_OUT,pin,set_state)
        
        # print('Set Done')

    def spinWait(self,tag_id,Time = 0):
        print('Set tag ',tag_id)
        print('-------------Start------------------------')
        self.set_event(SetEventRequest.TAG, tag_id, 0)
        self.wait_tag = tag_id
        while(1):
            if(self.Wait_Done == True):
                if(int(self.tag_feedback) == tag_id):
                    # print('Start Wiat Time : ',Time)
                    time.sleep(Time)
                    # print('Wait Time Finish')
                    print('-------------End------------------------')
                    break
                self.tag_feedback = -1
                self.Wait_Done  = False
            else:
                pass

    def Stop_TM(self):
        self.set_event(SetEventRequest.STOP,0,0)

                    
    