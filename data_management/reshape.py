import numpy as np
import pandas as pd

# 加载 npz 文件
npz_data = np.load('/users/ymy_yuan/My_NetShare/NetShare/results/test-ugr16/generated_data/sample_len-1/feat_raw/chunk_id-0/epoch_id-34.npz')
data_attribute = npz_data['data_attribute']
data_feature = npz_data['data_feature']
data_gen_flag = npz_data['data_gen_flag']

# 保存 data_attribute 为 CSV
df_attribute = pd.DataFrame(data_attribute)
df_attribute.to_csv('/users/ymy_yuan/My_NetShare/data_management/data_attribute.csv', index=False)

# 展开 data_feature 并保存为 CSV
data_feature_reshaped = data_feature.reshape(data_feature.shape[0], -1)
df_feature = pd.DataFrame(data_feature_reshaped)
df_feature.columns = [f'feature_{i}' for i in range(data_feature_reshaped.shape[1])]
df_feature.to_csv('/users/ymy_yuan/My_NetShare/data_management/data_feature.csv', index=False)

# 保存 data_gen_flag 为 CSV
df_gen_flag = pd.DataFrame(data_gen_flag)
df_gen_flag.to_csv('/users/ymy_yuan/My_NetShare/data_management/data_gen_flag.csv', index=False) 