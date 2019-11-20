#!/usr/bin/env python
# license removed for brevity
import rospy
from example.msg import Message


class Publisher:
    def __init__(self):
        rospy.init_node('Publisher', anonymous=True)
        self.my_pub = rospy.Publisher('pubsub', Message, queue_size=1)
        rospy.Timer(rospy.Duration(1), self.talker)
        
    def talker(self, timer):
        msg = Message()
        msg.content = "hello world %s" % rospy.get_time()
        msg.options = ['Option 1', 'Option 2']
        rospy.loginfo(msg.content)
        self.my_pub.publish(msg)


if __name__ == '__main__':
    try:
        Publisher()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
