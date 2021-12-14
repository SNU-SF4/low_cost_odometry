# Comparison of Low-Cost Odometry for Mobile Robot in Various Indoor Environments

---

## Overview

- Paper

- [Presentation Video](https://youtu.be/iK0QkvQVDcc)

- [Presentation Slide](https://github.com/SNU-SF4/low_cost_odometry/blob/master/docs/Final%20Presentation.pdf)

## Our Dataset

- .rosbag file download link

| Scenario Files | Features | Object Type | Driving Path Pattern |
|:--------------:|:--------:|:-----------:|:--------------------:|
| [s1.bag](https://drive.google.com/file/d/1wzxDV77zRVn54Utbji_6kYGPARO9lEUA/view?usp=sharing) | Many | Static | Straight |
| [s2.bag](https://drive.google.com/file/d/1NdQNDeO9lAZSxGLSwATfnhGLFPFWQTwo/view?usp=sharing) | Many | Static | Zig-zag |
| [s3.bag](https://drive.google.com/file/d/1Z_XrhmLtkIxeywfYbzp9B9SXbCQKng2S/view?usp=sharing) | Many | Dynamic | Straight |
| [s4.bag](https://drive.google.com/file/d/1Mz33g9se3Gz_AfXxkszVqeF8Brn0HB8S/view?usp=sharing) | Many | Dynamic | Zig-zag |
| [s5.bag](https://drive.google.com/file/d/1yhdSs-YQiiyNVaIjRY0iPPceRBmjUaWg/view?usp=sharing) | Not Many | Static | Straight |
| [s6.bag](https://drive.google.com/file/d/1dNNRLzCfjIUs9eEikB_6pS679w0Aib02/view?usp=sharing) | Not Many | Static | Zig-zag |
| [s7.bag](https://drive.google.com/file/d/1wfo1uhe8xe8nkJTT9hZ1DhK6sDnqWsCg/view?usp=sharing) | Not Many | Dynamic | Straight |
| [s8.bag](https://drive.google.com/file/d/1WTiYG-9ADSSttW8-QoeQ1mMmT80McESL/view?usp=sharing) | Not Many | Dynamic | Zig-zag |

## Sensor Fusion Combination List

- Wheel only
- Wheel + IMU
- LiDAR only
- Wheel + IMU + LiDAR
- Monocular
- RGBD Only
- LiDAR + RGBD
- Wheel + IMU + RGBD
- Wheel + IMU + LiDAR +RGBD

## How to re-play rosbag dataset

- Download .bag file & copy to workspace

- Select scenario data by modifying the [launch file](https://github.com/SNU-SF4/low_cost_odometry/blob/master/launch/rosbag_play.launch).

  - Of course, rosbag options can be added through the "option" argument.

- View odometry visualization of sensor fusion method

```bash
roslaunch low_cost_odometry [sensor_fusion_method].launch
```

## How to extract jrajectory data

- Edit [launch file](https://github.com/SNU-SF4/low_cost_odometry/blob/master/launch/rosmsg_to_tum.launch)

- Parameters
  - [msg_type](https://github.com/SNU-SF4/low_cost_odometry/blob/master/launch/rosmsg_to_tum.launch#L20): argment name to select rosmsg type

  - [extracted_topic](https://github.com/SNU-SF4/low_cost_odometry/blob/master/launch/rosmsg_to_tum.launch#L21): argment name to extract topic

  - [scene_number](https://github.com/SNU-SF4/low_cost_odometry/blob/master/launch/rosmsg_to_tum.launch#L22): scenario folder name

  - [tum_file_name](https://github.com/SNU-SF4/low_cost_odometry/blob/master/launch/rosmsg_to_tum.launch#L22): output tum file name

## Installation EVO

```bash
pip install evo --upgrade --no-binary evo
```

## plot output data

- Go to tum files directory

```bash
roscd low_cost_odometry/output/{s1, s2, s3 ...}
evo_traj tum wheel_only.txt wheel_imu.txt lidar_only.txt wheel_imu_lidar.txt rgbd.txt wheel_imu_rgbd.txt lidar_rgbd.txt wheel_imu_lidar_rgbd.txt --plot
```
