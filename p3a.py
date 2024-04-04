import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv("min_max.csv", usecols = ["ANNUAL - MIN","ANNUAL - MAX"])
print(data)
df=pd.DataFrame(data)
df.plot(kind='hist',y='ANNUAL - MIN',title='annual season temperature')
plt.xlabel("temperature")
plt.ylabel("number of times")
plt.show()
