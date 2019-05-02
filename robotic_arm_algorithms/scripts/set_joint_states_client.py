#!/usr/bin/env python

import sys
import rospy
from robotic_arm_algorithms.srv import *

def set_joint_states(joint_states):
    rospy.wait_for_service('set_joint_states_service')
    try:
        set_joint_states_h = rospy.ServiceProxy('set_joint_states_service', SetJointStates)
        req = SetJointStatesRequest()
        req.forearm_0.data = joint_states[0]
        req.forearm_1.data = joint_states[1]
        req.arm_0.data = joint_states[2]
        req.arm_1.data = joint_states[3]
        
        resp = set_joint_states_h(req)
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

if __name__ == "__main__":
    if len(sys.argv) == 5:
        joint_states = [float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])]
        set_joint_states(joint_states)
    else:
        print("not enaugh argument. Four arguments required: forearm 0, forearm 1, arm 0, arm 1")
        sys.exit(1)
        