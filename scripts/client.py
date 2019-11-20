#!/usr/bin/env python

import rospy

from example.srv import Instructions, InstructionsRequest

def instructions_client():
    rospy.wait_for_service('instructions')
    
    try:
        instructions_client = rospy.ServiceProxy('instructions', Instructions)
        
        instructions = InstructionsRequest()
        instructions.content = "Do you like it?"
        instructions.options = ['Okay']

        resp = instructions_client(instructions)
        return resp.result

    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

if __name__ == "__main__":
    
    print "Answer: %s" % instructions_client()
