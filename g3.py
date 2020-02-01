import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('g.csv')
df1=df[411:571]
group = df1.groupby('BRANCH').count()
group["COMPANY PL"].plot(kind='bar', color='green')
plt.ylabel('PLACED', fontsize=10)
plt.xlabel('BRANCH', fontsize=10)
plt.title('Students placed in 2014 ')
plt.tight_layout()
plt.savefig('g3.jpg')