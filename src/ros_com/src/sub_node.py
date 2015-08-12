#!/usr/bin/env python

import rospy
from std_msgs.msg import String

rospy.init_node("sub_node")
n=0
print "hello"

def callback(msg):
    n=+1
    print " the message is " + msg.data
    print n

rospy.Subscriber('first_topic', String, callback)

rospy.spin()
