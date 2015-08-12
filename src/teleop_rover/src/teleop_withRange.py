#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Range

rospy.init_node("teleop_withRange")
pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
gJoy = Joy()
gJoy.axes = [0,0,0,0,0,0]
gRange = Range()
twist = Twist()
something_in_front = True

def callback_joy(joy):
    global gJoy
    gJoy = joy

def callback_range(ranges):
    global gRange
    gRange = ranges

rospy.Subscriber('range', Range, callback_range)
rospy.Subscriber('joy', Joy, callback_joy)
r = rospy.Rate(20)

#rospy.spin()
while not rospy.is_shutdown():
    print "Object %f far away" % gRange.range

    twist.angular.z = gJoy.axes[0]
    twist.linear.x = gJoy.axes[1]

    if gRange.range <= 0.20 and gJoy.axes[1] >= 0:
        twist.linear.x = 0
        print "ACHTUNG!!!"

    pub.publish(twist)
    r.sleep()
