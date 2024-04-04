import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("res.csv")
df.plot(kind='box',x='year')
plt.xlabel('year')
plt.ylabel('rating')
plt.show()
