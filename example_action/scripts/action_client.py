#! /usr/bin/env python

import rospy
import actionlib

from example_action.msg import DoCountAction, DoCountGoal


class CounterClient:

    def __init__(self):
        rospy.init_node('example_action_client')
        self._action_client = actionlib.SimpleActionClient(
            'do_count',
            DoCountAction,
        )

    def run_and_wait_for_result(self, value_to_count_to):
        self.run(value_to_count_to)
        return self.wait_for_result()

    def run(self, value_to_count_to):

        self._action_client.wait_for_server()
        goal = DoCountGoal()
        goal.count_until = value_to_count_to

        self._action_client.send_goal(
            goal,
            done_cb=self._done_callback,
            feedback_cb=self._feedback_callback,
            active_cb=self._active_callback,
        )

    def wait_for_result(self):

        self._action_client.wait_for_result()
        return self.get_result()

    def get_result(self):
        return self._action_client.get_result()

    def get_state(self):
        return self._action_client.get_state()

    def cancel_goal(self):
        self._action_client.cancel_goal()

    def _done_callback(self, status, result):

        rospy.loginfo("DONE with status of '{status}' and a result of '{result}'".format(
            status=status,
            result=result,
        ))

    def _feedback_callback(self, feedback):
        rospy.loginfo("Feedback received: {}".format(feedback))

    def _active_callback(self):
        rospy.loginfo("Goal is active")


if __name__ == '__main__':

    value_to_count_to_ = 5

    counter_client = CounterClient()

    print("\n###############################")
    print("###     Run to success      ###")
    print("###############################")
    result_ = counter_client.run_and_wait_for_result(value_to_count_to_)
    rospy.loginfo("Run finished with result '{}'".format(result_))
    rospy.sleep(1)

    print("\n###############################")
    print("###      Cancel early       ###")
    print("###############################")
    counter_client.run(value_to_count_to_)
    rate = rospy.Rate(1)
    for _ in range(3):
        rospy.loginfo("Current state is '{}'".format(counter_client.get_state()))
        rospy.loginfo("Current result is '{}'".format(counter_client.get_result()))
        rate.sleep()
    rospy.loginfo("Cancelling job")
    counter_client.cancel_goal()
    rospy.sleep(1)
    rospy.loginfo("State after cancelling '{}'".format(counter_client.get_state()))
    rospy.loginfo("Result after cancelling '{}'".format(counter_client.get_result()))
    rospy.sleep(1)

    print("\n###############################")
    print("###      Preempt goal       ###")
    print("###############################")
    counter_client.run(value_to_count_to_)
    for _ in range(3):
        rate.sleep()
    rospy.loginfo("Preempting with another job")
    result_ = counter_client.run_and_wait_for_result(value_to_count_to_)
    rospy.loginfo("Run finished with result '{}'".format(result_))
