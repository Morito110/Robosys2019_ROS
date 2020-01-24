#!/usr/bin/env python
import rospy
import random
from std_msgs.msg import String

rospy.init_node( 'ActionCommand' )
pub = rospy.Publisher( 'ActionCommand', String, queue_size=1 )
rate = rospy.Rate(1)

while not rospy.is_shutdown():
    r = random.randint( 1, 4 )
    if r == 3:
        a = 'OK '
    else:
        a = 'STOP! '
    pub.publish(a)
    rate.sleep()
