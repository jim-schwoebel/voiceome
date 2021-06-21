'''
Code adapted from https://github.com/jim-schwoebel/voicebook/wiki/0.6.-Visualization
'''
import librosa, os, time, shutil, math
from tqdm import tqdm
from pydub import AudioSegment
import numpy as np
import matplotlib.pyplot as plt
from natsort import natsorted

def visualize_data(sample, minimum, maximum):
    difference=maximum-minimum
    delta=difference/10
    bar='==.==.'
    if sample <= minimum:
        # 1 bar
        output=bar
    elif minimum+delta >= sample > minimum:
        # 1 bar
        output=bar
    elif minimum+delta*2 >= sample > minimum+delta:
        # 2 bars
        output=bar*2
    elif minimum+delta*3 >= sample >= minimum+delta*2:
        # 3 bars
        output=bar*3
    elif minimum+delta*4 >= sample > minimum+delta*3:
        # 4 bars
        output=bar*4
    elif minimum+delta*5 >= sample > minimum+delta*4:
        # 5 bars
        output=bar*5
    elif minimum+delta*6 >= sample > minimum+delta*5:
        # 6 bars
        output=bar*6
    elif minimum+delta*7 >= sample > minimum+delta*6:
        # 7 bars
        output=bar*7
    elif minimum+delta*8 >= sample > minimum+delta*7:
        # 8 bards
        output=bar*8
    elif minimum+delta*9 >= sample > minimum+delta*8:
        # 9 bars
        output=bar*9
    elif maximum > sample >= minimum+delta*9:
        # 10 bars
        output=bar*10
    elif sample >= maximum:
        # 10 bars
        output=bar*10
    else:
        print(sample)
        output='error'

    # plot bars based on a min and max 
    return output[0:-1]

def calculate_rmse(filename):
    # synchronous recording 
    y, sr = librosa.load(filename)
    rmse_features=librosa.feature.rmse(y)[0]*1000
    print(rmse_features)
    return rmse_features

def plot_sample(filename):
    # break up audio file into 20 millisecond intervals
    startdir=os.getcwd()
    rmse_features=calculate_rmse(filename)
    x=list()
    for i in range(len(rmse_features)):
        x.append(i)
        
    os.chdir(startdir)
    try:
        os.chdir('plots')
    except:
        os.mkdir('plots')
        os.chdir('plots')
        
    plt.title('RMS Energy vs. time (20 ms windows)')
    plt.plot(x, rmse_features, 'o', color='black')
    plt.xlabel('Time (20 ms intervals)')
    plt.ylabel('RMS energy (RMSE)')
    plt.savefig(filename[0:-4]+'.png')
    plt.clf()

    return x, rmse_features
    
# get all wave files
curdir=os.getcwd()
listdir=os.listdir()
wavfiles=list()
for i in range(len(listdir)):
    if listdir[i].endswith('.wav'):
        wavfiles.append(listdir[i])

wavfiles=natsorted(wavfiles)
# now plot out RMSE per file to explore if it's a good feature to use
x_list=list()
sample_list=list()
for i in tqdm(range(len(wavfiles))):
    print(wavfiles[i])
    os.chdir(curdir)
    # try:
    x, samples = plot_sample(wavfiles[i])
    x_list.append(x)
    sample_list.append(samples)
    # except:
        # print('error')
    # time.sleep(2)

# create proper subplot number
plt.figure()
plt.suptitle("RMS vs. time across various words", fontsize=16)
for i in range(len(x_list)):
    plt.subplot(math.ceil(len(x_list)/5),5, i+1)
    plt.plot(x_list[i], sample_list[i])
    plt.xlabel('Time (20 ms intervals)')
    plt.ylabel('RMS')
    plt.title(wavfiles[i][0:-4])

plt.subplots_adjust(left=0.12, bottom=0.11, right=0.90, top=0.93, wspace=0.36, hspace=0.61)
plt.savefig('allplots.png')
plt.show()
    
