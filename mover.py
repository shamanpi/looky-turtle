#!/usr/bin/env python
# MIT License -- Do whatever you want with this file, the author couldn't care less

import rospy
import cv2
import numpy as np
from std_msgs.msg import String
from geometry_msgs.msg import Twist, Vector3

#    pub = rospy.Publisher('detector_topic', String, queue_size=10)
#    rospy.init_node('detector_node', anonymous=True)
#    rate = rospy.Rate(3) #3 Hz

#        for (x,y,w,h) in faces:
#            coords += `x` + "," + `y` + "," + `w` + "," + `h`
#            pub.publish(coords)

# here we should use the 4 values within a target to publish to the cmd_vel topics
def callback(target_data):
  x, y, w, h = target_data
  center = (x+w/2, y+h/2)
  pub.publish(Twist(Vector3(i,j,k), Vector3(x,y,z)))

def listener():
  pub = rospy.Publisher('cmd_vel_mux/input/teleop', Twist, queue_size=10)
  rospy.init_node('mover', anonymous=True)
  rospy.Subscriber('detector_topic', String, callback)

  rospy.spin()

if __name__ == '__main__':
  listener()
