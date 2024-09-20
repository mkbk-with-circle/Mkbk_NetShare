
import pickle
import json

# 自定义对象转换函数
def default_serializer(obj):
    try:
        # 尝试将对象转换为字典
        return obj.__dict__
    except AttributeError:
        # 如果对象没有 __dict__ 属性，则返回对象的字符串表示
        return str(obj)

# 读取 .pkl 文件中的数据
with open('/users/ymy_yuan/My_NetShare/NetShare/results/test-ugr16/pre_processed_data/chunkid-0/data_feature_fields.pkl', 'rb') as f:
    data = pickle.load(f)
print(data)
# 将数据保存为 JSON 文件
with open('data_feature_field.json', 'w') as jsonfile:
    json.dump(data, jsonfile, default=default_serializer, indent=4)