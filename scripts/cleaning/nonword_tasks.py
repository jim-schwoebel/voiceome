import os, shutil
import pandas as pd 
from tqdm import tqdm

# read csv document 
g=pd.read_csv('new2.csv')
labels=list(g)

curdir=os.getcwd()
try:
	os.mkdir('nonwords')
except:
	shutil.rmtree('nonwords')
	os.mkdir('nonwords')

bnt_tasks=list()
bnt_dict=dict()

for i in range(len(labels)):
	if labels[i].lower().find('nonsense word') >= 0:
		bnt_tasks.append(labels[i])
		bnt_dict[labels[i]]=list(g[labels[i]])
# ok I got all the images 
# now let's move them into the right spot 
print(bnt_tasks)

sessions=list(g['sessionId'])

def get_audiofilename(string_):
	# (nlx-0a83ad70-a10d-11ea-a9bd-05f6eec0ad7f 00:00:05.57) The Quick Brown Fox jumps over the lazy dog.
	return string_.replace('(','').split(' ')[0] + '.wav'

def combine_audiofiles(audiofiles):
	cmd='sox'
	for k in range(len(audiofiles)):
		os.system('sox %s -r 16000 -c 1 -b 16 %s_mono.wav'%(audiofiles[k], audiofiles[k][0:-4]))
		cmd=cmd+ ' %s'%(audiofiles[k][0:-4]+'_mono.wav')

	cmd=cmd+' merged.wav'
	os.system(cmd)

	for k in range(len(audiofiles)):
		os.remove(audiofiles[k])
		os.remove(audiofiles[k][0:-4]+'_mono.wav')

for i in tqdm(range(len(g))):
	session=sessions[i]

	# make session directory 
	os.chdir(curdir)
	os.chdir('nonwords')
	os.mkdir(session)
	os.chdir(session)
	bnt_session=os.getcwd()

	# get sessions
	os.chdir(curdir)
	os.chdir('sessions')
	os.chdir(session)

	audiofiles=list()

	try:
		for j in range(len(bnt_tasks)):
			# get the value 
			audiofile = get_audiofilename(bnt_dict[bnt_tasks[j]][i])
			audiofiles.append(audiofile)
		for j in range(len(audiofiles)):
			shutil.copy(os.getcwd()+'/'+audiofiles[j], curdir+'/nonwords/'+session+'/'+audiofiles[j])
		print(len(audiofiles))
		os.chdir(bnt_session)
		combine_audiofiles(audiofiles)

	except:
		print('error')
