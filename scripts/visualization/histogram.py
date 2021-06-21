import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
import time
from nltk import FreqDist
import numpy as np 

def get_variables(transcript):
    # get transcript split
    transcript=transcript.split()
    # get top 10 word counts
    unique=list(set(transcript))
    counts=dict()
    for k in range(len(unique)):
        counts[unique[k]]=transcript.count(unique[k])
        
    counts=list(sorted(counts.items(), key=lambda x: x[1], reverse=True))
    x=list()
    y=list()
    for i in range(5):
        x.append(counts[i][0])
        y.append(counts[i][1])
    
    return x, y

def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')
                
transcript='hello this is a test only a test it is an incredibly variables transcript totally is cool yup yes good cool totally yes total night'

fig, axes = plt.subplots(nrows=5, ncols=5, figsize=(12, 8))
width = 0.4

for i in range(5):
    print(i)
    for j in range(5):
        print(j)
        x, y = get_variables(transcript)
        axes[i, j].bar(x,y, color='navy', width=width)
        axes[i, j].set_title(str(i)+' '+str(j))

for ax in axes.flat:
    # xlabel='keyword',
    ax.set(ylabel='counts')
    ax.tick_params(axis='x', rotation=90)
    
    
fig.suptitle('Top 5 keywords across Confrontational Naming Tasks for Survey A')
plt.tight_layout()
plt.show()
