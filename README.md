# Comparison of Low-Cost Odometry for Mobile Robot in Various Indoor Environments

## Our Dataset

- .rosbag file download link

| File Name | Description |
|:---------:|:-----------:|
| [2021-11-13-19-45-51.bag](https://drive.google.com/file/d/1A_lgDory2tU7COJQypWiKVzKj4QV_qGF/view)| for sensor data acquisition test |
| [2021-11-xx-xx-xx-xx.bag](https://TBD) | Scenario #1 |
| [2021-11-xx-xx-xx-xx.bag](https://TBD) | Scenario #2 |

## Sensor Fusion Combination List

- TBD

## How to run

- Download .bag file & copy to workspace

```bash
roscore
roscd low_cost_odometry/bag
# copy the bag file in the directory
rosbag play 2021-11-13-19-49-51.bag --clock # for test
```

- View odometry visualization of sensor fusion method

```bash
roslaunch low_cost_odometry [sensor_fusion_method].launch
```
