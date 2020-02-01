import numpy as np
from pandas import Series, DataFrame
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("edit3.csv")
rslt = data.loc[data['COMPANY PLCD'] == "Intel, Bangalore"] 
rslt.to_csv('file1.csv')
data1 = pd.read_csv("file1.csv")
labels=[2012,2013,2014,2015,2016,2017,2018]
explode = (0, 0, 0, 0,0,0,0.1)
group = data1.groupby('YEAR', as_index = False).count()
a=group[["BRANCH", "YEAR"]]
print (a)
patches, texts = plt.pie(a['BRANCH'], explode,  shadow=True, startangle=90)
plt.legend(patches, labels, loc="best")
plt.title("percentage of students placed in INTEL per year")
plt.axis('equal')
plt.tight_layout()
plt.savefig("intel_pie.jpg")
plt.show()