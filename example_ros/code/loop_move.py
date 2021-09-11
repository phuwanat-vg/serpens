#! /usr/bin/env python3

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()    
group = moveit_commander.MoveGroupCommander("serpens_arm")
tool_group = moveit_commander.MoveGroupCommander("serpens_tool")

display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory)

def d2r(deg):
	rad = deg/180*3.14159
	return rad

while not rospy.is_shutdown():
	
	#enter code for looping
	group.set_named_target("stand_by")
	plan1 = group.go()
	group.set_named_target("motion1")
	plan1 = group.go()
	
	group_variable_values = group.get_current_joint_values()
	group_variable_values[0] = d2r(30)
	group_variable_values[1] = d2r(-50)
	group_variable_values[2] = d2r(60)
	group_variable_values[3] = d2r(0)
	group_variable_values[4] = d2r(30)
	group_variable_values[5] = d2r(45)
	
	group.set_joint_value_target(group_variable_values)
	plan1 = group.go()
	pose_target = geometry_msgs.msg.Pose()
	
	
	pose_target.orientation.x = 0.0
	pose_target.orientation.y = 0.0
	pose_target.orientation.z = -0.271
	pose_target.orientation.w = 0.963
	pose_target.position.x = 0.1
	pose_target.position.y = 0.0
	pose_target.position.z = 0.1
	group.set_pose_target(pose_target)
	
	plan1 = group.go()
	
	rospy.sleep(5)
moveit_commander.roscpp_shutdown()
