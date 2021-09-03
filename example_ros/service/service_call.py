#!/usr/bin/env python3

import rospy
from std_srvs.srv import SetBool

rospy.init_node('service_client_test')

def call():

    rospy.wait_for_service('toggle_status')
    try:
       srv = rospy.ServiceProxy('toggle_status', SetBool)
       response = srv(True)
       return(response)
    except rospy.ServiceException as e:
       print('Service call failed: %s'%e)

res = call()

print('Finish :',res)
