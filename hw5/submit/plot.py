import matplotlib.pyplot as plt
import math
import numpy as np

processors = [1, 2, 4, 8]

strong_scaling_exec_time = [1.442221e+01, 9.165723e+00, 1.172163e+01, 1.178163e+01]
strong_scaling_efficiency = []

for index, proc in enumerate(processors):

	strong_scaling_efficiency.append(strong_scaling_exec_time[0] / (proc * strong_scaling_exec_time[index]) )


print("Strong Scaling Efficiency", strong_scaling_efficiency)
# m1, c1 = 0.1, 2.0
# m2, c2 = 2.0, -3.0
# xi = (c1 - c2) / (m2 - m1)
# yi = m1 * xi + c1
plt.axvline(x = 1, color='#bfbfbf', linestyle='--', ymin=0, ymax = 1.0)
plt.axvline(x = 2, color='#bfbfbf', linestyle='--', ymin=0, ymax = 0.7867469920267065)
plt.axvline(x = 4, color='#bfbfbf', linestyle='--', ymin=0, ymax = 0.3075982179952788)
plt.axvline(x = 8, color='#bfbfbf', linestyle='--', ymin=0, ymax = 0.15301586028418818)
plt.plot(processors, strong_scaling_efficiency, "-ob", label="Linear Fit")

#plt.axvline(y = strong_scaling_efficiency, color='gray', linestyle='--')
plt.xlabel("№ threads")
plt.ylabel("efficiency")
# plt.xticks([1,2,3,4])
plt.title("strong-scaling parallel efficiency")
plt.ylim(0, 1.1)
plt.savefig("plot.png")
plt.close()
