import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv("min_max.csv", usecols = ["ANNUAL - MIN","ANNUAL - MAX"])
print(data)
df=pd.DataFrame(data)
df.plot(kind='hist',title='annual season temperature',color=['yellow','red'])
plt.xlabel("temperature")
plt.ylabel("number of times")
plt.show()
