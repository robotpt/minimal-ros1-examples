#!/usr/bin/env python

import rospy
from example.msg import Message


class Subscriber:
    def __init__(self):
        rospy.init_node('subscriber', anonymous=True)
        rospy.Subscriber("pubsub", Message, self.callback)

    def callback(self, data):
        contents = data.content
        options = data.options
        rospy.loginfo(rospy.get_caller_id() + "I heard '%s' with '%s' options" % (contents, options))


if __name__ == '__main__':
    try:
        Subscriber()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
