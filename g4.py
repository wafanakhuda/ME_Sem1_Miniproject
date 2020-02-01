import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('gedit.csv')
df1=df[572:714]
group = df1.groupby('BRANCH').count()
group["COMPANY PL"].plot(kind='bar', color='red')
plt.ylabel('PLACED', fontsize=10)
plt.xlabel('BRANCH', fontsize=10)
plt.title(' Students placed in 2015 ')
plt.tight_layout()
plt.savefig('g4.jpg')