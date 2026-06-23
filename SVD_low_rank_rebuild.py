import numpy as np
import pandas as pd
from numpy.linalg import svd

m = 4   #NOTE:change with main program
# 读取 Excel 文件
data = pd.read_excel('迭代结果-原始.xlsx', sheet_name='Sheet1', header=None).values
#data = np.diff(data, axis=1)
data = np.array(data[:,0:m])

# 1. 计算 SVD
U, s, Vt = svd(data, full_matrices=False)

# 2. 选择保留的奇异值个数 k（这里用能量占比 95%）
total_energy = np.cumsum(s**2)
energy_ratio = 0.9999
k = np.searchsorted(total_energy / total_energy[-1], energy_ratio) + 1
print(k)
# 3. 截断小的奇异值
s_denoised = s.copy()
s_denoised[k:] = 0

# 4. 重建降噪后矩阵
X_denoised = U @ np.diag(s_denoised) @ Vt
# 将降噪后的矩阵转为 DataFrame
df = pd.DataFrame(X_denoised)
# 保存为 Excel 文件
df.to_excel('迭代结果.xlsx', index=False, header=False)
# 此时 X_denoised 即为降噪后的数据
print(f"原始矩阵形状: {data.shape}")
print(f"保留的奇异值个数: {k}")
print(f"降噪后矩阵形状: {X_denoised.shape}")