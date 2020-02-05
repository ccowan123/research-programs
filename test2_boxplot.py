import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import cv2
A = [53.50508734, 54.36035041, 55.08213072, 54.51467963, 56.24833217, 55.3099335, 59.58925101, 54.92515689, 56.93582875, 55.29353029, 54.69088455, 55.25679248];
B = [54.43714216, 55.4931446, 54.47022648, 50.89394586, 54.14384934, 53.27506735, 54.33138715, 55.27150711, 54.08970518, 54.85994398, 55.04258134, 54.3207883, 54.3358393, 52.50005857, 54.72625756, 53.49036315];

box_plot = [A, B];
fig = plt.figure(1, figsize=(9,6))
ax = fig.add_subplot(111)
bp = ax.boxplot(box_plot)

#editing the axis
ax.set_xticklabels(['Group A', 'Group B'])
plt.title('Test 2')
plt.text(1.8, 58, 'P-Value: 0.0061')

for i in range(2):
    y = box_plot[i]
    x = np.random.normal(1+i, 0.04, size=len(y))
    plt.plot(x, y, 'r.', alpha=0.2)

plt.show()

fig.savefig('fig2.png', bbox_inches='tight')