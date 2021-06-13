'''
               AAA               lllllll lllllll   iiii                      
              A:::A              l:::::l l:::::l  i::::i                     
             A:::::A             l:::::l l:::::l   iiii                      
            A:::::::A            l:::::l l:::::l                             
           A:::::::::A            l::::l  l::::l iiiiiii     eeeeeeeeeeee    
          A:::::A:::::A           l::::l  l::::l i:::::i   ee::::::::::::ee  
         A:::::A A:::::A          l::::l  l::::l  i::::i  e::::::eeeee:::::ee
        A:::::A   A:::::A         l::::l  l::::l  i::::i e::::::e     e:::::e
       A:::::A     A:::::A        l::::l  l::::l  i::::i e:::::::eeeee::::::e
      A:::::AAAAAAAAA:::::A       l::::l  l::::l  i::::i e:::::::::::::::::e 
     A:::::::::::::::::::::A      l::::l  l::::l  i::::i e::::::eeeeeeeeeee  
    A:::::AAAAAAAAAAAAA:::::A     l::::l  l::::l  i::::i e:::::::e           
   A:::::A             A:::::A   l::::::ll::::::li::::::ie::::::::e          
  A:::::A               A:::::A  l::::::ll::::::li::::::i e::::::::eeeeeeee  
 A:::::A                 A:::::A l::::::ll::::::li::::::i  ee:::::::::::::e  
AAAAAAA                   AAAAAAAlllllllllllllllliiiiiiii    eeeeeeeeeeeeee  


|  ___|       | |                        / _ \ | ___ \_   _|  _ 
| |_ ___  __ _| |_ _   _ _ __ ___  ___  / /_\ \| |_/ / | |   (_)
|  _/ _ \/ _` | __| | | | '__/ _ \/ __| |  _  ||  __/  | |      
| ||  __/ (_| | |_| |_| | | |  __/\__ \ | | | || |    _| |_   _ 
\_| \___|\__,_|\__|\__,_|_|  \___||___/ \_| |_/\_|    \___/  (_)
                                                                
                                                                
  ___            _ _       
 / _ \          | (_)      
/ /_\ \_   _  __| |_  ___  
|  _  | | | |/ _` | |/ _ \ 
| | | | |_| | (_| | | (_) |
\_| |_/\__,_|\__,_|_|\___/ 
                           

This will featurize folders of audio files if the default_audio_features = ['audiotext_features']

Featurizes data with text feautures extracted from the transcript.
These text features include nltk_features, textacy_features, spacy_features, and text_features.
'''

import librosa_features as lf 
import helpers.transcribe as ts
import numpy as np
import random, math, os, sys, json, time

def prev_dir(directory):
    g=directory.split('/')
    dir_=''
    for i in range(len(g)):
        if i != len(g)-1:
            if i==0:
                dir_=dir_+g[i]
            else:
                dir_=dir_+'/'+g[i]
    # print(dir_)
    return dir_

directory=os.getcwd()
prevdir=prev_dir(directory)
sys.path.append(prevdir+'/text_features')
import text2_features as tf
import nltk_features as nf 
import textacy_features as tfe
import spacy_features as spf
import text_features as tfea

import spacy
nlp=spacy.load('en_core_web_sm')

def audiotext_featurize(wavfile, transcript):

    features2, labels2 = tf.text2_featurize(transcript)
  
    # get features 
    nltk_features, nltk_labels=nf.nltk_featurize(transcript)

    textacy_features, textacy_labels=tfe.textacy_featurize(transcript, nlp)

    spacy_features, spacy_labels=spf.spacy_featurize(transcript, nlp)
    
    text_features,text_labels=tfea.text_featurize(transcript)

    # concatenate feature arrays 
    features=np.append(np.array(nltk_features),np.array(textacy_features))
    features=np.append(features,np.array(spacy_features))
    features=np.append(features, np.array(text_features))
    
    # concatenate labels
    labels=nltk_labels+textacy_labels+spacy_labels+text_labels

    features=list(np.append(features, np.array(features2)))
    labels=labels+labels2

    return features, labels 