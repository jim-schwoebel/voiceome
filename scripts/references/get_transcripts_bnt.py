import os, json
import numpy as np

# now sort words by counts 
def extract_bnt(transcript):
	# https://github.com/NeuroLexDiagnostics/voiceome_bnt_models
	transcript=transcript.lower().split()
	print(transcript)

	counts=0
	if 'mushroom' in transcript:
		counts=counts+1
	if 'bicycle' in transcript:
		counts=counts+1
	if 'camel' in transcript:
		counts=counts+1
	if 'camera' in transcript:
		counts=counts+1
	if 'chicken' in transcript:
		counts=counts+1
	if 'dinosaur' in transcript or 'brontosaurus' in transcript or 'brontosaur' in transcript:
		counts=counts+1
	if 'balloon' in transcript or 'bullion' in transcript:
		counts=counts+1
	if 'glasses' in transcript or 'spectacles' in transcript or 'bifocals' in transcript:
		counts=counts+1
	if 'gorilla' in transcript:
		counts=counts+1
	if 'volcano' in transcript:
		counts=counts+1
	if 'asparagus' in transcript:
		counts=counts+1
	if 'pizza' in transcript or 'piazza' in transcript:
		counts=counts+1
	if 'railroad' in transcript or 'track' in transcript or 'tracks' in transcript:
		counts=counts+1
	if 'scissors' in transcript:
		counts=counts+1
	if 'shovel' in transcript:
		counts=counts+1
	if 'flamingo' in transcript:
		counts=counts+1
	if 'suit' in transcript or 'suitcase' in transcript or 'case' in transcript:
		counts=counts+1
	if 'telephone' in transcript or 'phone' in transcript:
		counts=counts+1
	if 'later' in transcript or 'ladder' in transcript:
		counts=counts+1
	if 'toothbrush' in transcript or 'tooth' in transcript or 'brush' in transcript:
		counts=counts+1
	if 'coconut' in transcript or 'cocoanut' in transcript:
		counts=counts+1
	if 'while' in transcript or 'wallet' in transcript:
		counts=counts+1
	if 'pineapple' in transcript or 'pine' in transcript:
		if 'pine' in transcript and 'apple' in transcript:
			counts=counts+1
		else:
			counts=counts+1
	if 'cactus' in transcript:
		counts=counts+1

	return counts 

def extract_nonword(transcript):
	transcript=transcript.lower().split()
	print(transcript)
	counts=0
	if 'plive' in transcript or 'pli' in transcript or 'live' in transcript or 'pliv' in transcript or 'life' in transcript or 'plife' in transcript:
		counts=counts+1
	if 'for' in transcript or 'flove' in transcript:
		counts=counts+1
	if 'zowl' in transcript or 'thou' in transcript or 'zone' in transcript or 'zoul' in transcript:
		counts=counts+1
	if 'zox' in transcript or 'zoolix' in transcript or 'filks' in transcript:
		counts=counts+1
	if 'they' in transcript or 'tave' in transcript or 'wall' in transcript or 'vave' in transcript:
		counts=counts+1
	if 'kwaj' in transcript or 'quash' in transcript or 'quatda' in transcript:
		counts=counts+1
	if 'jom' in transcript or 'joam' in transcript or 'dram' in transcript or 'jome' in transcript:
		counts=counts+1
	if 'boys' in transcript or 'boyl' in transcript or 'bwils' in transcript or 'bwiz' in transcript:
		counts=counts+1
	if 'broe' in transcript or 'brow' in transcript:
		counts=counts+1
	if 'nay' in transcript or 'nayb' in transcript or 'nab' in transcript or 'a' in transcript:
		counts=counts+1

	return counts 

# os.chdir('nonwords')
os.chdir('bnt_images')
listdir=os.listdir()

transcripts=''
counts_list=list()
transcripts_list=list()

for i in range(len(listdir)):
	if listdir[i].endswith('.wav') and listdir[i][0:-4]+'.json' in listdir:
		try:
			g=json.load(open(listdir[i][0:-4]+'.json'))
			# transcript=g['transcripts']['audio']['deepspeech_nodict']
			# counts=extract_nonword(transcript)
			
			transcript=g['transcripts']['audio']['deepspeech_dict']
			counts=extract_bnt(transcript)
			# print(counts)
			if counts > 10:
				counts_list.append(counts)
				transcripts=transcripts+' '+transcript
				transcripts_list.append(transcript)
		except:
			print('error')

unique_words=list(set(transcripts.split()))

unique_counts=dict()

for i in range(len(unique_words)):
	unique_counts[unique_words[i]]=transcripts.count(unique_words[i])

g={k: v for k, v in sorted(unique_counts.items(), key=lambda item: item[1])}

print(np.mean(np.array(counts_list)))
print(np.std(np.array(counts_list)))

# # count the most frequent (keep only unique words in top 80% of distribution)
# plive=list()
# keywords=dict()
# for i in range(len(transcripts_list)):
# 	try:
# 		word=transcripts_list[i].split()[1]
# 		print(word)
# 		if word not in plive:
# 			keywords[word]=transcripts.count(word)
# 			plive.append(word)
# 	except:
# 		pass


# print(keywords)
# print({k: v for k, v in sorted(keywords.items(), key=lambda item: item[1])})