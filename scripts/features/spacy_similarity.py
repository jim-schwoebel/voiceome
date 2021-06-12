import spacy, os, json
from tqdm import tqdm
import numpy as np

nlp = spacy.load('en_core_web_sm')

def calculate_similarity(text1, text2, nlp):
	doc1=nlp(text1)
	doc2=nlp(text2)
	similarity=doc1.similarity(doc2)
	return similarity 

os.chdir('audio')
listdir=os.listdir()

mes=list()
azures=list()
letters=list()
deepspeechs=list()

for i in tqdm(range(len(listdir))):
	if listdir[i].endswith('.json'):
		transcripts=json.load(open(listdir[i]))['transcripts']['audio']

		# testing transcription schemes
		me=transcripts['transcribeme'].lower()
		azure=transcripts['azure'].lower()
		letter=transcripts['wav2vec'].lower()
		deepspeech=transcripts['deepspeech_dict'].lower()

		# reference accuracy
		mes.append(1.0)
		azures.append(calculate_similarity(azure, me, nlp))
		letters.append(calculate_similarity(letter, me, nlp))
		deepspeechs.append(calculate_similarity(deepspeech, me, nlp))


# calculate averages and stds	
print('azure')	
print(np.mean(azures))
print(np.std(azures))
print('wav2vec')
print(np.mean(letters))
print(np.std(letters))
print('deepspeech')
print(np.mean(deepspeechs))
print(np.std(deepspeechs))

print('lengths')
print(len(azures))
print(len(letters))
print(len(deepspeechs))
