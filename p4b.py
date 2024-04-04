import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("res.csv")
df.plot(kind='box',x='year',vert=False,patch_artist=True)
plt.xlabel('year')
plt.ylabel('rating')
plt.show()
