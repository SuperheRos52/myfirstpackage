#!/usr/bin/env python

import rospy
from std_msgs.msg import String

rospy.init_node("pub_node")

msg_string = String()

pub = rospy.Publisher('first_topic', String, queue_size=10)

r = rospy.Rate(5)

while not rospy.is_shutdown():
    msg_string.data = "Welcome to ROS!"
    pub.publish(msg_string)
    r.sleep()


