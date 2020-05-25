#!/usr/bin/env python
# license removed for brevity

import rospy

# Brings in the SimpleActionClient
import actionlib
from std_msgs.msg import String
# Brings in the .action file and messages used by the move base action
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Pose, PoseWithCovarianceStamped, Point, Quaternion, Twist
import sys

pub = rospy.Publisher('theReacher', String, queue_size = 10)

def movebase_client(destino):

    if destino.data == "puerta":
        chosen = Point(22.163, 5.586, 0.000)
    elif destino.data == "sala":
        chosen = Point(-11.744, 6.409, 0.000)
    elif destino.data == "cocina":
        chosen = Point(-5.119, -0.348, 0.000)
    elif destino.data == "bodega":
        chosen = Point(5.496, 2.195, 0.000)

   # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
 
   # Waits until the action server has started up and started listening for goals.
    client.wait_for_server()

   # Creates a new goal with the MoveBaseGoal constructor
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
   # Move 0.5 meters forward along the x axis of the "map" coordinate frame 
    goal.target_pose.pose = Pose(chosen, Quaternion(0.000, 0.000, 0.223, 0.975))
   # No rotation of the mobile base frame w.r.t. map frame

   # Sends the goal to the action server.
    client.send_goal(goal)
   # Waits for the server to finish performing the action.
    wait = client.wait_for_result()
   # If the result doesn't arrive, assume the Server is not available
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
    # Result of executing the action
        pub.publish('goal reached')   

def controller():
  rospy.init_node('theMoover', anonymous = True)

  rospy.Subscriber("heardString", String, movebase_client)

  rospy.spin() 

# If the python node is executed as main process (sourced directly)
if __name__ == '__main__':
    print("Starting route service...")
    controller()
    # try:
    #    # Initializes a rospy node to let the SimpleActionClient publish and subscribe
    #     rospy.init_node('theMoover')
    #     result = movebase_client(sys.argv[1])
    #     if result:
    #         rospy.loginfo("Goal execution done!")
    # except rospy.ROSInterruptException:
    #     rospy.loginfo("Navigation test finished.")
