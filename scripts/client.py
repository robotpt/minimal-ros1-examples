#!/usr/bin/env python

import rospy
from example.srv import Instructions, InstructionsRequest


class Client:

    def __init__(
            self, 
            node_name='client', 
            service_topic='instructions'
    ):
        
        rospy.init_node(node_name, anonymous=True)
        self._service_topic = service_topic
        self._client = rospy.ServiceProxy(self._service_topic, Instructions)

    def spin(self):

        while True:
            answer = self.respond_once()
            rospy.loginfo(rospy.get_caller_id() + "I received '%s'" % answer)
            print "Answer: %s" % answer

    def respond_once(self):

        rospy.wait_for_service(self._service_topic)

        try:
            instructions = InstructionsRequest()
            instructions.content = "Do you like it?"
            instructions.options = ['Okay']

            resp = self._client(instructions)
            return resp.result

        except rospy.ServiceException, e:
            print "Service call failed: %s"%e


if __name__ == "__main__":
    client = Client()
    client.spin()
