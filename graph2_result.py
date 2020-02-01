import numpy as np
from pandas import Series, DataFrame
import pandas as pd
import matplotlib.pyplot as plt

def get_data(fname):
    df = pd.read_csv(fname)
    df['BRANCH'] = df['BRANCH'].str.strip()
    df['BE BRANCH'] = df['BE BRANCH'].str.strip()

    return df
def plot_stack_chart(data):

    branch_year = data.groupby(['BE BRANCH', 'BRANCH'], as_index = False).count()[['BE BRANCH', 'BRANCH', 'COMPANY PLCD']]
    df = branch_year.pivot(index = 'BRANCH', columns = 'BE BRANCH', values = 'COMPANY PLCD')
    df.dropna()
    ax=df.plot(kind = 'bar', stacked = True, legend=False, figsize=(15,10))
    patches, labels = ax.get_legend_handles_labels()
    
    ax.legend(patches, labels, loc='upper right', bbox_to_anchor=(1,1))


	
    plt.xlabel("ME Branches", fontsize=15)
    plt.ylabel("Number of students", fontsize=15)
    plt.title("Number of students according to BE branches", fontsize=20)
    plt.tight_layout()
    plt.savefig("graph2.jpg")
    plt.show()
    
def create_stack_graph():
    data1 = get_data('edit3.csv')
    plot_stack_chart(data1)

create_stack_graph()

