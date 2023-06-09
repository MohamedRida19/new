import numpy as np 
import matplotlib.pyplot as plt

x = np.array([1,7,4,71])
y = np.array([1,11,2,118])
plt.title('6')
plt.subplot(2,3,1)
plt.plot(x,y)

x = np.array([1,5,9,10])
y = np.array([1,6,4,14])
plt.subplot(2,3,2)
plt.title('19')
plt.plot(x,y)

plt.suptitle('new branch')
plt.show()







