#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32

rospy.init_node("sub_random")
n=0
print "hello"

def callback(msg):
    n=+1
    print " the message is " + str(msg.data)
    print n

rospy.Subscriber('number', Float32, callback)

rospy.spin()
