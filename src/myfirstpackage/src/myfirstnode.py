#!/usr/bin/env python

import rospy

rospy.init_node('myfirstnode')
rate = rospy.Rate(10)

# ADD YOUR CODE HERE
variable = rospy.get_param("rosversion", 10)
print "hello world running in ros version %s" % variable
rospy.set_param("rosversion", 11)
variable = rospy.get_param("rosversion", 1)
print "hello world running in ros version %s" % variable

rate.sleep()
