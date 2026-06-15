import numpy as np
import pandas as pd
import time

#start_time = time.time()

# 读取 Excel 文件
data_list = pd.read_excel('迭代结果.xlsx', sheet_name='Sheet1', header=None).values
data = np.diff(data_list, axis=1)
vectors = np.array(data)

# 参数 m（通常设为总通道数或预期最大基底数）
m = 3600   #NOTE:change with main program

# ===================== 算法主体 =====================
basis = []          # 标准正交基向量列表
indices = []        # 被接受的通道索引
p = 0               # 当前基底数量
phi_max = 0.0       # 已处理向量的最大范数

i = 0
while i < len(vectors):
    phi = vectors[:,i]
    #print(vectors[:,i].shape)
    idx = i                     # 原 enumerate 的索引
    phi = np.asarray(phi).flatten()
    norm_phi = np.linalg.norm(phi)
    if norm_phi == 0.0:
        i += 1                  # 跳过零向量，继续下一个
        continue

    phi_max = max(phi_max, norm_phi)
    print("迭代中的最大长度:",phi_max)

    # 修正的格拉姆-施密特正交化：计算残差 psi
    psi = phi.copy()
    for d in basis:
        proj = np.dot(d, psi)
        psi -= proj * d

    norm_res = np.linalg.norm(psi)
    print("正交基的长度:",norm_res)
    # 自适应阈值判断
    if p == 0:
        accept = True
    else:
        threshold = (p / m) * phi_max
        #print(p / m)
        accept = (norm_res >= threshold)

    if accept:
        if norm_res > 1e-12:
            new_basis = psi / norm_res
        else:
            i += 1              # 残差过小，不加入基底，继续下一个
            continue
        basis.append(new_basis)
        indices.append(idx)
        p += 1
        i += 1                  # 处理完当前向量，移动到下一个
    else:
        break                   # 不满足条件，停止选取后续通道
# ===================== 输出结果 =====================
print("被接受的通道索引:", indices)
print("基底向量个数:", len(basis))
print("各基底的范数 (应为1):", [np.linalg.norm(v) for v in basis])
if len(basis) > 1:
    print("前两个基底的内积 (应接近0):", np.dot(basis[0], basis[1]))