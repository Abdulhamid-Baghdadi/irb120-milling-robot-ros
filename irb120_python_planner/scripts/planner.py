#!/usr/bin/env python
#
# Pose-goal planner for the ABB IRB 120 + milling tool (MoveIt, ROS 1 / Python 2).
#
# Derived from the MoveIt "Move Group Python Interface" tutorial
# (moveit_tutorials, BSD-3-Clause, (c) SRI International / PickNik),
# which provides all_close(), the class skeleton and the BEGIN/END_SUB_TUTORIAL
# comments. Adapted by Abdulhamid Baghdadi: "manipulator" group, the collision
# box in the planning scene and the four drilling poses in main().

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
from tf.transformations import quaternion_from_euler


def all_close(goal, actual, tolerance):
  """
  Convenience method for testing if a list of values are within a tolerance of their counterparts in another list
  @param: goal       A list of floats, a Pose or a PoseStamped
  @param: actual     A list of floats, a Pose or a PoseStamped
  @param: tolerance  A float
  @returns: bool
  """
  all_equal = True
  if type(goal) is list:
    for index in range(len(goal)):
      if abs(actual[index] - goal[index]) > tolerance:
        return False

  elif type(goal) is geometry_msgs.msg.PoseStamped:
    return all_close(goal.pose, actual.pose, tolerance)

  elif type(goal) is geometry_msgs.msg.Pose:
    return all_close(pose_to_list(goal), pose_to_list(actual), tolerance)
  return True


class MoveGroupPythonIntefaceTutorial(object):
  """MoveGroupPythonIntefaceTutorial"""
  def __init__(self):
    super(MoveGroupPythonIntefaceTutorial, self).__init__()

    ## BEGIN_SUB_TUTORIAL setup
    ##
    ## First initialize `moveit_commander`_ and a `rospy`_ node:
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('move_group_python_interface_tutorial',
                    anonymous=True)

    ## Instantiate a `RobotCommander`_ object. This object is the outer-level interface to
    ## the robot:
    robot = moveit_commander.RobotCommander()

    ## Instantiate a `PlanningSceneInterface`_ object.  This object is an interface
    ## to the world surrounding the robot:
    scene = moveit_commander.PlanningSceneInterface()

    ## Instantiate a `MoveGroupCommander`_ object.  This object is an interface
    ## to one group of joints.  In this case the group is the joints in the Panda
    ## arm so we set ``group_name = panda_arm``. If you are using a different robot,
    ## you should change this value to the name of your robot arm planning group.
    ## This interface can be used to plan and execute motions on the Panda:
    group_name = "manipulator"
    group = moveit_commander.MoveGroupCommander(group_name)

    ## We create a `DisplayTrajectory`_ publisher which is used later to publish
    ## trajectories for RViz to visualize:
    display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                   moveit_msgs.msg.DisplayTrajectory,
                                                   queue_size=20)

    ## END_SUB_TUTORIAL

    ## BEGIN_SUB_TUTORIAL basic_info
    ##
    ## Getting Basic Information
    ## ^^^^^^^^^^^^^^^^^^^^^^^^^
    # We can get the name of the reference frame for this robot:
    planning_frame = group.get_planning_frame()
    print "============ Reference frame: %s" % planning_frame

    # We can also print the name of the end-effector link for this group:
    eef_link = group.get_end_effector_link()
    print "============ End effector: %s" % eef_link

    # We can get a list of all the groups in the robot:
    group_names = robot.get_group_names()
    print "============ Robot Groups:", robot.get_group_names()

    # Sometimes for debugging it is useful to print the entire state of the
    # robot:
    print "============ Printing robot state"
    print robot.get_current_state()
    print ""
    ## END_SUB_TUTORIAL


    #box_pose = geometry_msgs.msg.PoseStamped()
    #box_pose.header.frame_id = "box_frame"
    #box_pose.pose.orientation.w = 1.0
    #box_name = "box"

    p = geometry_msgs.msg.PoseStamped()
    p.header.frame_id = robot.get_planning_frame()

    p.pose.position.x = 0.4
    p.pose.position.y = -0.0
    p.pose.position.z = 0.2
    scene.add_box("part", p, (0.3, 0.1, 0.4))

    # Misc variables
    self.box_name = ''
    self.robot = robot
    self.scene = scene
    self.group = group
    self.display_trajectory_publisher = display_trajectory_publisher
    self.planning_frame = planning_frame
    self.eef_link = eef_link
    self.group_names = group_names


  def go_to_pose_goal(self, pose_goal):
    # Copy class variables to local variables to make the web tutorials more clear.
    # In practice, you should use the class variables directly unless you have a good
    # reason not to.
    group_name = "manipulator"
    group = moveit_commander.MoveGroupCommander(group_name)
    group.set_planning_time(10.0)
    print(group.get_joints())
    #group.set_end_effector_link("link_6")
    eef_link = group.get_end_effector_link()
    print "============ End effector: %s" % eef_link
    #group = self.group

    print "============ current pose: %s" % self.group.get_current_pose().pose
    #current_pose = self.group.get_current_pose().pose

    ## BEGIN_SUB_TUTORIAL plan_to_pose
    ##
    ## Planning to a Pose Goal
    ## ^^^^^^^^^^^^^^^^^^^^^^^
    ## We can plan a motion for this group to a desired pose for the
    ## end-effector:
    group.set_pose_target(pose_goal)
    ## Now, we call the planner to compute the plan and execute it.
    plan = group.go(wait=True)

    # Calling `stop()` ensures that there is no residual movement
    group.stop()
    # It is always good to clear your targets after planning with poses.
    # Note: there is no equivalent function for clear_joint_value_targets()
    group.clear_pose_targets()

    ## END_SUB_TUTORIAL

    # For testing:
    # Note that since this section of code will not be included in the tutorials
    # we use the class variable rather than the copied state variable
    current_pose = self.group.get_current_pose().pose
    return all_close(pose_goal, current_pose, 0.01)


def main():
  try:
    #print "============ Press `Enter` to begin the tutorial by setting up the moveit_commander (press ctrl-d to exit) ..."
    #raw_input()
    tutorial = MoveGroupPythonIntefaceTutorial()


    #quaternion_from_euler(roll_angle, pitch_angle, yaw_angle)
    quaternion = quaternion_from_euler(1.57, 0, 0)
    pose_goal = geometry_msgs.msg.Pose()
    pose_goal.orientation.x = quaternion[0]
    pose_goal.orientation.y = quaternion[1]
    pose_goal.orientation.z = quaternion[2]
    pose_goal.orientation.w = quaternion[3]
    pose_goal.position.x = 0.2
    pose_goal.position.y = 0.2
    pose_goal.position.z = 0.3
    tutorial.go_to_pose_goal(pose_goal)


    pose_goal.position.x = 0.4
    pose_goal.position.y = 0.2
    pose_goal.position.z = 0.3
    tutorial.go_to_pose_goal(pose_goal)

    quaternion = quaternion_from_euler(-1.57, 0, 0)
    pose_goal = geometry_msgs.msg.Pose()
    pose_goal.orientation.x = quaternion[0]
    pose_goal.orientation.y = quaternion[1]
    pose_goal.orientation.z = quaternion[2]
    pose_goal.orientation.w = quaternion[3]


    pose_goal.position.x = 0.2
    pose_goal.position.y = -0.2
    pose_goal.position.z = 0.3
    tutorial.go_to_pose_goal(pose_goal)


    pose_goal.position.x = 0.4
    pose_goal.position.y = -0.2
    pose_goal.position.z = 0.3
    tutorial.go_to_pose_goal(pose_goal)

    print "============ Python tutorial demo complete!"
  except rospy.ROSInterruptException:
    return
  except KeyboardInterrupt:
    return

if __name__ == '__main__':
  main()

