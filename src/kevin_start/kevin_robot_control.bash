#!/bin/bash
# Program:
#       This program start tmr_ws
# History:
# 2022/6/10	kevin	First release

echo -e "\033[32m
##############################
# tmr_ws
# by Kevin Chiu 2022
##############################
\033[0m"
ws_path="/home/kevin/src/tmr_ws/" # 路徑
# ws_path=$(pwd) # 自動路徑
echo -e "ws_path:" $ws_path "\n" # 列印路徑
cd $ws_path
source devel/setup.bash

gnome-terminal --tab -t "roslaunch" -- bash -ic "roslaunch tm5_700_moveit_config tm5_700_moveit_planning_execution.launch sim:=False robot_ip:=192.168.10.2"
sleep 0.2
gnome-terminal --tab -t "RobotCtrl_udp" -- bash -ic "python2 src/arm_control/src/RobotCtrl_udp.py"
sleep 0.2