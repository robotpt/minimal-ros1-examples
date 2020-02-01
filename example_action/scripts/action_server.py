#! /usr/bin/env python

import rospy
import actionlib

from example_action.msg import DoCountAction, DoCountFeedback, DoCountResult


class CounterServer:

    def __init__(self):

        self._action_server = actionlib.SimpleActionServer(
            'do_count',
            DoCountAction,
            execute_cb=self._execute_callback,
            auto_start=False,
        )
        self._action_server.start()  # helps to avoid race conditions, somehow

    def _execute_callback(self, goal):

        success = True
        rate = rospy.Rate(1)  # run the following for loop every one second
        feedback = DoCountFeedback()
        for i in range(1, goal.count_until+1):

            rospy.loginfo("Current count is {}".format(i))
            feedback.current_value = i
            self._action_server.publish_feedback(feedback)

            if rospy.is_shutdown():
                rospy.loginfo('The server was shutdown')
                exit(-1)
            if self._action_server.is_preempt_requested():
                rospy.loginfo('Goal quit before finishing')
                self._action_server.set_preempted(
                    self._make_result("I didn't make it :/")
                )
                success = False
                break
            rate.sleep()

        if success:
            self._action_server.set_succeeded(
                self._make_result("Made it!")
            )

    @staticmethod
    def _make_result(message):
        result = DoCountResult()
        result.message = message
        return result


if __name__ == '__main__':
    rospy.init_node('action_server')
    CounterServer()
    rospy.spin()
