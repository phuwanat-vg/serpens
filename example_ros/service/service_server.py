#!/usr/bin/env python3

import rospy

from std_srvs.srv import SetBool, SetBoolResponse

def turn_on_off(status):
    message = 'status :OFF'
    if status.data:
      message = 'status : ON'
    else:
      message = 'status : OFF'
      
    return SetBoolResponse(True,message)

rospy.init_node('service_server')

service=rospy.Service('toggle_status',SetBool, turn_on_off)
print("start service server")
rospy.spin()
