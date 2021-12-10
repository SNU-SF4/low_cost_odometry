#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

import rospy
import rospkg
import tf2_ros
import os
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped

# Parameter Server
msg_type = rospy.get_param("/rosmsg_to_tum/msg_type")
extracted_topic = rospy.get_param("/rosmsg_to_tum/extracted_topic")
scene_number = rospy.get_param("/rosmsg_to_tum/scene_number")
tum_file_name = rospy.get_param("/rosmsg_to_tum/tum_file_name")

# Load Config File
rospack = rospkg.RosPack()
output_path = os.path.join(rospack.get_path('low_cost_odometry'), 'output/'+scene_number+'/')


def odom_callback(msg):
    # parse rosmsg
    timestamp = str(msg.header.stamp) + ' '
    x = str(msg.pose.pose.position.x) + ' '
    y = str(msg.pose.pose.position.y) + ' '
    z = str(msg.pose.pose.position.z) + ' '
    q_x = str(msg.pose.pose.orientation.x) + ' '
    q_y = str(msg.pose.pose.orientation.y) + ' '
    q_z = str(msg.pose.pose.orientation.z) + ' '
    q_w = str(msg.pose.pose.orientation.w) + '\n'

    # write tum file
    f = open(output_path + tum_file_name, "a")
    f.write(timestamp + x + y + z + q_x + q_y + q_z + q_w)
    f.close()


def pose_callback(msg):
    # parse rosmsg
    timestamp = str(msg.header.stamp) + ' '
    x = str(msg.pose.position.x) + ' '
    y = str(msg.pose.position.y) + ' '
    z = str(msg.pose.position.z) + ' '
    q_x = str(msg.pose.orientation.x) + ' '
    q_y = str(msg.pose.orientation.y) + ' '
    q_z = str(msg.pose.orientation.z) + ' '
    q_w = str(msg.pose.orientation.w) + '\n'

    # write tum file
    f = open(output_path + tum_file_name, "a")
    f.write(timestamp + x + y + z + q_x + q_y + q_z + q_w)
    f.close()


def get_transform():
    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)
    rate = rospy.Rate(10.0)

    while not rospy.is_shutdown():
        try:
            tf = tfBuffer.lookup_transform('map', 'base_footprint', rospy.Time(0))
            trans = tf.transform
            if trans.translation.x != 0.0: # receive only one msg
                break
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            continue
        rate.sleep()

    timestamp = str(tf.header.stamp.secs) + str(tf.header.stamp.nsecs) + ' '
    x = str(tf.transform.translation.x) + ' '
    y = str(tf.transform.translation.y) + ' '
    z = str(tf.transform.translation.z) + ' '
    q_x = str(tf.transform.rotation.x) + ' '
    q_y = str(tf.transform.rotation.y) + ' '
    q_z = str(tf.transform.rotation.z) + ' '
    q_w = str(tf.transform.rotation.w) + '\n'

    # write tum file
    f = open(output_path + tum_file_name, "a")
    f.write(timestamp + x + y + z + q_x + q_y + q_z + q_w)
    f.close()

if __name__ == '__main__':
    rospy.init_node('rosmsg_to_tum')
    rospy.loginfo("Record at " + output_path + tum_file_name)

    if msg_type == 'Odometry':
        rospy.loginfo("Msg type is Odometry")
        rospy.Subscriber(extracted_topic, Odometry, odom_callback, queue_size=100)
    elif msg_type == 'PoseStamped':
        rospy.loginfo("Msg type is PoseStamped")
        rospy.Subscriber(extracted_topic, PoseStamped, pose_callback, queue_size=100)
    elif msg_type == 'Transform':
        rospy.loginfo("TF echo - map to base_footprint")
        while not rospy.is_shutdown():
            get_transform()

    rospy.spin()
