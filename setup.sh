# bash setup.sh part1
# bash setup.sh part2
#!/bin/bash

if [ "$1" == "part1" ]; then
    # 这是 setup_part1 的部分
    sudo apt update  
    sudo apt install ubuntu-drivers-common
    sudo ubuntu-drivers devices
    sudo apt install nvidia-driver-535
    sudo reboot

elif [ "$1" == "part2" ]; then
    # 这是 setup_part2 的部分
    nvidia-smi

    sudo apt update
    #（sudo apt install python3-pip）
    pip3 install torch
    export PATH=$PATH:/users/ymy_yuan/.local/bin
    echo 'export PATH=$PATH:/users/ymy_yuan/.local/bin' >> ~/.bashrc
    source ~/.bashrc

    wget https://repo.anaconda.com/archive/Anaconda3-2023.03-Linux-x86_64.sh
    bash Anaconda3-2023.03-Linux-x86_64.sh
    source ~/.bashrc
    sudo apt install git

    vim ~/.bashrc
    # <<< conda initialize <<<
    export PS1='(\W)\$ '
    export CUDA_HOME=/usr/local/cuda
    export PATH=$CUDA_HOME/bin:$PATH
    export LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH
    export PATH=/usr/local/cuda-11.5/bin:$PATH
    export LD_LIBRARY_PATH=/usr/local/cuda-11.5/lib64:$LD_LIBRARY_PATH
else
    echo "请提供有效的参数: part1 或 part2"
fi
