#!/bin/bash

# 运行nvidia-smi命令, 检查 Nvidia 驱动
echo "Run 'nvidia-smi' to check Nvidia driver status:"
nvidia-smi

# 安装 Python3 pip 和 Torch
echo "Installing Python3 pip and Torch..."
sudo apt update -y
sudo apt install -y python3-pip
pip3 install torch --user

# 更新 PATH 环境变量
echo "Updating PATH environment variable..."
export PATH=$PATH:/users/ymy_yuan/.local/bin
echo 'export PATH=$PATH:/users/ymy_yuan/.local/bin' >> ~/.bashrc
source ~/.bashrc

# 下载并安装 Anaconda
echo "Downloading and installing Anaconda..."
wget https://repo.anaconda.com/archive/Anaconda3-2023.03-Linux-x86_64.sh
bash Anaconda3-2023.03-Linux-x86_64.sh
source ~/.bashrc

# 安装 Git
echo "Installing Git..."
sudo apt install -y git

# 编辑 .bashrc 文件，设置 CUDA 环境变量
echo "Updating .bashrc for CUDA paths..."
cat <<EOT >> ~/.bashrc
# <<< conda initialize <<<
export PS1='(\W)\$ '
export CUDA_HOME=/usr/local/cuda
export PATH=\$CUDA_HOME/bin:\$PATH
export LD_LIBRARY_PATH=\$CUDA_HOME/lib64:\$LD_LIBRARY_PATH
export PATH=/usr/local/cuda-11.5/bin:\$PATH
export LD_LIBRARY_PATH=/usr/local/cuda-11.5/lib64:\$LD_LIBRARY_PATH
EOT
source ~/.bashrc

echo "All tasks completed."
