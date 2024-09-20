import numpy as np
import pandas as pd

# 加载 .npy 文件
data = np.load('/users/ymy_yuan/My_NetShare/Diffusion-TS/OUTPUT/unconstrained_output/ddpm_fake_unconstrained_output.npy')

# 确保数据是三维的并且形状为 (1, n, m)
if len(data.shape) == 3 and data.shape[0] == 1:
    # 去掉第一个维度，使其变为 (n, m)
    data_reshaped = data.squeeze(axis=0)
    
    # 将数据转换为 Pandas DataFrame
    df = pd.DataFrame(data_reshaped)
    
    # 保存为 .csv 文件
    output_csv = '/path/to/your/output.csv'
    df.to_csv("/users/ymy_yuan/My_NetShare/data_management/3dto2d.csv", index=False)
    
    print(f"Data saved to {output_csv}")
else:
    raise ValueError("Input data is not in the expected shape (1, n, m).")