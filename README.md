# tm robot ws

```
 _  __          _        ____ _     _       
| |/ /_____   _(_)_ __  / ___| |__ (_)_   _ 
| ' // _ \ \ / / | '_ \| |   | '_ \| | | | |
| . \  __/\ V /| | | | | |___| | | | | |_| |
|_|\_\___| \_/ |_|_| |_|\____|_| |_|_|\__,_|
                                            
```

## intall
tm_robot install

https://github.com/TechmanRobotInc/tmr_ros1/tree/noetic

    cd src/
    git clone https://github.com/TechmanRobotInc/tmr_ros1.git

arm control install

    sudo apt install python-is-python3


## run

run tm robot

    roslaunch tm5_900_moveit_config tm5_900_moveit_planning_execution.launch sim:=True

    roslaunch tm5_900_moveit_config tm5_900_moveit_planning_execution.launch sim:=False robot_ip:=192.168.0.10

    roslaunch tm5_700_moveit_config tm5_700_moveit_planning_execution.launch sim:=False robot_ip:=192.168.10.2

    rosrun tm_driver tm_driver <robot_ip_address>

    rosrun ui_for_debug_and_demo robot_ui

run arm control

    rosrun arm_control RobotCtrl.py

    python2 src/arm_control/src/RobotCtrl.py

run arm control udp

    python2 src/arm_control/src/RobotCtrl_udp.py
    python2 src/socket/robot_udp_send.py