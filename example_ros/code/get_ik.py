#! /usr/bin/env python3

import sys
import copy
import rospy
import moveit_commander
from moveit_msgs.msg import RobotState, Constraints, PositionIKRequest
from moveit_msgs.srv import GetPositionIK
from std_msgs.msg import Header
from geometry_msgs.msg import PoseStamped

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('get_ik', anonymous=True)

arm = moveit_commander.MoveGroupCommander('serpens_arm')
robot = moveit_commander.RobotCommander()
rospy.wait_for_service('compute_ik')

try:
  moveit_ik = rospy.ServiceProxy('compute_ik', GetPositionIK)
except rospy.ServiceException:
  rospy.logerror("Service call failed: %s"%e)

ps = PoseStamped()
ps.pose.position.x = 0.1
ps.pose.position.y = 0.08
ps.pose.position.z = 0.05
ps.pose.orientation.x = 0
ps.pose.orientation.y = 0
ps.pose.orientation.z = 0
ps.pose.orientation.w = 1
ps.header.frame_id = "base_link"

req = PositionIKRequest()
req.group_name = "serpens_arm"
req.pose_stamped = ps
req.robot_state = robot.get_current_state()
req.avoid_collisions = False
req.ik_link_name = arm.get_end_effector_link()
req.timeout = rospy.Duration(10)
#req.attempts = 0

resp = moveit_ik(req)
print(resp)
