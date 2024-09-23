# 更新系统并安装 Nvidia 驱动
sudo apt update  
sudo apt install ubuntu-drivers-common
sudo ubuntu-drivers devices
sudo apt install nvidia-driver-535
sudo reboot
nvidia-smi

# 更新系统并安装 Python3 pip
sudo apt update
sudo apt install python3-pip
pip3 install torch

# 设置 PATH 环境变量
export PATH=$PATH:/users/ymy_yuan/.local/bin
echo 'export PATH=$PATH:/users/ymy_yuan/.local/bin' >> ~/.bashrc
source ~/.bashrc

# 下载并安装 Anaconda
wget https://repo.anaconda.com/archive/Anaconda3-2023.03-Linux-x86_64.sh
bash Anaconda3-2023.03-Linux-x86_64.sh
source ~/.bashrc

# 安装 Git
sudo apt install git

# 编辑 .bashrc 文件
vim ~/.bashrc

# 在 .bashrc 文件中添加以下内容
# <<< conda initialize <<<
export PS1='(\W)\$ '
export CUDA_HOME=/usr/local/cuda
export PATH=$CUDA_HOME/bin:$PATH
export LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH
export PATH=/usr/local/cuda-11.5/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda-11.5/lib64:$LD_LIBRARY_PATH

# 使用 SCP 进行文件传输
scp  ymy_yuan@c240g5-110119.wisc.cloudlab.us:~/My_NetShare/My_NetShare.tar.gz ~/Desktop
scp /Users/yuanmingyulinyizaitaofan/Desktop/My_NetShare.tar.gz ymy_yuan@c240g5-110107.wisc.cloudlab.us:~/My_NetShare.tar.gz
