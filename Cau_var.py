import numpy as np

a = [397,
     323,
     257,
     141,
     349
     ]

a_mean = np.mean(a)  # 求均值
a_std = np.std(a,ddof=1)  # 求标准差


print("平均值为：%f" % a_mean)
print("标准差为:%f" % a_std)