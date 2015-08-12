#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

rospy.init_node("teleop_node")
pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
twist = Twist()

def callback(joy):
    global twist, pub
    twist.angular.z = joy.axes[0]
    twist.linear.x = joy.axes[1]
    pub.publish(twist)

rospy.Subscriber('joy', Joy, callback)

rospy.spin()
