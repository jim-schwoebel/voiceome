import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
import time, math
from nltk import FreqDist
import numpy as np 
import pandas as pd 
from tqdm import tqdm 

def get_variables(transcript):
    # get transcript split
    transcript=transcript.replace('.','').lower()
    transcript=transcript.split()
    # get top 10 word counts
    unique=list(set(transcript))
    counts=dict()
    for k in range(len(unique)):
        counts[unique[k]]=transcript.count(unique[k])
        
    counts=list(sorted(counts.items(), key=lambda x: x[1], reverse=True))
    x=list()
    y=list()
    count=0
    i=0
    while count < 5:  
        if str(counts[i][0]).replace(' ','') in ['nan', 'undefined']:
            i=i+1    
        else:
            x.append(counts[i][0])
            y.append(counts[i][1])
            count=count+1
            i=i+1
    
    return x, y

def get_transcript():
    pass 

csvfiles=['01_plive.csv', '02_fwov.csv', '03_zowl.csv', '04_zulx.csv', '05_vave.csv', '06_kwaj.csv', '07_jome.csv', '08_bwiz.csv', '09_broe.csv', '10_nayb.csv']
fig, axes = plt.subplots(nrows=2, ncols=5, figsize=(12, 8))
width = 0.4

for i in range(2):
    for j in range(5):
        # get transcript word 
        print((i)*5+j)
        csvfile=csvfiles[(i)*5+j]
        data=pd.read_csv(csvfile)
        data=list(data['azure'])
        transcript=''
        for k in tqdm(range(len(data))):
           transcript=transcript+' '+str(data[k])

        x, y = get_variables(transcript)
        axes[i, j].bar(x,y, color='navy', width=width)
        axes[i, j].set_title(csvfiles[(i)*5+j].replace('.csv',''))
        axes[i,j].set_ylim([0,2000])

for ax in axes.flat:
    # xlabel='keyword',
    ax.set(ylabel='counts')
    ax.tick_params(axis='x', rotation=90)
    
fig.suptitle('Top 5 keywords across Nonword Naming Tasks for Survey A')
plt.tight_layout()
plt.show()