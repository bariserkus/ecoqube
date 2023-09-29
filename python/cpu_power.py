import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
du = 0.01

t1 = np.arange(0.0, 0.5, du)
s1 = np.arange(0.0, 0.5, du)

t2 = np.arange(0.5+du, 1.0, du)
s2 = np.arange(0.5+du, 1.0, du)

lt1 = len(t1)
lt2 = len(t2)


for i in range(lt1):
    if t1[i] <= 0.5:
        s1[i] = 69 + 328.338*t1[i] + 60.1008
    elif t1[i] > 0.5:
        s1[i] = 69 + 202.707*t1[i] + 33.91
     
for j in range(lt2):
    if t2[j] <= 0.5:
        s2[j] = 69 + 328.338*t2[j] + 60.1008
    elif t2[j] > 0.5:
        s2[j] = 69 + 202.707*t2[j] + 33.91

fig, ax = plt.subplots(1)
plt.xlim([0, 1])
plt.ylim([0, 300])
ax.grid()

ax.plot(t1, s1, 'black')
ax.plot(t2, s2, 'black')


ax.set(xlabel='Utilization, $u$', ylabel='Power Consumption, $P_\mathrm{s}$ (W)')


fig.savefig("../summary/figures/fig04.pdf")
plt.show()
