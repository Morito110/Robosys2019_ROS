#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def cb( message ):
    Go = 'Go'
    Wait = 'Wait'

    if 'K' in message.data:
      msg = message.data + Go
    else:
      msg = message.data + Wait
    pub.publish(msg)

if __name__ == '__main__':
    rospy.init_node( 'Go' )
    pub = rospy.Publisher( 'Go', String, queue_size=1 )
    rate = rospy.Rate(1)
    sub = rospy.Subscriber( 'ActionCommand', String, cb )
    while not rospy.is_shutdown():
        
        rate.sleep()
