## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard something")

if __name__ == '__main__':
  p = rospy.Publisher('chatter', String, queue_size=10)
  rospy.Subscriber('chatter', String, callback)
  rospy.init_node('python', anonymous=True)
  rate = rospy.Rate(10)
  while not rospy.is_shutdown():
    str = rospy.get_time()
#    rospy.loginfo("%s" % str)
    p.publish("%s" % str)
    rate.sleep()

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
