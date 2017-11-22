import rospy
import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3

p = rospy.Publisher('mobile_base/commands/velocity', Twist, queue_size=10)
bridge = CvBridge()

# callback function is called whenever the subscriber detects new data within the camera
# topic, takes the topic's data as input, and uses that for whatever purpose we define.
def callback(data):
    frame = data.header.seq
    vel = 1.0 * frame / 1000.0
    try:
	cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
	print(e)
    (rows, cols, channels) = cv_image.shape
    p.publish(Twist(Vector3(0,0,0), Vector3(vel, vel, vel)))
    print ("Current frame number is: %d" % frame, "Am publishing velocity: (%d, %d, %d) (%d, %d, %d)" % (0, 0, 0, vel, vel, vel))

if __name__ == '__main__':
  rospy.init_node('translator', anonymous=False)
  rospy.Subscriber('camera/rgb/image_raw', Image, callback)
  rate = rospy.Rate(10)
  while not rospy.is_shutdown():
    str = rospy.get_time()
    img = rospy
#    rospy.loginfo("%s" % str)
    rate.sleep()


# Overall plan: import necessary data and message libraries, including cv2 and cv_bridge.
# Define the necessary callback function, publisher, subscriber, and CvBridge objects.
# Define other necessary functions for the ML Object Detection code from Kent.
# Main Method Order:
#   1. Take video feed as input with callback function
#   2. Check if current frame is xth frame since last analyzed: If not, change nothing.
#   3. Analyze frame to detect object and its position within the image frames.
#   4. Adjust heading and velocity based on said object's position: Can stop if need be
