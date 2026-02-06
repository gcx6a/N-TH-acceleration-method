import numpy as np
import pandas as pd
import time
# 增加精度控制
#np.set_printoptions(precision=16)
# 开始计时
start_time = time.time()

# 读取 Excel 文件，不将第一行作为列名，而是作为数据
data = pd.read_excel('迭代结果.xlsx', sheet_name='Sheet1', header=None).values
#print(data)
a = 1  # 第一个快照阵的起始（注意：Python索引从0开始，但这里保持原意）
b = 3 # 第一个快照阵的结束
cmax = 100  # 总共需要计算的燃耗步数

x1 = data[:, a-1:b]  # Python索引从0开始，所以a-1到b-1
x2 = data[:, a:b+1]  # a到b（原MATLAB中的a+1到b+1）
#print(x1)
# 对第一个快照矩阵进行奇异值分解
u, s, vh = np.linalg.svd(x1, full_matrices=False)
#print(u)
# 选取截断秩
rank = round(0.7 * (b - a +1))
uu = u[:, :rank]  # 左奇异值矩阵截断
#print(uu)
# 注意：numpy的svd返回的是vh（V的共轭转置），需要转置得到v
v = vh.T
vv = v[:, :rank]  # 右奇异值矩阵截断

U = uu.T  # 转置
#print(U)
# 构建奇异值矩阵（对角阵）
ss = np.diag(s[:rank])
#print(ss)
#print(ss)
S = np.linalg.inv(ss)  # 求截断后奇异值矩阵逆

# 求原矩阵低阶近似矩阵
Fdmd = U @ x2 @ vv @ S

# 进行特征值分解
l, w = np.linalg.eig(Fdmd)  # l为特征值数组，w为特征向量矩阵

# 构建模态
motai = x2 @ vv @ S @ w
#print(motai)
# 求模态伪逆
motai_weini = np.linalg.pinv(motai)
#print(motai_weini)

# 初始化预测结果和误差数组
yuce2 = np.zeros((data.shape[0], cmax))
z2 = np.zeros((data.shape[0], cmax))
wucha = np.zeros((data.shape[0], cmax))

# 计算后续燃耗步的核素密度
for j in range(a-1, cmax):  # Python索引从0开始
    # 构建核素密度演变规律矩阵
    # 注意：这里使用特征值的幂次，需要处理复数情况
    l_power = np.diag(l ** (j - b + 1))  # 调整索引偏移
    
    B = motai @ l_power @ motai_weini
    
    # 计算核素密度（注意索引调整）
    yuce2[:, j] = B @ data[:, b-1]  # b-1对应MATLAB中的b索引
    
    # 取实部
    z2[:, j] = np.real(yuce2[:, j])
    '''
    # 计算相对误差
    for i in range(data.shape[0]):
        if data[i, j] != 0:  # 避免除以零
            wucha[i, j] = (z2[i, j] - data[i, j]) / data[i, j] * 100
        else:
            wucha[i, j] = 0
    '''
#print(z2[:,70])
# 结束计时
end_time = time.time()
print(f"计算完成，耗时: {end_time - start_time:.2f} 秒")

# 如果需要保存结果，可以添加以下代码：
pd.DataFrame(z2).to_excel('预测结果.xlsx')
#pd.DataFrame(wucha).to_excel('误差分析.xlsx')