#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'moveit_gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import rospy
from geometry_msgs.msg import Pose
import sys
import copy
import moveit_commander
import moveit_msgs.msg
from sensor_msgs.msg import JointState


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(596, 262)
        MainWindow.setMinimumSize(QtCore.QSize(596, 262))
        MainWindow.setMaximumSize(QtCore.QSize(596, 262))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buttMove = QtWidgets.QPushButton(self.centralwidget)
        self.buttMove.setGeometry(QtCore.QRect(20, 150, 141, 61))
        self.buttMove.setObjectName("buttMove")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 50, 121, 89))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.inX = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.inX.setObjectName("inX")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.inX)
        self.inY = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.inY.setObjectName("inY")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.inY)
        self.inZ = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.inZ.setObjectName("inZ")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.inZ)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(200, 50, 111, 142))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lblTheta1 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.lblTheta1.setObjectName("lblTheta1")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lblTheta1)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lblTheta2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.lblTheta2.setObjectName("lblTheta2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lblTheta2)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lblTheta3 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.lblTheta3.setObjectName("lblTheta3")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lblTheta3)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lblTheta4 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.lblTheta4.setObjectName("lblTheta4")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lblTheta4)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lblTheta5 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.lblTheta5.setObjectName("lblTheta5")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lblTheta5)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lblTheta6 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.lblTheta6.setObjectName("lblTheta6")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lblTheta6)
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(320, 50, 64, 134))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_16 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_16.setObjectName("label_16")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.label_17 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_17.setObjectName("label_17")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.label_18 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_18.setObjectName("label_18")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.label_19 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_19.setObjectName("label_19")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.label_20 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_20.setObjectName("label_20")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.label_21 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_21.setObjectName("label_21")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(410, 50, 151, 141))
        self.groupBox.setObjectName("groupBox")
        self.buttOpen = QtWidgets.QPushButton(self.groupBox)
        self.buttOpen.setGeometry(QtCore.QRect(30, 70, 89, 25))
        self.buttOpen.setObjectName("buttOpen")
        self.buttClose = QtWidgets.QPushButton(self.groupBox)
        self.buttClose.setGeometry(QtCore.QRect(30, 110, 89, 25))
        self.buttClose.setObjectName("buttClose")
        self.lblGripperStatus = QtWidgets.QLabel(self.groupBox)
        self.lblGripperStatus.setGeometry(QtCore.QRect(10, 30, 131, 20))
        self.lblGripperStatus.setObjectName("lblGripperStatus")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 596, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.buttMove.clicked.connect(self.moveRobot)
        self.buttOpen.clicked.connect(self.openGripper)
        self.buttClose.clicked.connect(self.closeGripper)
       
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ROS Moveit Controller Interface"))
        self.buttMove.setText(_translate("MainWindow", "Move to point"))
        self.label_2.setText(_translate("MainWindow", "y"))
        self.label_3.setText(_translate("MainWindow", "z"))
        self.label.setText(_translate("MainWindow", "x"))
        self.label_4.setText(_translate("MainWindow", "Theta1"))
        self.lblTheta1.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "Theta2"))
        self.lblTheta2.setText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "Theta3"))
        self.lblTheta3.setText(_translate("MainWindow", "0"))
        self.label_7.setText(_translate("MainWindow", "Theta4"))
        self.lblTheta4.setText(_translate("MainWindow", "0"))
        self.label_8.setText(_translate("MainWindow", "Theta5"))
        self.lblTheta5.setText(_translate("MainWindow", "0"))
        self.label_9.setText(_translate("MainWindow", "Theta6"))
        self.lblTheta6.setText(_translate("MainWindow", "0"))
        self.label_16.setText(_translate("MainWindow", "degrees"))
        self.label_17.setText(_translate("MainWindow", "degrees"))
        self.label_18.setText(_translate("MainWindow", "degrees"))
        self.label_19.setText(_translate("MainWindow", "degrees"))
        self.label_20.setText(_translate("MainWindow", "degrees"))
        self.label_21.setText(_translate("MainWindow", "degrees"))
        self.groupBox.setTitle(_translate("MainWindow", "Gripper control"))
        self.buttOpen.setText(_translate("MainWindow", "OPEN"))
        self.buttClose.setText(_translate("MainWindow", "CLOSE"))
        self.lblGripperStatus.setText(_translate("MainWindow", "GRIPPER CLOSED"))
        
    def moveRobot(self):
    	print("Ready to move")
    	x = float(self.inX.text()) 
    	y = float(self.inY.text())
    	z = float(self.inZ.text()) 
    	print("goal point x:{} y:{} z:{}".format(x,y,z))
    	
    	moveit.go_from_pose(x,y,z)
    	
    def displayJoint(self,theta1,theta2,theta3,theta4,theta5,theta6):
    	self.lblTheta1.setText(str(round(theta1*180/3.14159,2)))
    	self.lblTheta2.setText(str(round(theta2*180/3.14159,2)))
    	self.lblTheta3.setText(str(round(theta3*180/3.14159,2)))
    	self.lblTheta4.setText(str(round(theta4*180/3.14159,2)))
    	self.lblTheta5.setText(str(round(theta5*180/3.14159,2)))
    	self.lblTheta6.setText(str(round(theta6*180/3.14159,2)))
    
    def openGripper(self):
    	moveit.go_from_name(1)
    	self.lblGripperStatus.setText("GRIPPER OPENED")
    
    def closeGripper(self):
    	moveit.go_from_name(0)
    	self.lblGripperStatus.setText("GRIPPER CLOSED")
    	
    	
class robotArm(object):
    def __init__(self):
    	moveit_commander.roscpp_initialize(sys.argv)
    	rospy.init_node('move_group_python_interface_tutorial', anonymous=True)
    	self.robot = moveit_commander.RobotCommander()
    	self.scene = moveit_commander.PlanningSceneInterface()    
    	self.arm_group = moveit_commander.MoveGroupCommander("serpens_arm")
    	self.tool_group = moveit_commander.MoveGroupCommander("serpens_tool")
    	self.display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
    	moveit_msgs.msg.DisplayTrajectory)
    	self.sub_joint_state = rospy.Subscriber("/joint_states",JointState, self.jointStateCb)
    	
    def go_from_pose(self,x,y,z):
    	pose_target = Pose()
    	pose_target.orientation.w = 1.0
    	pose_target.position.x = x
    	pose_target.position.y = y
    	pose_target.position.z = z
    	self.arm_group.set_pose_target(pose_target)
    	plan1 = self.arm_group.go()
    	
    def go_from_name(self,toggle):
    	if toggle ==1:
    		self.tool_group.set_named_target("end_open")
    		plan2 = self.tool_group.go()
    	else:
    		self.tool_group.set_named_target("end_close")
    		plan2 = self.tool_group.go()
    
    def jointStateCb(self,joint_value):
    	theta1 = joint_value.position[0]
    	theta2 = joint_value.position[1]
    	theta3 = joint_value.position[2]
    	theta4 = joint_value.position[3]
    	theta5 = joint_value.position[4]
    	theta6 = joint_value.position[5]
    
    	ui.displayJoint(theta1,theta2,theta3,theta4,theta5,theta6)
    	return theta1,theta2,theta3,theta4,theta5,theta6
     
    	



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    moveit = robotArm()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
