#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def listener():
    rospy.init_node('listener_node', anonymous=True)
    rospy.Subscriber('detector_topic', String, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
