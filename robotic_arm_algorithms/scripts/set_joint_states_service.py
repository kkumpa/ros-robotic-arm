#!/usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from std_msgs.msg import Float32
from moveit_commander.conversions import pose_to_list
from robotic_arm_algorithms.srv import *


class MoveItContext(object):
    """
    MoveIt! context object contains all information about the robot and planning.
    """
    def __init__(self):
        moveit_commander.roscpp_initialize(sys.argv)

        ## Instance of a `RobotCommander`_ object provides information such as the robot's
        ## kinematic model and the robot's current joint states
        robot = moveit_commander.RobotCommander()

        ## Instantce of a `PlanningSceneInterface`_ object provides a remote interface
        ## for getting, setting, and updating the robot's internal understanding of the
        ## surrounding world:
        scene = moveit_commander.PlanningSceneInterface()

        ## Instantce of a `MoveGroupCommander`_ object is an interface
        ## to a planning group (group of joints).  
        ## This interface can be used to plan and execute motions:
        group_name = "arm"
        move_group = moveit_commander.MoveGroupCommander(group_name)
        
        planning_frame = move_group.get_planning_frame()
        end_effector_link = move_group.get_end_effector_link()
        group_names = robot.get_group_names()

        self.box_name = ''
        self.robot = robot
        self.scene = scene
        self.move_group = move_group
        self.planning_frame = planning_frame
        self.end_effector_link = end_effector_link
        self.group_names = group_names


    def go_to_joint_state(self, req):
        print("Starting planning to go to joint state.\n")
        joint_goal = self.move_group.get_current_joint_values()
        joint_goal[0] = req.forearm_0.data   # forearm 0
        joint_goal[1] = req.forearm_1.data   # forearm 1
        joint_goal[2] = req.arm_0.data   # arm 0
        joint_goal[3] = req.arm_1.data   # arm 1

        print("Setting joint goal:")
        print(joint_goal)
        print("")

        # The go command can be called with joint values, poses, or without any
        # parameters if you have already set the pose or joint target for the group
        self.move_group.go(joint_goal, wait=True)

        # Calling ``stop()`` ensures that there is no residual movement
        self.move_group.stop()


def set_joint_states(req):
    moveit_context = MoveItContext()
    moveit_context.go_to_joint_state(req)
    res = SetJointStatesResponse()
    res.res.data = True

    return(res)


def set_joint_states_server():
    rospy.init_node('set_joint_states_service_node')
    service = rospy.Service('set_joint_states_service', SetJointStates, set_joint_states)
    rospy.spin()
    

if __name__ == '__main__':
    try:
        set_joint_states_server()
    except rospy.ROSInterruptException:
        pass
