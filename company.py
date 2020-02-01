import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv("edit3.csv")
data=data.dropna()
d=data.groupby(['COMPANY PLCD']).count()
highest=d.sort_values(["YEAR"],ascending=False)
bar_graph=highest.head(12)
bar_graph1=bar_graph.sort_values(["YEAR"],ascending=True)
bar_graph1["YEAR"].plot(kind='barh', color='blue',figsize=(15,10))
plt.xlabel('Most Visited company', fontsize=15)
plt.ylabel('No.of students Placed', fontsize=15)
plt.title("Most Visited Companies to MSOIS", fontsize=20)
plt.xlim(0,120,10)
plt.savefig("company.jpg")
plt.tight_layout()
plt.show()