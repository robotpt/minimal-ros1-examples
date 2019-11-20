#!/usr/bin/env python
## Simple demo of a rospy service that add two integers

NAME = 'instructions_server'

# import the AddTwoInts service
from example.srv import Instructions, InstructionsResponse
import rospy 
import random

def follow_instructions(request):
    response = InstructionsResponse()
    response.result = raw_input(request.content)
    return response

def instructions_server():
    rospy.init_node(NAME)
    s = rospy.Service('instructions', Instructions, follow_instructions)

    rospy.spin()

if __name__ == "__main__":
    instructions_server()
