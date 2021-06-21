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

bnt_tasks=['Name this image  ![](https://www.voiceome.org/bnt_images/01_Mushroom.png)', 
			'Name this image  ![](https://www.voiceome.org/bnt_images/02_Bicycle.jpg)', 
			'Name this image  ![](https://www.voiceome.org/bnt_images/03_Camel.png)', 
			'Name this image  ![](https://www.voiceome.org/bnt_images/04_Camera.png)', 
			'Name this image  ![](https://www.voiceome.org/bnt_images/05_Chicken.png)', 
			'Name this image  ![](https://www.voiceome.org/bnt_images/06_Dinosaur.jpg)', 
			'Name this image  ![](https://www.voiceome.org/bnt_images/07_Balloon.png)', 
			'Name this image  ![](https://www.voiceome.org/bnt_images/08_Glasses.png)', 
			'Name this image  ![](https://www.voiceome.org/bnt_images/09_Gorilla.png)', 
			'Name this image  ![](https://www.voiceome.org/bnt_images/10_Volcano.png)', 
			'Name this image  ![](https://www.voiceome.org/bnt_images/11_Asparagus.png)', 
			'Name this image  ![](https://www.voiceome.org/bnt_images/12_Pizza_.png)', 
			'Name this image  ![](https://www.voiceome.org/bnt_images/13_Railroad.png)', 
			'Name this image  ![](https://www.voiceome.org/bnt_images/14_Scissors_.png)', 
			'Name this image  ![](https://www.voiceome.org/bnt_images/15_Shovel.png)', 
			'Name this image  ![](https://www.voiceome.org/bnt_images/16_Flamingo.png)', 
			'Name this image  ![](https://www.voiceome.org/bnt_images/17_Suitcase.png)', 
			'Name this image  ![](https://www.voiceome.org/bnt_images/18_Telephone.png)', 
			'Name this image  ![](https://www.voiceome.org/bnt_images/19_Ladder_.jpg)', 
			'Name this image  ![](https://www.voiceome.org/bnt_images/20_Toothbrush_.png)', 
			'Name this image  ![](https://www.voiceome.org/bnt_images/21_Hammer_.png)', 
			'Name this image  ![](https://www.voiceome.org/bnt_images/22_Coconut_3.png)', 
			'Name this image  ![](https://www.voiceome.org/bnt_images/23_Wallet_3.png)', 
			'Name this image  ![](https://www.voiceome.org/bnt_images/24_Pineapple.png)', 
			'Name this image  ![](https://www.voiceome.org/bnt_images/25_Cactus_.png)'] 

for i in range(len(bnt_tasks)):
	# new label
	bnt_task=bnt_tasks[i]
	label=bnt_task.split('/')[-1].replace('.png','').replace('_','').replace(')','').replace('.jpg','')
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