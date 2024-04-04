import matplotlib.pyplot as plt
temp = [20.3,32.2,15,33.9,10,]
date = ['23/2','31/3','26/6','15/9','11/12']
plt.plot(date,temp)
plt.xlabel('date')
plt.ylabel('temp')
plt.grid()
plt.title('temperature record')
plt.show()
