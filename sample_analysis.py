'''
================================================ 
            VOICEOME REPOSITORY                     
================================================ 

repository name: Voiceome 
repository version: 1.0 
repository link: https://github.com/jim-schwoebel/voiceome 
author: Jim Schwoebel 
author contact: jim.schwoebel@gmail.com 
description: A set of scripts related to the Voiceome Study, a clinical study for speech and language biomarker research N=6000+ 
license category: opensource 
license: Apache 2.0 license 
organization name: Sonde Health Inc. 
location: Boston, MA 
website: https://sondehealth.com 
release date: 2021-06-13 

This code (Voiceome) is hereby released under a Apache 2.0 license license. 

For more information, check out the license terms below. 

================================================ 
              DESCRIPTION                    
================================================ 

Voiceome.py 

A simple set of scripts to help with various tasks related to the Voiceome 
dataset. This includes:
- cleaning audio to mono16Hz  
- featurizing audio 
- querying reference ranges as published in the paper 
- transcribing audio files with Microsoft Azure (given environment variables)
- defining quality criteria for each speech task / calculating metrics

Thank you for your interest in our work!

================================================ 
                LICENSE TERMS                      
================================================ 

Copyright 2021 by Jim Schwoebel.
Licensed under the Apache License, Version 2.0 (the "License"); 
you may not use this file except in compliance with the License. 
You may obtain a copy of the License at 

     http://www.apache.org/licenses/LICENSE-2.0 

Unless required by applicable law or agreed to in writing, software 
distributed under the License is distributed on an "AS IS" BASIS, 
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and 
limitations under the License. 
'''

######################################################################
##                           IMPORTS                               ##
######################################################################
import sys, os, json, time, shutil, argparse, random, math
import matplotlib.pyplot as plt
import soundfile as sf
import numpy as np
from pyvad import vad, trim, split
import pandas as pd
from datetime import datetime
import librosa
import matplotlib.pyplot as plt
import numpy as np
import difflib
import nltk
from nltk import word_tokenize
import speech_recognition as sr
from tqdm import tqdm
from beautifultable import BeautifulTable

directory=os.getcwd()

######################################################################
##                     QUALITY METRICS                              ##
######################################################################

def extract_transcript(transcript):
    try:
        return transcript.split(') ')[1]
    except:
        return ''

def animal_features(transcript, animal_list):
    transcript=transcript.lower().split(' ')
    count=0
    for j in range(len(transcript)):
        if transcript in animal_list:
            count=count+1
    return count 

def letterf_features(transcript):
    transcript=transcript.lower().split(' ')
    count=0
    words=list()
    for j in range(len(transcript)):
        if transcript[j].startswith('f') and transcript[j] not in words:
            count=count+1
            words.append(transcript[j])
    return count

def passage_features(transcript, reference):
    # similarity (https://stackoverflow.com/questions/1471153/string-similarity-metrics-in-python)
    # similarity
    seq=difflib.SequenceMatcher(a=transcript.lower(), b=reference.lower())
    # longest matching string
    match = seq.find_longest_match(0, len(transcript), 0, len(reference))
    
    return 100*seq.ratio() #, match.size, match.a, match.b

def bnt_features(transcript):
    # use 'deepspeech_dict' setting in Allie ML framework
    transcript=transcript.lower().split()
    # print(transcript)

    counts=0
    if 'mushroom' in transcript:
        counts=counts+1
    if 'bicycle' in transcript:
        counts=counts+1
    if 'camel' in transcript:
        counts=counts+1
    if 'camera' in transcript:
        counts=counts+1
    if 'chicken' in transcript:
        counts=counts+1
    if 'dinosaur' in transcript or 'brontosaurus' in transcript or 'brontosaur' in transcript:
        counts=counts+1
    if 'balloon' in transcript or 'bullion' in transcript:
        counts=counts+1
    if 'glasses' in transcript or 'spectacles' in transcript or 'bifocals' in transcript:
        counts=counts+1
    if 'gorilla' in transcript:
        counts=counts+1
    if 'volcano' in transcript:
        counts=counts+1
    if 'asparagus' in transcript:
        counts=counts+1
    if 'pizza' in transcript or 'piazza' in transcript:
        counts=counts+1
    if 'railroad' in transcript or 'track' in transcript or 'tracks' in transcript:
        counts=counts+1
    if 'scissors' in transcript:
        counts=counts+1
    if 'shovel' in transcript:
        counts=counts+1
    if 'flamingo' in transcript:
        counts=counts+1
    if 'suit' in transcript or 'suitcase' in transcript or 'case' in transcript:
        counts=counts+1
    if 'telephone' in transcript or 'phone' in transcript:
        counts=counts+1
    if 'later' in transcript or 'ladder' in transcript:
        counts=counts+1
    if 'toothbrush' in transcript or 'tooth' in transcript or 'brush' in transcript:
        counts=counts+1
    if 'coconut' in transcript or 'cocoanut' in transcript:
        counts=counts+1
    if 'while' in transcript or 'wallet' in transcript:
        counts=counts+1
    if 'pineapple' in transcript or 'pine' in transcript:
        if 'pine' in transcript and 'apple' in transcript:
            counts=counts+1
        else:
            counts=counts+1
    if 'cactus' in transcript:
        counts=counts+1

    return counts 

def nonword_features(transcript):
    # use 'deepspeech_nodict' setting in Allie ML framework
    transcript=transcript.lower().split()
    # print(transcript)
    counts=0
    if 'plive' in transcript or 'pli' in transcript or 'live' in transcript or 'pliv' in transcript or 'life' in transcript or 'plife' in transcript:
        counts=counts+1
    if 'for' in transcript or 'flove' in transcript:
        counts=counts+1
    if 'zowl' in transcript or 'thou' in transcript or 'zone' in transcript or 'zoul' in transcript:
        counts=counts+1
    if 'zox' in transcript or 'zoolix' in transcript or 'filks' in transcript:
        counts=counts+1
    if 'they' in transcript or 'tave' in transcript or 'wall' in transcript or 'vave' in transcript:
        counts=counts+1
    if 'kwaj' in transcript or 'quash' in transcript or 'quatda' in transcript:
        counts=counts+1
    if 'jom' in transcript or 'joam' in transcript or 'dram' in transcript or 'jome' in transcript:
        counts=counts+1
    if 'boys' in transcript or 'boyl' in transcript or 'bwils' in transcript or 'bwiz' in transcript:
        counts=counts+1
    if 'broe' in transcript or 'brow' in transcript:
        counts=counts+1
    if 'nay' in transcript or 'nayb' in transcript or 'nab' in transcript or 'a' in transcript:
        counts=counts+1

    return counts 

######################################################################
##                    QUERYING DATABASES                            ##
######################################################################

def mean_std(list_):
    array_=np.array(list_)
    return np.mean(array_), np.std(array_)

def get_reference(task, feature_embedding, feature, agegender, basedir):

    curdir=os.getcwd()

    os.chdir(basedir)
    os.chdir('data')
    os.chdir('references')

    # go to proper location
    if task in ['microphone_task', 'freespeech_task', 'picture_task', 'category_task',
                'letterf_task', 'paragraph_task', 'ahh_task', 'papapa_task', 'pataka_task',
                'mandog_task', 'tourbus_task', 'diagnosis_task', 'medication_task']:
        os.chdir('main_tasks')

    elif task in ['mushroom_task', 'bicycle_task', 'camel_task', 'camera_task', 'chicken_task', 
                  'dinosaur_task', 'balloon_task', 'glasses_task', 'gorilla_task', 'volcano_task', 
                  'asparagus_task', 'pizza_task', 'railroad_task', 'scissors_task', 'shovel_task', 
                  'flamingo_task', 'suitcase_task', 'telephone_task', 'ladder_task', 'toothbrush_task', 
                  'hammer_task', 'coconut_task', 'wallet_task', 'pineapple_task', 'cactus_task']:
        os.chdir('bnt_task')

    elif task in ['plive_task', 'broe_task', 'jome_task', 'zulx_task', 'zowl_task', 
                  'vave_task', 'fwov_task', 'nayb_task', 'kwaj_task', 'bwiz_task']:
        os.chdir('nonword_task')

    # 00. Microphone check task = 'microphone_task'
    if task == 'microphone_task': 
        data=json.load(open('00_mic_check.json'))

    # 01. Free speech task = 'freespeech_task'
    elif task == 'freespeech_task':
        data=json.load(open('01_free_speech.json'))

    # 02. Picture description task = 'picture_task'
    elif task == 'picture_task':
        data=json.load(open('02_picture_description.json'))

    # 03. Category naming task = 'category_task'
    elif task == 'category_task':
        data=json.load(open('03_animal_naming.json'))

    # 04. Letter {FAS} Tasks = 'leterf_task'
    elif task == 'letterf_task':
        data=json.load(open('04_letter_f_naming.json'))

    # 05. Paragraph reading task = 'paragraph_task'
    elif task == 'paragraph_task':
        data=json.load(open('05_caterpillar_reading.json'))

    # 06. Sustained phonation ('ahh') = 'ahh_task'
    elif task == 'ahh_task':
        data=json.load(open('06_sustained_ahh.json'))

    # 07. Pa pa pa task = 'papapa_task'
    elif task == 'papapa_task':
        data=json.load(open('07_pa_pa_pa.json'))

    # 08. Pa taska ka task - 'pataka_task'
    elif task == 'pataka_task':
        data=json.load(open('08_pa_ta_ka.json'))

    # 09. Confrontational naming task (different images) - 'bnt_task'
    elif task == 'mushroom_task':
        data=json.load(open('01_Mushroom.json'))
    elif task == 'bicycle_task':
        data=json.load(open('02_Bicycle.json'))
    elif task == 'camel_task':
        data=json.load(open('03_Camel.json'))
    elif task == 'camera_task':
        data=json.load(open('04_Camera.json'))
    elif task == 'chicken_task':
        data=json.load(open('05_Chicken.json'))
    elif task == 'dinosaur_task':
        data=json.load(open('06_Dinosaur.json'))
    elif task == 'balloon_task':
        data=json.load(open('07_Balloon.json'))
    elif task == 'glasses_task':
        data=json.load(open('08_Glasses.json'))
    elif task == 'gorilla_task':
        data=json.load(open('09_Gorilla.json'))
    elif task == 'volcano_task':
        data=json.load(open('10_Volcano.json'))
    elif task == 'asparagus_task':
        data=json.load(open('11_Asparagus.json'))
    elif task == 'pizza_task':
        data=json.load(open('12_Pizza.json'))
    elif task == 'railroad_task':
        data=json.load(open('13_Railroad.json'))
    elif task == 'scissors_task':
        data=json.load(open('14_Scissors.json'))
    elif task == 'shovel_task':
        data=json.load(open('15_Shovel.json'))
    elif task == 'flamingo_task':
        data=json.load(open('16_Flamingo.json'))
    elif task == 'suitcase_task':
        data=json.load(open('17_Suitcase.json'))
    elif task == 'telephone_task':
        data=json.load(open('18_Telephone.json'))
    elif task == 'ladder_task':
        data=json.load(open('19_Ladder.json'))
    elif task == 'toothbrush_task':
        data=json.load(open('20_Toothbrush.json'))
    elif task == 'hammer_task':
        data=json.load(open('21_Hammer.json'))
    elif task == 'coconut_task':
        data=json.load(open('22_Coconut.json'))
    elif task == 'wallet_task':
        data=json.load(open('23_Wallet.json'))
    elif task == 'pineapple_task':
        data=json.load(open('24_Pineapple.json'))
    elif task == 'cactus_task':
        data=json.load(open('25_Cactus.json'))


    # 10. Nonword task (different nonwords) - 'nonword_task'
    elif task == 'plive_task':
        data=json.load(open('01_Plive.json'))
    elif task == 'broe_task':
        data=json.load(open('02_Fwov.json'))
    elif task == 'jome_task':
        data=json.load(open('03_Zowl.json'))
    elif task == 'zulx_task':
        data=json.load(open('04_Zulx.json'))
    elif task == 'zowl_task':
        data=json.load(open('05_Vave.json'))
    elif task == 'vave_task':
        data=json.load(open('06_Kwaj.json'))
    elif task == 'fwov_task':
        data=json.load(open('07_Jome.json'))
    elif task == 'nayb_task':
        data=json.load(open('08_Bwiz.json'))
    elif task == 'kwaj_task':
        data=json.load(open('09_Broe.json'))
    elif task == 'bwiz_task':
        data=json.load(open('10_Nayb.json'))

    # 11. Immediate recall task -  'mandog_task' or 'tourbus_task'
    elif task == 'mandog_task':
        data=json.load(open('45_repeat_mandog.json'))

    elif task == 'tourbus_task':
        data=json.load(open('47_repeat_schoolbus.json'))

    # 12. Spoken diagnosis task - 'diagnosis_task'
    elif task == 'diagnosis_task':
        data=json.load(open('48_diagnosis_task.json'))

    # 13. Spoken medication task - 'medication_task'
    elif task == 'medication_task':
        data=json.load(open('49_medication_task.json'))

    # calculate possible featurestypes here 
    os.chdir(basedir)
    os.chdir('data')
    os.chdir('options')
    options=json.load(open('feature_options.json'))
    feature_embeddings=list(options)
    features=list()
    for i in range(len(feature_embeddings)):
        features=features+options[feature_embeddings[i]]

    # print(features)

    # age options
    agegenders=['TwentiesMale', 'TwentiesFemale', 'ThirtiesMale', 'ThirtiesFemale', 'FourtiesMale]', 'FourtiesFemale', 'FiftiesMale', 'FiftiesFemale', 'SixtiesMale', 'SixtiesFemale', 'AllAgesGenders']

    os.chdir(curdir)

    # return results 
    if feature_embedding in feature_embeddings and feature in features and agegender in agegenders:
        return data[feature_embedding][feature][agegender]
    else:
        return 'ERROR - FeatureType, Feature, or Age not recognize. Please check these settings and try again.'

def reference_task_embedding(task, feature_embedding, agegender, basedir):
    # get all options 
    os.chdir(basedir)
    os.chdir('data')
    os.chdir('options')

    feature_options=json.load(open('feature_options.json'))
    feature_embeddings=list(feature_options)

    agegender_options=json.load(open('agegender_options.json'))
    agegenders=agegender_options['AgeGenderOptions']

    names=list()
    means=list()
    stds=list()
    ages=list()
    samplenums=list()

    if feature_embedding in feature_embeddings and agegender in agegenders:
        features=feature_options[feature_embedding]

        for i in range(len(features)):
            data=get_reference(task, feature_embedding, features[i], agegender, basedir)
            names.append(features[i])
            means.append(data['AverageValue'])
            stds.append(data['StdValue'])
            ages.append(agegender)
            samplenums.append(data['SampleNumber'])

    elif feature_embedding not in feature_embeddings:
        print('ERROR - [%s] is not a recognized feature embedding'%(feature_embedding))
    elif agegender not in agegenders:
        print('ERROR - [%s] is not a recognized age and gender'%(agegender))
       
    return names, means, stds, ages, samplenums

def reference_feature_across_tasks(feature_embedding, feature, agegender, basedir):
    # get all options 
    os.chdir(basedir)
    os.chdir('data')
    os.chdir('options')

    feature_options=json.load(open('feature_options.json'))
    feature_embeddings=list(feature_options)        

    agegender_options=json.load(open('agegender_options.json'))
    agegenders=agegender_options['AgeGenderOptions']

    task_options=json.load(open('task_options.json'))
    tasks=task_options['AllTasks']

    names=list()
    means=list()
    stds=list()
    ages=list()
    samplenums=list()

    if agegender in agegenders and feature_embedding in feature_embeddings:
        features=feature_options[feature_embedding]

        for i in range(len(tasks)):
            data=get_reference(tasks[i], feature_embedding, feature, agegender, basedir)
            names.append(tasks[i])
            means.append(data['AverageValue'])
            stds.append(data['StdValue'])
            ages.append(agegender)
            samplenums.append(data['SampleNumber'])

    elif feature_embedding not in feature_embeddings:
        print('ERROR - [%s] is not a recognized feature embedding'%(feature_embedding))
    elif agegender not in agegenders:
        print('ERROR - [%s] is not a recognized age and gender'%(agegender))
       
    return names, means, stds, ages, samplenums

def visualize_bar(feature, feature_embedding, names, means, stds, agegender, basedir, show):
    os.chdir(basedir)
    os.chdir('data')
    os.chdir('visualizations')
    plt.title(agegender)
    plt.bar(names, means, yerr=stds)
    plt.xticks(rotation='vertical')
    plt.ylabel('%s'%(feature))
    plt.xlabel('Task type')
    plt.tight_layout()
    plt.savefig(feature_embedding+'_'+feature+'.png')
    if show == True:
        plt.show()
    os.chdir(basedir)

def visualize_bar_cohorts(feature, feature_embedding, names, means_1, stds_1, agegender_1, means_2, stds_2, agegender_2, basedir, show):
    os.chdir(basedir)
    os.chdir('data')
    os.chdir('visualizations')

    labels = names
    men_means = means_1
    women_means = means_2

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, men_means, width, label=agegender_1)
    rects2 = ax.bar(x + width/2, women_means, width, label=agegender_2)

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel(feature)
    ax.set_title(agegender_1 + ' | ' + agegender_2)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    plt.xticks(rotation='vertical')

    fig.tight_layout()
    plt.savefig(feature_embedding+'_'+feature+'_'+agegender_1+'_'+agegender_2+'.png')

    if show==True:
        plt.show()
    os.chdir(basedir)

######################################################################
##                           LOAD SETTINGS                          ##
######################################################################

settings=json.load(open('settings.json'))

# specify azure settings 
os.environ['AZURE_SPEECH_KEY']=settings['AzureKey']
os.environ['AZURE_SPEECH_RECOGNITION_LANGUAGE']='en-US'
os.environ['AZURE_REGION']='East-US'

# all other settings
basedir=os.getcwd()
transcript_engine=settings['TranscriptEngine']
feature_embedding=settings['FeatureEmbedding']
featuretype=settings['FeatureType']
task=settings['Task']
clean_audio=settings['CleanAudio']
agegender = settings['DefaultAgeGender']

######################################################################
##                           MAIN SCRIPT                           ##
######################################################################

# get reference 
print(feature_embedding + ' - ' + featuretype)
data=get_reference(task, feature_embedding, featuretype, agegender, basedir)
table = BeautifulTable()
table.columns.header = ["Task", "FeatureType", "Feature", "AgeGender", "Average", "Standard Deviation", "Sample Number"]
table.rows.append([task, feature_embedding, featuretype, agegender, data['AverageValue'], data['StdValue'], data['SampleNumber']])
print(table)

# get reference by embedding
names, means, stds, ages, samplenums =reference_task_embedding(task, feature_embedding, agegender, basedir)
table = BeautifulTable()
table.columns.header = ["Task", "FeatureType", "Feature", "AgeGender", "Average", "Standard Deviation", "Sample Number"]
for i in range(len(means)):
    table.rows.append([task, feature_embedding, names[i], agegender, means[i], stds[i], samplenums[i]])
print(table)

# get reference by embedding
names, means, stds, ages, samplenums =reference_feature_across_tasks(feature_embedding, featuretype, 'TwentiesMale', basedir)
table = BeautifulTable()
table.columns.header = ["Task", "FeatureType", "Feature", "AgeGender", "Average", "Standard Deviation", "Sample Number"]
for i in range(len(means)):
    table.rows.append([task, feature_embedding, names[i], agegender, means[i], stds[i], samplenums[i]])
print(table)

# visualize these as a bar chart 
visualize_bar(featuretype, feature_embedding, names, means, stds, 'TwentiesMale', basedir, False)

names_2, means_2, stds_2, ages_2, samplenums =reference_feature_across_tasks(feature_embedding, featuretype, 'TwentiesFemale', basedir)
visualize_bar_cohorts(featuretype, feature_embedding, names, means, stds, 'TwentiesMale', means_2, stds_2, 'TwentiesFemale', basedir, False)

######################################################################
##                 TEST SURVEY A DATA ANALYSIS                      ##
######################################################################

# ## do analysis 
os.chdir(basedir)
os.chdir('data')
os.chdir('test')
g=pd.read_csv('data.csv')
labels=list(g)

for i in range(len(labels)):
    if labels[i].lower().find('caterpillar') > 0:
        caterpillar=labels[i]

fox=g['Please click the start button and then say:\n\n"The quick brown fox jumps over the lazy dog."\n\nYou may press the Stop button if you finish before the timer runs out.']
memory=g['Tell us about a recent happy memory based on experiences from the past month.']
picture=g['Tell us everything you see going on in this picture.\n\n<center>![Aphasia image](http://www.neurolex.co/uploads/alphasia.png)</center>']
animals=g['Category: ANIMALS. Name all the animals you can think of as quickly as possible before the time elapses below.']
letterf=g['Letter: F. Name all the words beginning with the letter F you can think of as quickly as possible before the time elapses below.']
passage=g[caterpillar]
mandog=g['Please repeat back what you just heard as accurately as possible. You may press the stop button if you finish before the timer runs out.']
tourbus=g['Please repeat back what you just heard as accurately as possible. You may press the stop button if you finish before the timer runs out..1']

# get transcripts
transcript=extract_transcript('(nlx-35ec5930-a10d-11ea-ad75-47afc39b88d6 00:00:59.90) I spent some time recently in the back garden with my dogs.  Um, it was really nice because we just relaxed and sat out there. It was a sunny day. It had been raining a lot recently and it was the first sunny day. So we got to sit out and relax. My family were also there and it was a really enjoyable afternoon.  Also, we cook together later in the day, so that was enjoyable as well.  ')

# passage references
fox_passage="The Quick Brown Fox jumps over the lazy dog."
caterpillar_passage="Do you like amusement parks? Well, I sure do. To amuse myself, I went twice last spring. My most MEMORABLE moment was riding on the Caterpillar, which is a gigantic roller coaster high above the ground. When I saw how high the Caterpillar rose into the bright blue sky I knew it was for me. After waiting in line for thirty minutes, I made it to the front where the man measured my height to see if I was tall enough. I gave the man my coins, asked for change, and jumped on the cart. Tick, tick, tick, the Caterpillar climbed slowly up the tracks. It went SO high I could see the parking lot. Boy was I SCARED! I thought to myself, â€œThereâ€™s no turning back now.â€ People were so scared they screamed as we swiftly zoomed fast, fast, and faster along the tracks. As quickly  as it started, the Caterpillar came to a stop. Unfortunately, it was time to pack the car and drive home. That night I dreamt of the wild ride on the Caterpillar. Taking a trip to the amusement park and riding on the Caterpillar was my MOST memorable moment ever!"
mandog_passage="the man saw the boy that the dog chased"
tourbus_passage="the tour bus is coming into the town to pick up the people from the hotel to go swimming."

# print(transcript)
print('Fox passage')
fox_metrics=list()
for i in range(len(fox)):
    transcript=extract_transcript(fox[i])
    metric=passage_features(transcript, fox_passage)
    fox_metrics.append(metric)

mean_, std_=mean_std(fox_metrics)
print(mean_)
print('+/- %s'%(str(std_)))

# print(transcript)
print('Paragraph - caterpillar')
caterpillar_metrics=list()
for i in range(len(passage)):
    transcript=extract_transcript(passage[i])
    metric=passage_features(transcript, caterpillar_passage)
    caterpillar_metrics.append(metric)

mean_, std_=mean_std(caterpillar_metrics)
print(mean_)
print('+/- %s'%(str(std_)))

# print(transcript)
print('Recall - mandog')
# recall_mandog=g['Please listen carefully to the following audio clip once.\n\n[autoplay](https://s3.amazonaws.com/www.voiceome.org/data/mandog.mp3)']
mandog_metrics=list()
transcript=extract_transcript(mandog[0])
# recall_transcript=extract_transcript(recall_mandog)
metric=passage_features(transcript, mandog_passage)
mandog_metrics.append(metric)

mean_, std_=mean_std(mandog_metrics)
print(mean_)
print('+/- %s'%(str(std_)))

# print(transcript)
print('Recall - tourbus')
# recall_tourbus=g['Please listen carefully to the following audio clip once.\n\n[autoplay](https://s3.amazonaws.com/www.voiceome.org/data/tourbus.mp3)']
tourbus_metrics=list()
transcript=extract_transcript(tourbus[0])
# recall_transcript=extract_transcript(recall_tourbus[i])
metric=passage_features(transcript, tourbus_passage)
tourbus_metrics.append(metric)

mean_, std_=mean_std(tourbus_metrics)
print(mean_)
print('+/- %s'%(str(std_)))

print('LetterF')
letterf_metrics=list()
for i in range(len(letterf)):
    transcript=extract_transcript(letterf[i])
    print(transcript)
    metric=letterf_features(transcript)
    letterf_metrics.append(metric)

mean_, std_=mean_std(letterf_metrics)
print(mean_)
print('+/- %s'%(str(std_)))

animals=g['Category: ANIMALS. Name all the animals you can think of as quickly as possible before the time elapses below.']
animal_metrics=list()

words=list()
stopwords=['um', 'think','hum','oh',"let's",'blue','name','uhm','brown',"i'm",'category','ok','uh',
           'time','ah', 'yeah', 'hey', 'love', 'lot', 'god', 'eh', 'funny', 'sure', 'honey', 'sugar',
           'doc', 'email', 'al', 'il', 'rap', 'count', 'talk', 'check', 'ha', 'anything', 'jack', 'cheap',
           'wow', 'world', 'devil', 'gosh', 'mama', 'please', 'kind', 'king', 'thing', 'sorry', 'see',
           'awesome', 'uhm', 'yellow', 'tail', 'need', 'mu', 'search', 'wizard', 'kid', 'wanna', 'mind', 'girl',
           'giant', 'fire', 'care', 'steak', 'weather', 'war', 'window', 'rock', 'ego', 'word', 'camera', 'square',
           'kiwi', 'pie', 'cheat', 'kit', 'grey', 'warm', 'dumb', 'border', 'auto', 'god', 'fear', 'die', 'author', 'mix',
           'experience', 'grow', 'aw', 'doe', 'drive', 'stuck', 'number', 'oil', 'fan', 'pay', 'amazon', 'problem', 'jesus',
           'laugh', "i'd", 'ghost', 'cause', 'target', 'pay', 'mingo', 'tire', 'strange', 'bar', 'canadian', 'beef', 
           'wine', 'asp', 'poop', 'dollar', 'record', 'coca', 'exit', 'ceo', 'donald', 'blog', 'store', 'myth', 'act', 'ow',
           'horny', 'alliana', 'gun', 'cina', 'firm', 'elf', 'walmart', 'remind', 'mr', 'underground', 'hurdle', 'payroll',
           'commas',' audi', 'salon', 'milk']

for i in range(len(animals)):
    transcript=extract_transcript(animals[i]).lower().replace('.','').replace('?','').replace(',','').split()
    count=0
    for j in range(len(transcript)):
        # cehck if the word is a noun
        if nltk.pos_tag(word_tokenize(transcript[j]))[0][1] == 'NN' and transcript[j] not in stopwords: 
            count=count+1

    animal_metrics.append(count)
print('ANIMALS')
mean_, std_ = mean_std(animal_metrics)
print(mean_)
print('+/- %s'%(str(std_)))

######################################################################
##              TEST SURVEY A FEATURIZATION/CLEANING                ##
######################################################################

def get_wavfile(transcript):
    wavfile=transcript.split(' ')[0].replace('(','')+'.wav'
    return wavfile 

def combine_wavfiles(wavfiles, sessionid, type_):
    curdir=os.getcwd()
    cmd='sox'
    for k in range(len(wavfiles)):
        cmd=cmd+' '+wavfiles[k]
    cmd=cmd+' %s_%s.wav'%(sessionid, type_)
    os.chdir(sessionid)
    os.system(cmd)
    os.chdir(curdir)

os.chdir(basedir)
os.chdir('data')
os.chdir('test')

## CLEAN the CSV spreadsheet!
os.system('python3 clean.py')
data=pd.read_csv('clean.csv')
sessions = data['sessionId']

# we go to the right spot and need to map elictation types to prompts
curdir=os.getcwd()
sys.path.append(curdir)
from prompts import * 

# this unlocks bnt_tasks | nonword_tasks | all_tasks

## Make Functions ## 
# --> stich together all the BNT-naming prompts (1 master session) --> sessionid_bnt.wav
for i in range(len(data)):
    session=str(sessions[i])
    wavfiles=list()
    for j in range(len(bnt_tasks)):
        bnt_task=data[bnt_tasks[j]][i]
        wavfile=get_wavfile(bnt_task)
        wavfiles.append(wavfile)
    combine_wavfiles(wavfiles, session,'bnt')

# --> stitch together all the Nonword-naming prompts (1 master session) --> sessionid_nonword.wav 
for i in range(len(data)):
    session=str(sessions[i])
    wavfiles=list()
    for j in range(len(nonword_tasks)):
        nonword_task=data[nonword_tasks[j]][i]
        wavfile=get_wavfile(nonword_task)
        wavfiles.append(wavfile)
    combine_wavfiles(wavfiles, session,'nonword')

## clean (mono 16000 Hz) featurize sesions
for i in range(len(data)):
    session=str(sessions[i])
    os.chdir(curdir)
    os.chdir('allie')
    # if clean_audio == True:
        # os.system('python3 allie.py --command clean --sampletype audio --dir %s'%(curdir+'/'+session))
    os.system('python3 allie.py --command features --sampletype audio --dir %s'%(curdir+'/'+session))

## visualize relative to standards
os.chdir(basedir)
os.chdir('data')
os.chdir('options')

tasks=json.load(open('task_options.json'))['AllTasks']

os.chdir(basedir)
os.chdir('data')
os.chdir('test')
os.chdir(sessions[0])

means_3=list()
stds_3=list()

for i in range(len(tasks)):
    wavfile=get_wavfile(data[all_tasks[i]][0]).replace('.wav','_cleaned.wav')
    jsonfile=wavfile[0:-4]+'.json'

    # convert to the format of this repository (Allie --> Voiceome)
    if feature_embedding == 'OpensmileFeatures':
        feature_data=json.load(open(jsonfile))['features']['audio']['opensmile_features']
    elif feature_embedding == 'ProsodyFeatures':
        feature_data=json.load(open(jsonfile))['features']['audio']['prosody_features']
    elif feature_embedding == 'PauseFeatures':
        feature_data=json.load(open(jsonfile))['features']['audio']['pause_features']
    elif feature_embedding == 'AudiotextFeatures':
        feature_data=json.load(open(jsonfile))['features']['audio']['audiotext_features']

    dict_=dict(zip(feature_data['labels'],feature_data['features']))
    value_=dict_[featuretype]
    means_3.append(value_)
    stds_3.append(0)

# visualize recent featurizations against the data
visualize_bar_cohorts(featuretype, feature_embedding, names, means_3, stds_3, 'Jim (ThirtiesMale)', means_2, stds_2, 'TwentiesFemale', basedir, False)
visualize_bar_cohorts(featuretype, feature_embedding, names, means_3, stds_3, 'Jim (ThirtiesMale)', means, stds, 'TwentiesMale', basedir, False)

######################################################################
##                      BNT AND NONWORD METRICS                     ##
######################################################################

os.chdir(basedir)
os.chdir('data')
os.chdir('test')
os.chdir(sessions[0])

# sample BNT value 
listdir=os.listdir()
for i in range(len(listdir)):
    if listdir[i].find('bnt') >= 0 and listdir[i].endswith('.json'):
        # used deepspeech transcript in the paper
        transcript=json.load(open(listdir[i]))['transcripts']['audio']['deepspeech_dict']
        bnt_metric=bnt_features(transcript)
        print('Confrontational Naming Task:')
        print(bnt_metric)
        break
# sample nonword value
listdir=os.listdir()
for i in range(len(listdir)):
    if listdir[i].find('nonword') >= 0 and listdir[i].endswith('.json'):   
        # used deepspeech no_dict in the paper
        transcript=json.load(open(listdir[i]))['transcripts']['audio']['deepspeech_nodict']
        nonword_metric=nonword_features(transcript)
        print('Nonword Task:')
        print(nonword_metric)
        break
