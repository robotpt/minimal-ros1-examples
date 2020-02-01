#!/usr/bin/env python

from example_service.srv import Instructions, InstructionsResponse
import rospy 
import random


class Server:

    def __init__(
            self, 
            node_name='server',
            service_topic='instructions',
            is_user_input=False,
    ):
        rospy.init_node(node_name)
        self._service = rospy.Service(service_topic, Instructions, self._follow_instructions)
        self._is_user_input = is_user_input

    def _follow_instructions(self, request):
        rospy.loginfo(rospy.get_caller_id() + "I received '%s'" % request.content)
        response = InstructionsResponse()
        if self._is_user_input:
            response.result = raw_input(request.content + "\n > ")
        else:
            response.result = random.choice(['Yup', 'Yessir', 'Yuppers', 'Yeah', 'Si'])
            rospy.sleep(1)
        return response


if __name__ == "__main__":
    Server()
    rospy.spin()
