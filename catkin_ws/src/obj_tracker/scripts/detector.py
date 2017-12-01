#!/usr/bin/env python
# MIT License -- Do whatever you want with this file, the author couldn't care less

import rospy
import cv2
import numpy as np
from std_msgs.msg import String

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

def detector():
    pub = rospy.Publisher('detector_topic', String, queue_size=10)
    rospy.init_node('detector_node', anonymous=True)
    rate = rospy.Rate(100) #3 Hz
    while not rospy.is_shutdown():

        ret, img = cap.read()

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

#	 Only functions correctly if uses cv2.waitKey(1) & 0xFF == ord(key)?
        cv2.imshow('img', img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
	  break

        for (x,y,w,h) in faces:
            coords = `x` + "," + `y` + "," + `w` + "," + `h`
            pub.publish(coords)

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
