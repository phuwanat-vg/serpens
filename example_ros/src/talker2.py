#!/usr/bin/env python3
# license removed for brevity
import rospy
from geometry_msgs.msg import Twist

def talker():
    pub = rospy.Publisher('chatter_vel', Twist, queue_size=10)
    rospy.init_node('talker_vel', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    vel = Twist()
    while not rospy.is_shutdown():
        vel.linear.x = 0.1
        vel.angular.z = 0.5
        rospy.loginfo(vel)
        pub.publish(vel)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
