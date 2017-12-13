#!/usr/bin/env python
# MIT License -- Do whatever you want with this file, the author couldn't care less

# Accel. limits, use Microsoft Kinect, pad 0's instead of stopping, try to use depth,
# remember which direction target left FOV. 

import rospy
import cv2
import numpy as np
from std_msgs.msg import String
from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

running_avg, vel, turn, acc = [(0,0,0)], 0, 0, 0.2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
bridge = CvBridge()
cap = cv2.VideoCapture(0)

rospy.init_node('detector_node', anonymous=True)
pub = rospy.Publisher('/cmd_vel_mux/input/teleop', Twist, queue_size=10)
rate = rospy.Rate(100) #3 Hz

# determines average x-y coordinates of collection of points, and average areas
def get_avg(info):
    x, y, a, length = 0.0, 0.0, 0.0, len(info)
    for i in info:
        x += i[0]
        y += i[1]
        a += i[2]
    return (x/length, y/length, a/length)

# determines how quickly robot moves rotation-wise, includes deadzone and
# negative feedback in form of quadratic sloping speed. 
# Goal: Slow if target in center half of screen, stop if in inner quintile of screen
def get_turn(objC_X, scale):
    dist = objC_X - 320
    if dist > 100:
        return (dist**2) * scale
    elif dist < -100:
        return -(dist**2) * scale
    else:
        return 0
    
# determines how quickly robot moves forward, includes deadzone and negative
# feedback with small area meaning large velocity and large area meaning small
# velocity. Cutoff for deadzone. 
def get_vel(area, scale):
    vel = (340 * 260) / area * scale
    if (vel < .1):
        return 0
    else:
        return vel
    
# called whenever new data is received by subscriber in /camera/rgb/image_raw topic
def callback(data):
    global running_avg, vel, turn, acc

    cv_image = bridge.imgmsg_to_cv2(data, desired_encoding="passthrough")
    gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    # Only displays correctly if uses cv2.waitKey(1) to allow rendering
    cv2.imshow('img', cv_image)
    cv2.waitKey(1)

    # If no faces are found, slow down linearly but keep moving in same desired direction
    if (faces == ()):
        target_vel = 0
        if (turn > 0):
            target_turn = 1
        else:
            target_turn = -1
        rospy.loginfo("None found")
        
    # If some number of faces are found, add values to running_avg
    # TODO: What if multiple faces?
    else:
        for (x,y,w,h) in faces:
            # Set an upper limit on running_avg to the 5 most recent data points
            if (len(running_avg) >= 5):
                running_avg = running_avg[1:]
            list.append(running_avg, (x+w/2, y+h/2, w*h))
                
            # Assign a best guess for the position and size of the object
            (centerX, centerY, area) = get_avg(running_avg)

            # Calculate the actual forward and turning velocities, then publish
            target_turn = get_turn(centerX, 1)
            target_vel = get_vel(area, 1)
            rospy.loginfo("Turn: %d\t Vel: %d" %(turn, vel))

    # Some rudimentary acceleration limits, set at arbitrary values
    if (target_vel - vel > acc):
        vel = vel + acc
    elif (target_vel - vel < -acc):
        vel = vel - acc
    else:
        vel = target_vel
    if (target_turn - turn > acc):
        turn = turn + acc
    elif (target_turn - turn < -acc):
        turn = turn - acc
    else:
        turn = target_turn

    pub.publish(Twist(Vector3(vel, 0, 0), Vector3(0, 0, turn)))
            

if __name__ == '__main__':
    # Note: Standard image size is 640x480 with x = 0-639, y= 0-479
    sub = rospy.Subscriber('/camera/rgb/image_raw', Image, callback)
    try:
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
