import numpy as np 
import matplotlib.pyplot as plt

x= np.array([1,2,3,5])
y = np.array([1,3,2,6])
plt.title('1')
plt.subplot(1,2,1)
plt.plot(x,y)

x = np.array([1,2,3,4])
y = np.array([1,5,2,17])
plt.title('2')
plt.subplot(1,2,2)
plt.plot(x,y)

plt.suptitle("TWIX")
plt.show()