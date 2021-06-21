import os, time
import pandas as pd 

def extract_transcript(transcript):
	try:
		transcript=transcript.split(') ')[1]
	except:
		transcript=''
	return transcript

data=pd.read_csv('new2.csv')
labels=list(data)

for i in range(len(labels)):
	print(labels[i])

bnt_tasks = ['Speak the nonsense word you see below:  <h1><center>plive</center></h1>', 
				'Speak the nonsense word you see below:  <h1><center>fwov</center></h1>', 
				'Speak the nonsense word you see below:  <h1><center>zowl</center></h1>', 
				'Speak the nonsense word you see below:  <h1><center>zulx</center></h1>', 
				'Speak the nonsense word you see below:  <h1><center>vave</center></h1>', 
				'Speak the nonsense word you see below:  <h1><center>kwaj</center></h1>', 
				'Speak the nonsense word you see below:  <h1><center>jome</center></h1>', 
				'Speak the nonsense word you see below:  <h1><center>bwiz</center></h1>', 
				'Speak the nonsense word you see below:  <h1><center>broe</center></h1>', 
				'Speak the nonsense word you see below:  <h1><center>nayb</center></h1>']

for i in range(len(bnt_tasks)):
	# new label
	bnt_task=bnt_tasks[i]
	label=bnt_task.split('<center>')[1].split('</center>')[0]
	new_data_remove=list()
	for j in range(len(labels)):
		if labels[j] not in ['With which gender do you most identify? ', bnt_task]:
			new_data_remove.append(labels[j])

	transcripts=list()
	new_data=data.drop(columns=new_data_remove, axis=1)
	col=new_data[bnt_task]
	for j in range(len(col)):
		transcript=extract_transcript(col[j])
		print(transcript)
		transcripts.append(transcript)
	new_data['azure']=transcripts
	new_data.to_csv(label+'.csv', index=False)