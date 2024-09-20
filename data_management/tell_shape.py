import numpy as np
import os
import pandas as pd

# 可自由复制的文件路径                                                                                                                      
file_path = '/users/ymy_yuan/My_NetShare/Diffusion-TS/OUTPUT/pred_time_series/final_data.npy'  # 替换为你的文件路径，支持 .npz、.npy 或 .csv 文件

def print_npy_shape(file_path):
    data = np.load(file_path)
    print(f"The shape of the array in {file_path} is {data.shape}")

def print_npz_shapes(file_path):
    data = np.load(file_path)
    for array_name in data:
        array_shape = data[array_name].shape
        print(f"Array '{array_name}' has shape {array_shape}")
    data.close()

def print_csv_shape(file_path):
    data = pd.read_csv(file_path)
    print(f"The shape of the data in {file_path} is {data.shape} (rows, columns)")

def check_file_type_and_print_shape(file_path):
    if not os.path.isfile(file_path):
        print(f"The file {file_path} does not exist.")
        return

    file_extension = os.path.splitext(file_path)[1].lower()

    if file_extension == '.npy': 
        print_npy_shape(file_path)
    elif file_extension == '.npz':
        print_npz_shapes(file_path)
    elif file_extension == '.csv':
        print_csv_shape(file_path)
    else:
        print(f"The file {file_path} is not a .npy, .npz, or .csv file.")

# 调用函数进行检测和输出
print(file_path)
check_file_type_and_print_shape(file_path)