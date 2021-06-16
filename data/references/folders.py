import json
import os
from tqdm import tqdm

def get_folders():
	listdir=os.listdir()	
	folders=list()
	for i in range(len(listdir)):
		if listdir[i].find('.') < 0:
			folders.append(listdir[i])
	return folders 

def change_json(file):
	data=json.load(open(file))
	feature_options=['AudiotextFeatures', 'OpensmileFeatures', 'ProsodyFeatures', 'PauseFeatures']
	for j in range(len(feature_options)):
		features=list(data[feature_options[j]])
		for k in range(len(features)):
			data[feature_options[j]][features[k]]['FourtiesMale']=data[feature_options[j]][features[k]]['FourtiesMale]']
			del data[feature_options[j]][features[k]]['FourtiesMale]']

	jsonfile=open(file,'w')
	json.dump(data,jsonfile)
	jsonfile.close()

def get_change_json():
	jsonfiles=list()
	listdir=os.listdir()
	for i in tqdm(range(len(listdir))):
		if listdir[i].endswith('.json'):
			change_json(listdir[i])

folders=get_folders()
cur_dir=os.getcwd()
for i in range(len(folders)):
	os.chdir(cur_dir)
	os.chdir(folders[i])
	get_change_json()