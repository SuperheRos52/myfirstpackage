#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy

rospy.init_node("sub_joy")
print "hello"

is_pressed = False

def callback(msg):
    global is_pressed
    # print " the message is " + str(msg.data[0])
    if not is_pressed and msg.buttons[0] == 1:
        print "Button 1 is pressed "
        is_pressed = True
    elif is_pressed and msg.buttons[0] == 0:
        print "Button 1 is released"
        is_pressed = False

#callback.is_pressed = False

rospy.Subscriber('joy', Joy, callback)

rospy.spin()
