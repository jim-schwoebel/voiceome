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
                                                                             
|  \/  |         | |    | |  / _ \ | ___ \_   _|
| .  . | ___   __| | ___| | / /_\ \| |_/ / | |  
| |\/| |/ _ \ / _` |/ _ \ | |  _  ||  __/  | |  
| |  | | (_) | (_| |  __/ | | | | || |    _| |_ 
\_|  |_/\___/ \__,_|\___|_| \_| |_/\_|    \___/ 
						   
Makes a table in Microsoft Word for all the audio features present in a file in a particular folder.
This is useful for peer-reviewed publications (for supplementary tables).

Usage: python3 get_stats.py [folder]

Example: python3 get_stats.py females

Following this tutorial with modifications: https://towardsdatascience.com/how-to-generate-ms-word-tables-with-python-6ca584df350e
'''

from docx import Document
from docx.shared import Cm, Pt
import numpy as np
import os, json, time, sys
import pandas as pd 
from tqdm import tqdm
import random

def describe_text(jsonfile):

	# get dictionary 
	g=json.load(open(jsonfile))
	features=g['features']['audio']
	featuretypes=list(features)

	print(featuretypes)
	features_=list()
	labels_=list()
	for j in range(len(featuretypes)):
		if featuretypes[j] in ['audiotext_features']:
			pass
		else:
			rename_labels=list()
			temp_labels=features[featuretypes[j]]['labels']
			for k in range(len(temp_labels)):
				if featuretypes[j] == 'pause2_features':
					rename_labels.append(temp_labels[k]+ '\n (pause_features)')
				else:
					rename_labels.append(temp_labels[k]+'\n (%s)'%(featuretypes[j]))
			try:
				features_=features_+features[featuretypes[j]]['features']
			except:
				features_=features_+[0]
			labels_=labels_+rename_labels

	description=dict(zip(labels_,features_))
	
	return description

def get_average(string_):
	return float(string_.split('\n')[0])
def get_std(string_):
	return float(string_.split(' ')[-1].replace(')',''))

def get_descriptive_statistics(new, lab):

	for j in range(len(lab)):
		print(lab[j])
		print(new[lab[j]])
		if lab[j] == ['UtteranceTimes\n (pause_features)','PauseTimes\n (pause_features)']:
			new.pop(lab[j])
		else:
			try:
				mean_=str(round(np.nanmean(np.array(new[lab[j]])), 3))
				std_=str(round(np.nanstd(np.array(new[lab[j]])), 3))
				new[lab[j]]=mean_+'\n(+/- '+std_+')'
			except:
				new.pop(lab[j])

	return new

def clean_gender(genders_, ):
	new=list()

	for i in range(len(genders_)):
		if genders_[i] in ['Male', 'Female']:
			new.append(genders_[i])
		else:
			pass

# go to the right folder
data=pd.read_csv('new2.csv')
cur_dir=os.getcwd()
directory=sys.argv[1]

# iterate through the data to find the sampleid 
age=list(data['common_voice_age'])
genders=list(data['With which gender do you most identify? '])

labels=list(data)
audiofiles=list()

for i in range(len(labels)):
	result=str(data[labels[i]][0])
	# print(result)
	if result.find('nlx-') > 0:
		audiofiles.append(labels[i])
	else:
		pass

# print(directory)
audiofiles=[audiofiles[int(directory.split('/')[-1].split('_')[0])]]
print(audiofiles)

# got all audio file columns now in audiofiles 
# audiofiles_=list()
# newdir=directory.split('/')[-1]
# ind_=newdir.find('_')

# for i in range(len(audiofiles)):
# 	if newdir[ind_+1:ind_+21].find(audiofiles[i][0:20].replace(' ','_')) >= 0:
# 		audiofiles=[audiofiles[i]]
# 		break

os.chdir(directory)
listdir=os.listdir()
jsonfiles=list()
for i in range(len(listdir)):
	if listdir[i].endswith('.json'):
		jsonfiles.append(listdir[i])

# got all the jsonfiles, now add to each feature 
print(jsonfiles)
b_=False 
counts=0
while b_==False:
	description=describe_text(random.choice(jsonfiles))
	counts=counts+1
	if len(list(description)) == 94:
		break
	elif counts > 300:
		break

labels=list(description)

dict_=dict()
dict_twenties_male=dict()
dict_twenties_female=dict()
dict_thirties_male=dict()
dict_thirties_female=dict()
dict_fourties_male=dict()
dict_fourties_female=dict()
dict_fifties_male=dict()
dict_fifties_female=dict()
dict_sixties_male=dict()
dict_sixties_female=dict()

for i in range(len(labels)):
	dict_[labels[i]]=[]
	dict_twenties_male[labels[i]]=[]
	dict_twenties_female[labels[i]]=[]
	dict_thirties_male[labels[i]]=[]
	dict_thirties_female[labels[i]]=[]
	dict_fourties_male[labels[i]]=[]
	dict_fourties_female[labels[i]]=[]
	dict_fifties_male[labels[i]]=[]
	dict_fifties_female[labels[i]]=[]
	dict_sixties_male[labels[i]]=[]
	dict_sixties_female[labels[i]]=[]

# now go through all the json files 
ages_list=list()
genders_list=list()
transcripts_list=list()

for i in tqdm(range(len(jsonfiles))):
	stats=describe_text(jsonfiles[i])
	# print(stats)

	for k in range(len(audiofiles)):
		data_=data[audiofiles[k]]
		for l in range(len(data_)):
			if str(data_[l]).find(jsonfiles[i].replace('_cleaned.json',''))>=0:
				ind_=l
				break 

	age_=age[ind_]
	gender_=genders[ind_]
	transcript_=json.load(open(jsonfiles[i]))['transcripts']['audio']['azure']
	# get list 
	
	for j in range(len(labels)):
		try:
			dict_[labels[j]]=dict_[labels[j]]+[stats[labels[j]]]

			# by gender
			if age_ in ['teens','twenties'] and gender_ in ['Male']:
				dict_twenties_male[labels[j]] = dict_twenties_male[labels[j]] + [stats[labels[j]]]
			elif age_ in ['teens','twenties'] and gender_ in ['Female']:
				dict_twenties_female[labels[j]] = dict_twenties_female[labels[j]] + [stats[labels[j]]]
			elif age_ in ['thirties'] and gender_ in ['Male']:
				dict_thirties_male[labels[j]] = dict_thirties_male[labels[j]] + [stats[labels[j]]]
			elif age_ in ['thirties'] and gender_ in ['Female']:
				dict_thirties_female[labels[j]] = dict_thirties_female[labels[j]] + [stats[labels[j]]]
			elif age_ in ['fourties'] and gender_ in ['Male']:
				dict_fourties_male[labels[j]] = dict_fourties_male[labels[j]] + [stats[labels[j]]]
			elif age_ in ['fourties'] and gender_ in ['Female']:
				dict_fourties_female[labels[j]] = dict_fourties_female[labels[j]] + [stats[labels[j]]]
			elif age_ in ['fifties'] and gender_ in ['Male']:
				dict_fifties_male[labels[j]] = dict_fifties_male[labels[j]] + [stats[labels[j]]]
			elif age_ in ['fifties'] and gender_ in ['Female']:
				dict_fifties_female[labels[j]] = dict_fifties_female[labels[j]] + [stats[labels[j]]]
			elif age_ in ['sixties', 'seventies', 'eighties', 'nineties'] and gender_ in ['Male']:
				dict_sixties_male[labels[j]] = dict_sixties_male[labels[j]] + [stats[labels[j]]]
			elif age_ in ['sixties', 'seventies', 'eighties', 'nineties'] and gender_ in ['Female']:
				dict_sixties_female[labels[j]] = dict_sixties_female[labels[j]] + [stats[labels[j]]]
		except:
			pass

n_total=str(len(dict_[labels[0]]))

# males 
n_twenties_male=str(len(dict_twenties_male[labels[0]]))
n_thirties_male=str(len(dict_thirties_male[labels[0]]))
n_fourties_male=str(len(dict_fourties_male[labels[0]]))
n_fifties_male=str(len(dict_fifties_male[labels[0]]))
n_sixties_male=str(len(dict_sixties_male[labels[0]]))
# females
n_twenties_female=str(len(dict_twenties_female[labels[0]]))
n_thirties_female=str(len(dict_thirties_female[labels[0]]))
n_fourties_female=str(len(dict_fourties_female[labels[0]]))
n_fifties_female=str(len(dict_fifties_female[labels[0]]))
n_sixties_female=str(len(dict_sixties_female[labels[0]]))

dict_desc=get_descriptive_statistics(dict_, labels)
#males
dict_twenties_male=get_descriptive_statistics(dict_twenties_male, labels)
dict_thirties_male=get_descriptive_statistics(dict_thirties_male, labels)
dict_fourties_male=get_descriptive_statistics(dict_fourties_male, labels)
dict_fifties_male=get_descriptive_statistics(dict_fifties_male, labels)
dict_sixties_male=get_descriptive_statistics(dict_sixties_male, labels)
#females
dict_twenties_female=get_descriptive_statistics(dict_twenties_female, labels)
dict_thirties_female=get_descriptive_statistics(dict_thirties_female, labels)
dict_fourties_female=get_descriptive_statistics(dict_fourties_female, labels)
dict_fifties_female=get_descriptive_statistics(dict_fifties_female, labels)
dict_sixties_female=get_descriptive_statistics(dict_sixties_female, labels)
labels=list(dict_desc)

# customizing the table
data = dict()

data['OpensmileFeatures']=dict()
data['ProsodyFeatures']=dict()
data['PauseFeatures']=dict()
data['AudioText']=dict()

for i in range(len(labels)):

	label=labels[i].split('\n')[0]

	if labels[i].find('(opensmile_features)') > 0:
		core='OpensmileFeatures'
	elif labels[i].find('(prosody_features)') > 0:
		core='ProsodyFeatures'
	elif labels[i].find('(pause_features)') > 0:
		core='PauseFeatures'
	elif labels[i].find('(audiotext_features)') > 0:
		core='AudiotextFeatures'

	data[core][label]=dict()

	data[core][label]['TwentiesMale'] = {'AverageValue': get_average(dict_twenties_male[labels[i]]), 
									   'StdValue': get_std((dict_twenties_male[labels[i]])),
									   'Description': 'Twenties Male (Ages 18-29)',
									   'SampleNumber': int(n_twenties_male)}

	data[core][label]['TwentiesFemale'] = {'AverageValue': get_average(dict_twenties_female[labels[i]]),
										 'StdValue': get_std(dict_twenties_female[labels[i]]),
										 'Description': 'Twenties Female (Ages 18-29)',
										 'SampleNumber': int(n_twenties_female)}

	data[core][label]['ThirtiesMale']={'AverageValue': get_average(dict_thirties_male[labels[i]]),
								     'StdValue': get_std(dict_thirties_male[labels[i]]),
									 'Description': 'Thirties Male (Ages 30-39)',
									 'SampleNumber': int(n_thirties_male)}

	data[core][label]['ThirtiesFemale'] = {'AverageValue': get_average(dict_thirties_female[labels[i]]),
								         'StdValue': get_std(dict_thirties_female[labels[i]]),
										 'Description': 'Thirties Female (Ages 30-39)',
										 'SampleNumber': int(n_thirties_female)}

	data[core][label]['FourtiesMale]'] = {'AverageValue': get_average(dict_fourties_male[labels[i]]),
								        'StdValue': get_std(dict_fourties_male[labels[i]]),
										'Description': 'Fourties Male (Ages 40-49)',
										'SampleNumber': int(n_fourties_male)}

	data[core][label]['FourtiesFemale']= {'AverageValue': get_average(dict_fourties_female[labels[i]]),
								        'StdValue': get_std(dict_fourties_female[labels[i]]),
										'Description': 'Fourties Female (Ages 40-49)',
										'SampleNumber': int(n_fourties_female)}

	data[core][label]['FiftiesMale'] = {'AverageValue': get_average(dict_fifties_male[labels[i]]),
								      'StdValue': get_std(dict_fifties_male[labels[i]]),
									  'Description': 'Fifties Male (Ages 50-59)',
									  'SampleNumber': int(n_fifties_male)}

	data[core][label]['FiftiesFemale'] = {'AverageValue': get_average(dict_fifties_female[labels[i]]),
								        'StdValue': get_std(dict_fifties_female[labels[i]]),
										'Description': 'Fifties Female (Ages 50-59)',
										'SampleNumber': int(n_fifties_female)}

	data[core][label]['SixtiesMale'] = {'AverageValue': get_average(dict_sixties_male[labels[i]]),
								      'StdValue': get_std(dict_sixties_male[labels[i]]),
									  'Description': 'Over Sixty Male (Ages >60)',
									  'SampleNumber': int(n_sixties_male)}

	data[core][label]['SixtiesFemale'] = {'AverageValue': get_average(dict_sixties_female[labels[i]]),
								        'StdValue': get_std(dict_sixties_female[labels[i]]),
										'Description': 'Over Sixty Female (Ages >60)',
										'SampleNumber': int(n_sixties_female)}

	data[core][label]['AllAgesGenders'] = {'AverageValue': get_average(dict_desc[labels[i]]),
								         'StdValue': get_std(dict_desc[labels[i]]),
										 'Description': 'All Ages and Genders (>18)',
										 'SampleNumber': int(n_total)}

# know that this is a feature vector
os.chdir(cur_dir)
jsonfile=open(directory+'.json','w')
json.dump(data,jsonfile)
jsonfile.close()

