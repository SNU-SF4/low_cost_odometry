# Comparison of Low-Cost Odometry for Mobile Robot in Various Indoor Environments

## Our Dataset

- .rosbag file download link

| File Name | Description |
|:---------:|:-----------:|
| [2021-11-13-19-45-51.bag](https://drive.google.com/file/d/1HWKkQmNr9aHAFg4VIHGh-mrRCe4SstbS/view?dusp=sharing)| for sensor data acquisition test |
| [Scenario files]([https://TBD](https://drive.google.com/drive/folders/1ONVs4CvSBaujFPBEARuzvEd-oGOKax3B?usp=sharing)) | Our dataset |

## Sensor Fusion Combination List

- TBD

## How to run

- Download .bag file & copy to workspace

```bash
roscore
roscd low_cost_odometry/bag
# copy the bag file in the directory
rosbag play 2021-11-22-13-10-34.bag --clock # for test
```

- View odometry visualization of sensor fusion method

```bash
roslaunch low_cost_odometry [sensor_fusion_method].launch
```
