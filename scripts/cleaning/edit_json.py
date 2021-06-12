import os, shutil, time, json
import pandas as pd 

def get_audiofile(transcript):
	file=str(transcript).split(' ')[0].replace('(','')+'_cleaned.wav'
	transcript=str(transcript).split(') ')[1]
	return file, transcript

g=pd.read_csv('new2.csv')

# picture description
sessions=list(g['sessionId'])

# print(sessions)

labels=list(g)
audiofiles=list()

for i in range(len(labels)):
	result=str(g[labels[i]][0])
	# print(result)
	if result.find('nlx-') > 0:
		audiofiles.append(labels[i])
	else:
		pass

# now copy into individual folders
folder='audio_bytask'
curdir=os.getcwd()

os.chdir(folder)

for i in range(len(audiofiles)):
	os.chdir(curdir)
	os.chdir(folder)
	task=list(g[audiofiles[i]])
	folder2=str(i)+'_'+audiofiles[i].replace(' ','_')[0:20]
	os.chdir(folder2)
	listdir=os.listdir()

	# print(len(task))
	# time.sleep(50)
	for j in range(len(task)):
		try:
			file, transcript=get_audiofile(task[j])
			print(file)
			print(transcript)
			loadfile=json.load(open(file[0:-4]+'.json'))
			loadfile['transcripts']={"audio": {"azure": transcript}, "text": {}, "image": {}, "video": {}, "csv": {}}
			os.remove(file[0:-4]+'.json')
			jsonfile=open(file[0:-4]+'.json','w')
			json.dump(loadfile,jsonfile)
			jsonfile.close()
			# print(loadfile)
		except:
			pass
