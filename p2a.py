import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Melasales.csv")
df.plot(kind = 'line', color = ['blue','red','brown'])
plt.xlabel('day')
plt.ylabel('sales in rupees')
plt.show()
