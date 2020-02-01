import numpy as np
from pandas import Series, DataFrame
import pandas as pd
import matplotlib.pyplot as plt

def get_data(fname):
    df = pd.read_csv(fname)
    df['BRANCH'] = df['BRANCH'].str.strip()
    return df
def plot_stack_chart(data):

    branch_year = data.groupby(['BRANCH', 'YEAR'], as_index = False).count()[['BRANCH', 'YEAR', 'COMPANY PLCD']]
    df = branch_year.pivot(index = 'YEAR', columns = 'BRANCH', values = 'COMPANY PLCD')
    ax=df.plot(kind = 'bar', stacked = True, legend=False, figsize=(15,10))
    patches, labels = ax.get_legend_handles_labels()
    ax.legend(patches, labels, loc='upper right')
    plt.title("Placement statistics per year" ,fontsize=20)
    plt.xlabel("Year", fontsize=15)
    plt.ylabel("No.of students placed from each branch", fontsize=15)
    plt.ylim(0,225,25)
    plt.tight_layout()
    
    plt.savefig("graph1.jpg")
    
    plt.show()
def create_stack_graph():
    data1 = get_data('edit3.csv')
    plot_stack_chart(data1)

create_stack_graph()
