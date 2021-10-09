# tm robot ws


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

    rosrun tm_driver tm_driver <robot_ip_address>

    rosrun ui_for_debug_and_demo robot_ui

run arm control

    rosrun arm_control RobotCtrl.py

    python src/arm_control/src/RobotCtrl.py