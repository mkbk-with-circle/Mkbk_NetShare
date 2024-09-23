#!/bin/bash

# 更新系统并安装 Nvidia 驱动
echo "Updating system and installing Nvidia drivers..."
sudo apt update -y
sudo apt install -y ubuntu-drivers-common
sudo ubuntu-drivers devices
sudo apt install -y nvidia-driver-535

# 提示重启
echo "Rebooting the system..."
sudo reboot
