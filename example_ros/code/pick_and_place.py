#! /usr/bin/env python3

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from sensor_msgs.msgs import JointState 
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()    
arm_group = moveit_commander.MoveGroupCommander("serpens_arm")
tool_group = moveit_commander.MoveGroupCommander("serpens_tool")

display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory)

def d2r(deg):
	rad = deg/180*3.14159
	return rad

while not rospy.is_shutdown():
#----------------stand by-------------
	arm_group.set_named_target("stand_by")
	plan1 = arm_group.go()

#---------------open gripper----------
	tool_group.set_named_target("end_open")
	plan2 = tool_group.go()

#--------------move to point close to object---------
	pose_target = geometry_msgs.msg.Pose()
	pose_target.orientation.x = 0.0
	pose_target.orientation.y = 0.0
	pose_target.orientation.z = 0.0
	pose_target.orientation.w = 1.0
	pose_target.position.x = 0.07
	pose_target.position.y = 0.09
	pose_target.position.z = 0.1
	arm_group.set_pose_target(pose_target)
	plan1 = arm_group.go()

#------------------approach to object----------------
	pose_target = geometry_msgs.msg.Pose()
	pose_target.orientation.x = 0.0
	pose_target.orientation.y = 0.0
	pose_target.orientation.z = 0.0
	pose_target.orientation.w = 1.0
	
	pose_target.position.z = 0.05
	arm_group.set_pose_target(pose_target)
	plan1 = arm_group.go()

#------------close gripper to pick object------------
	tool_group.set_named_target("end_close")
	plan2 = tool_group.go()

#-------------go to second point --------------------
	group_variable_values = arm_group.get_current_joint_values()
	
	group_variable_values[0] = d2r(-46)
	group_variable_values[1] = d2r(-36)
	group_variable_values[2] = d2r(30)
	group_variable_values[3] = d2r(-28)
	group_variable_values[4] = d2r(-45)
	group_variable_values[5] = d2r(0)
	
	arm_group.set_joint_value_target(group_variable_values)
	plan1 = arm_group.go()

#------------open gripper---------------------------
	tool_group.set_named_target("end_open")
	plan2 = tool_group.go()

#-------------Increase z velue-----------------------
	pose_target = geometry_msgs.msg.Pose()
	pose_target.orientation.x = 0.0
	pose_target.orientation.y = 0.0
	pose_target.orientation.z = 0.0
	pose_target.orientation.w = 1.0
	
	pose_target.position.z = pose_target.position.z+0.01
	arm_group.set_pose_target(pose_target)
	plan1 = arm_group.go()

#----------------return to home state--------------
	arm_group.set_named_target("home")
	plan1 = arm_group.go()
rospy.sleep(5)
moveit_commander.roscpp_shutdown()
