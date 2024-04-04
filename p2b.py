import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Melasales.csv")
df.plot(kind = 'bar', x='days')
plt.xlabel('days')
plt.ylabel('sales in rupees')
plt.show()
