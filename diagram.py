import numpy as np 
import matplotlib.pyplot as plt

x = np.array([1,2,4,7])
y = np.array([1,4,2,7])
plt.title('1')
plt.subplot(1,2,1)
plt.plot(x,y)

x = np.array([1,5,9,10])
y = np.array([1,6,4,14])
plt.subplot(1,2,2)
plt.title('2')
plt.plot(x,y)


plt.show()







