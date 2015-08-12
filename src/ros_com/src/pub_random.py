#!/usr/bin/env python

import rospy
import random
from std_msgs.msg import Float32

rospy.init_node("pub_random")

msg_string = Float32()

pub = rospy.Publisher('number', Float32, queue_size=10)

r = rospy.Rate(5)

while not rospy.is_shutdown():
    random.randrange(0,10)
    msg_string.data = random.random()*10
    pub.publish(msg_string)
    r.sleep()


