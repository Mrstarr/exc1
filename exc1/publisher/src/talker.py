#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32


def talker():
    # topic name is my Surname
    pub = rospy.Publisher('Hu', Float32, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(20) # 20hz
    k = 1   # miniumal integer
    n = 4   # number increased per loop
    while not rospy.is_shutdown():
        pub.publish(k)
        k += n 
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
