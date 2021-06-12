import os, shutil, time
import pandas as pd 

def get_audiofile(transcript):
	return str(transcript).split(' ')[0].replace('(','')+'_cleaned.wav'

g=pd.read_csv('new2.csv')

# picture description
sessions=list(g['sessionId'])

print(sessions)

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

try:
	os.mkdir(folder)
except:
	shutil.rmtree(folder)
	os.mkdir(folder)

os.chdir(folder)

for i in range(len(audiofiles)):
	task=list(g[audiofiles[i]])

	folder2=str(i)+'_'+audiofiles[i].replace(' ','_')[0:20]
	try:
		os.mkdir(folder2)
	except:
		shutil.rmtree(folder2)
		os.mkdir(folder2)

	# print(len(task))
	# time.sleep(50)
	for j in range(len(task)):
		try:
			print(task[j])
			file=get_audiofile(task[j])
			print(file)
			shutil.copy(curdir+'/sessions/'+str(sessions[j])+'/'+file, curdir+'/audio_bytask/'+folder2+'/'+file)
			try:
				shutil.copy(curdir+'/sessions/'+str(sessions[j])+'/'+file[0:-4]+'.json', curdir+'/audio_bytask/'+folder2+'/'+file[0:-4]+'.json')
			except:
				pass
		except:
			pass

print(audiofiles)