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

python2 src/socket/robot_udp_send.py