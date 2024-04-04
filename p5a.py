import matplotlib.pyplot as plt
import numpy as np
discount=np.array([10,20,30,40,50])
sales_in_rs= np.array([40000,45000,48000,50000,100000])
plt.scatter(x=discount,y=sales_in_rs)
plt.title("discounr vs sales")
plt.xlabel('discount offer')
plt.ylabel('sales in rupees')
plt.show()
