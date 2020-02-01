import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('gedit.csv')
df['BRANCH'] = df['BRANCH'].str.strip()
df1=df[1035:1226]
df1.dropna()
group = df1.groupby('BRANCH').count()
group["COMPANY PL"].plot(kind='bar', color='mediumvioletred')
plt.ylabel('PLACED', fontsize=10)
plt.xlabel('BRANCH', fontsize=10)
plt.title('Students placed in 2018 ')
plt.tight_layout()
plt.savefig('g7.jpg')
