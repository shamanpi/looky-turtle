## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3

# frame x = uint32 seq from the data, used for timing
p = rospy.Publisher('mobile_base/commands/velocity', Twist, queue_size=10)

def callback(data):
    rospy.loginfo(rospy.get_caller_id())
    p.publish(Twist(Vector3(data[0][0] / 255, data[0][1] / 255, data[0][2] / 255), Vector3(0, 0, 0)))

if __name__ == '__main__':
  rospy.Subscriber('camera/rgb/image_raw', Image, callback)
  rospy.init_node('translator', anonymous=False)
  rate = rospy.Rate(10)
  while not rospy.is_shutdown():
    str = rospy.get_time()
#    rospy.loginfo("%s" % str)
    img = rospy
    p.publish("%s" % str)
    rate.sleep()
