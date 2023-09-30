import matplotlib.pyplot as plt

xvals1 = [i for i in range(0, 10)]
yvals1 = [i**2 for i in range(0, 10)]
xvals2 = [i for i in range(11, 20)]
yvals2 = [i**3 for i in range(11, 20)]

f, ax = plt.subplots(1)
ax.plot(xvals1, yvals1)
ax.plot(xvals2, yvals2)