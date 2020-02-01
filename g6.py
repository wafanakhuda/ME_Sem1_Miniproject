import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('gedit.csv')
df1=df[864:1034]
group = df1.groupby('BRANCH').count()
group["COMPANY PL"].plot(kind='bar', color='rosybrown')
plt.ylabel('PLACED', fontsize=10)
plt.xlabel('BRANCH', fontsize=10)
plt.title('Students placed in 2017 ')
plt.tight_layout()
plt.savefig('g6.jpg')