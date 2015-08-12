#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Range

rospy.init_node("teleop_withRange")
pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
twist = Twist()
something_in_front = True

def callback(joy):
    global twist, pub, something_in_front
    twist.angular.z = joy.axes[0]
    if something_in_front:
        twist.linear.x = 0
    else:
        twist.linear.x = joy.axes[1]
    #pub.publish(twist)

def callback_range(ranges):
    global something_in_front, twist, pub
    print "Object %f far away" % ranges.range
    if ranges.range <= 0.20 and twist.linear.x>0:
        twist.linear.x = 0
        print "ACHTUNG!!!"
        something_in_front = True
    else:

        something_in_front = False
        #twist.linear.x = lastSpeed
    #pub.publish(twist)

rospy.Subscriber('range', Range, callback_range)
rospy.Subscriber('joy', Joy, callback)
r = rospy.Rate(20)

#rospy.spin()
while not rospy.is_shutdown():
    pub.publish(twist)
    r.sleep()
