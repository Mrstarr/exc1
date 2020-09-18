#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32


def callback(data):
    i = data.data
    i = i/0.15
    pub.publish(i)
    return i

    
def listener():
    global pub
    pub = rospy.Publisher('result', Float32, queue_size=10)
    rospy.init_node('listener', anonymous=True)
    k = rospy.Subscriber("Hu", Float32, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
