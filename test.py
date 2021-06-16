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

A simple unit test script for the Voiceome repository.

Thank you for your interest in our work!

================================================ 
                LICENSE TERMS                      
================================================ 

Copyright 2021 Sonde Health, Inc. 
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
import sys, os, json, time, shutil, argparse, random, math, unittest, shutil
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

# get current directory 
curdir=os.getcwd()

######################################################################
##                            UNIT TESTS                           ##
######################################################################

##### ##### ##### ##### ##### ##### ##### ##### ##### #####
class test_cleaning(unittest.TestCase):
    '''
    CLEANING API TESTS
    Tests file cleaning capabilities by removing duplicates, etc.
    across all file types.
    '''
    ##### ##### ##### ##### ##### ##### ##### ##### ##### #####
    
    def test_cleaning(self, curdir=curdir):
        os.chdir(curdir)
        os.chdir('tests')
        # get a fresh dataset in case it was manipulated 
        if 'voiceome_test_data' in os.listdir():
            shutil.rmtree('voiceome_test_data')
            os.system('git clone https://github.com/jim-schwoebel/voiceome_test_data')
        else:
            os.system('git clone https://github.com/jim-schwoebel/voiceome_test_data')
        os.chdir('voiceome_test_data')
        os.chdir('a871b730-cc8a-11eb-a78c-b9f05e289d42')
        clean_dir=os.getcwd()
        os.chdir(curdir)
        os.system('python3 cli.py --command clean --dir %s'%(clean_dir))
        os.chdir(clean_dir)
        listdir=os.listdir()
        cleanfiles=list()
        for i in range(len(listdir)):
            if listdir[i].find('cleaned.wav'):
                cleanfiles.append(listdir[i])

        if len(cleanfiles) == 50:
            b=True
        else:
            b=False
        
        msg='Featurizations failed, please check dependencies and try again.'
        self.assertEqual(True, b, msg) 

##### ##### ##### ##### ##### ##### ##### ##### ##### #####
class test_featurization(unittest.TestCase):
    '''
    FEATURIZATION API TESTS
    Tests featurization capabilities across all training scripts.
    '''
    #### ##### ##### ##### ##### ##### ##### ##### ##### #####

    def test_audio_features(self, curdir=curdir):
        os.chdir(curdir)
        os.chdir('tests')
        # get a fresh dataset in case it was manipulated 
        if 'voiceome_test_data' in os.listdir():
            shutil.rmtree('voiceome_test_data')
            os.system('git clone https://github.com/jim-schwoebel/voiceome_test_data')
        else:
            os.system('git clone https://github.com/jim-schwoebel/voiceome_test_data')
        os.chdir('voiceome_test_data')
        os.chdir('a871b730-cc8a-11eb-a78c-b9f05e289d42')
        features_dir=os.getcwd()
        os.chdir(curdir)
        os.system('python3 cli.py --command features --dir %s'%(features_dir))
        os.chdir(features_dir)
        listdir=os.listdir()
        jsonfiles=list()
        for i in range(len(listdir)):
            if listdir[i].endswith('.json'):
                jsonfiles.append(listdir[i])

        if len(jsonfiles) == 50:
            b=True
        else:
            b=False
        
        msg='Featurizations failed, please check dependencies and try again.'
        self.assertEqual(True, b, msg) 

##### ##### ##### ##### ##### ##### ##### ##### ##### #####
class test_quality(unittest.TestCase):
    '''
    TRANSCRIPTION API TESTS
    tests the ability to transcribe across many
    data types
    '''
    def test_quality_featurization(self, curdir=curdir):
        os.chdir(curdir)
        os.chdir('tests')
        if 'voiceome_test_data' not in os.listdir():
            os.system('git clone https://github.com/jim-schwoebel/voiceome_test_data')
        os.chdir('voiceome_test_data')
        os.chdir('a871b730-cc8a-11eb-a78c-b9f05e289d42')
        new_dir=os.getcwd()
        os.chdir(curdir)
        os.system('python3 cli.py --command quality --file nlx-4d2f5480-cc8b-11eb-aefd-7de9011dbebd.wav --dir %s > test.txt'%(new_dir))
        newfile=open('test.txt').read().split('--------------------------------------------------------------')
        output=newfile[-2].replace('\n','')
        os.remove('test.txt')

        # now go through and see if all the strings are there
        b=True

        if output.find('brownfox_feature') < 0:
            b=False
        if output.find('animal_feature') < 0:
            b=False
        if output.find('caterpillar_feature') < 0:
            b=False
        if output.find('mandog_feature') < 0:
            b=False
        if output.find('tourbus_feature') < 0:
            b=False
        if output.find('bnt_feature') < 0:
            b=False
        if output.find('nonword_feature') < 0:
            b=False 

        msg='failed the process of extracting quality metrics; please re-install dependencies with requirements.txt and try again.'

        self.assertEqual(True, b, msg) 

# class test_references(unittest.TestCase):
#     # git clone https://github.com/jim-schwoebel/voiceome_test_data
#     # cd .. 
#     # os.system('python3 clean.py')

##### ##### ##### ##### ##### ##### ##### ##### ##### #####
class test_settings(unittest.TestCase):
    '''
    SETTINGS TEST API 

    Make sure all settings are proper values.
    '''
    settings=json.load(open('settings.json'))

    def test_transcription_engine(self, curdir=curdir, settings=settings):
        os.chdir(curdir)
        os.chdir('data')
        os.chdir('options')
        transcript_option=settings['TranscriptEngine']
        transcript_options=json.load(open('transcriptengine_options.json'))['TranscriptEngineOptions']
        if transcript_option in transcript_options:
            b=True
        else:
            b=False
        msg='%s not in transcription options: \n%s'%(transcript_option, transcript_options)
        self.assertEqual(True, b, msg) 

    def test_feature_embedding(self, curdir=curdir):
        os.chdir(curdir)
        os.chdir('data')
        os.chdir('options')
        data=json.load(open('feature_options.json'))
        feature_embedding=settings['FeatureEmbedding']
        feature_embeddings=list(json.load(open('feature_options.json')))
        if feature_embedding in feature_embeddings:
            b=True
        else:
            b=False
        msg='%s not in possible list of feature embeddings: \n%s'%(feature_embedding, str(feature_embeddings))
        self.assertEqual(True, b, msg) 

    def test_featuretype(self, curdir=curdir):
        os.chdir(curdir)
        os.chdir('data')
        os.chdir('options')
        feature_embedding=settings['FeatureEmbedding']
        featuretype=settings['FeatureType']
        featuretypes=json.load(open('feature_options.json'))[feature_embedding]
        if featuretype in featuretypes:
            b=True
        else:
            b=False
        msg='%s not in list of possible feature types (in the %s embedding).'%(featuretype, feature_embedding)
        self.assertEqual(True, b, msg) 

    def test_task(self, curdir=curdir):
        os.chdir(curdir)
        os.chdir('data')
        os.chdir('options')
        task_option=settings['Task']
        task_options=json.load(open('task_options.json'))['AllTasks']
        if task_option in task_options:
            b=True
        else:
            b=False
        msg='%s not in task options: \n%s'%(task_option, task_options)
        self.assertEqual(True, b, msg) 

    def test_cleanaudio(self, curdir=curdir):
        os.chdir(curdir)
        os.chdir('data')
        os.chdir('options')
        option=settings['CleanAudio']
        options=[True, False]

        if option in options:
            b=True
        else:
            b=False
        msg='%s not in options: \n%s'%(option, options)
        self.assertEqual(True, b, msg) 

    def test_agegender(self, curdir=curdir):
        os.chdir(curdir)
        os.chdir('data')
        os.chdir('options')
        option=settings['DefaultAgeGender']
        options=json.load(open('agegender_options.json'))['AgeGenderOptions']
        if option in options:
            b=True
        else:
            b=False
        msg='%s not in options: \n%s'%(option, options)
        self.assertEqual(True, b, msg) 

# ##### ##### ##### ##### ##### ##### ##### ##### ##### #####
# class test_visualization(unittest.TestCase):
#     '''
#     VISUALIZATION API TESTS
#     '''
#     # self.assertEqual(True, b, msg) 


if __name__ == '__main__':
    unittest.main()
