#!/usr/bin/env python
# MIT License -- Do whatever you want with this file, the author couldn't care less

import rospy
import cv2
import numpy as np
from std_msgs.msg import String
from geometry_msgs.msg import Twist, Vector3

# definition of the classifier (for faces) and video capture.
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

# publishes coords for faces to the 'detector_topic' as a string
def detector():

    # declares topic to publish to, creates node, rate for computing
    pub = rospy.Publisher('detector_topic', String, queue_size=10)
    rospy.init_node('detector_node', anonymous=True)
    rate = rospy.Rate(3) #3 Hz

    while not rospy.is_shutdown():
        # declare variables 
        coords = ""
        ret, img = cap.read()

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
            coords += `x` + "," + `y` + "," + `w` + "," + `h`
            pub.publish(coords)

        cv2.imshow('img', img)

        if (faces != ()):
            rospy.loginfo(coords)
        else:
            rospy.loginfo("None found")
        rate.sleep()

if __name__ == '__main__':
    try:
        detector()
    except rospy.ROSInterruptException:
        pass
