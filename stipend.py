import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv("edit3.csv")


data=data.dropna()
data.STIPEND = data.STIPEND.astype(float)
data.STIPEND = data.STIPEND.astype(int)
new=data.sort_values(["STIPEND"],ascending=False)

new.to_csv('file4.csv')
df2=pd.read_csv("file4.csv")
df2.head()

a=df2.groupby('STIPEND').count()
a.sort_values(["STIPEND"],ascending=False)
print(a["COMPANY PLCD"])
a["YEAR"].plot(kind="bar", color="red",figsize=(15,10))
plt.ylim(0,150,10)
plt.title("Stipend provided by Companies throughout the Years",fontsize=20)
plt.xlabel("Stipend", fontsize=15)
plt.ylabel("No. of Students", fontsize=15)
plt.savefig("stipend.jpg")
plt.show()