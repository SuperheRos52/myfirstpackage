#!/usr/bin/env python

import rospy

rospy.init_node('myfirstnode')
rate = rospy.Rate(10)

# ADD YOUR CODE HERE
while not rospy.is_shutdown():
    #variable = rospy.get_param("rosversion", 10)
    #print "hello world running in ros version %s" % variable
    #rospy.set_param("rosversion", 11)
    #variable = rospy.get_param("rosversion", 1)
    #print "hello world running in ros version %s" % variable
    paramRate = rospy.get_param("rate", 10)
    rate = rospy.Rate(paramRate)
    print paramRate
    rate.sleep()
