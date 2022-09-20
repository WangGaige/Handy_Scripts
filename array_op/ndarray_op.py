#############################append() 函数可以合并一维数组：############################
import numpy as np
a =np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.append(a, b)
print(c)
# [1 2 3 4 5 6]

#################################append() 也可以合并多维数组：###############################
import numpy as np
a =np.arange(4).reshape(2, 2)
b = np.arange(4).reshape(2, 2)
# 按行合并
c = np.append(a, b, axis=0)
print('按行合并后的结果')
print(c)
print('合并后数据维度', c.shape)
# 按列合并
d = np.append(a, b, axis=1)
print('按列合并后的结果')
print(d)
print('合并后数据维度', d.shape)

按行合并后的结果
[[0 1]
  [2 3]
  [0 1]
  [2 3]]
合并后数据维度 (4, 2)
按列合并后的结果
[[0 1 0 1]
  [2 3 2 3]]
合并后数据维度 (2, 4)

##########################沿指定轴连接数组或矩阵：#####################################
import numpy as np
a =np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
c = np.concatenate((a, b), axis=0)
print(c)
d = np.concatenate((a, b.T), axis=1)
print(d)

[[1 2]
  [3 4]
  [5 6]]
[[1 2 5]
  [3 4 6]]

##############################沿指定轴堆叠数组或矩阵：#######################################
import numpy as np
a =np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(np.stack((a, b), axis=0))

[[[1 2]
  [3 4]]

[[5 6]
  [7 8]]]

##############################矩阵转置######################################
np1.T
np1.transpose()
