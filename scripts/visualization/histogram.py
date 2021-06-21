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

csvfiles=['01_Mushroom.csv', '02_Bicycle.csv', '03_Camel.csv', '04_Camera.csv', '05_Chicken.csv', '06_Dinosaur.csv', '07_Balloon.csv', '08_Glasses.csv', '09_Gorilla.csv', '10_Volcano.csv', '11_Asparagus.csv', '12_Pizza.csv', '13_Railroad.csv', '14_Scissors.csv', '15_Shovel.csv', '16_Flamingo.csv', '17_Suitcase.csv', '18_Telephone.csv', '19_Ladder.csv', '20_Toothbrush.csv', '21_Hammer.csv', '22_Coconut.csv', '23_Wallet.csv', '24_Pineapple.csv', '25_Cactus.csv']

fig, axes = plt.subplots(nrows=5, ncols=5, figsize=(12, 8))
width = 0.4

for i in range(5):
    for j in range(5):
        # get transcript word 
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
    
fig.suptitle('Top 5 keywords across Confrontational Naming Tasks for Survey A')
plt.tight_layout()
plt.show()