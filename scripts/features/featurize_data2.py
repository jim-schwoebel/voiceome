import os, random 

def get_folders():
	listdir=os.listdir()
	folders=list()
	for i in range(len(listdir)):
		if listdir[i].find('.') == -1:
			folders.append(listdir[i])
	return folders 

def clean_audio(allie_dir, clean_dir):
	os.chdir(allie_dir)
	os.system('python3 allie.py --command clean --sampletype audio --dir %s'%(clean_dir))

def featurize_audio(allie_dir, feature_dir):
	os.chdir(allie_dir)
	os.system('python3 allie.py --command features --sampletype audio --dir %s'%(feature_dir))

def pursue_featurize():
	listdir=os.listdir()
	wavfiles=list()
	for j in range(len(listdir)):
		if listdir[j].endswith('.wav'):
			wavfiles.append(listdir[j])

	counts=list()
	for j in range(len(wavfiles)):
		if wavfiles[j][0:-4]+'.json' in listdir:
			counts.append(True)
		else:
			counts.append(False)

	if counts.count(False) > 0:
		return False 
	else:
		return True 

curdir=os.getcwd()
allie_dir='/Users/jimschwoebel/desktop/allie-sonde'

# Pear-data-depresssion
os.chdir(curdir)
os.chdir('audio_bytask')
folders=get_folders()
random.shuffle(folders)
curdir2=os.getcwd()
counts=list()

for i in range(len(folders)):
	os.chdir(curdir2)
	os.chdir(folders[i])
	curdir3=os.getcwd()
	featurize_audio(allie_dir, curdir3)
