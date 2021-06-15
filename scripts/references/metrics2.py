import pandas as pd 
import difflib
import numpy as np 
import nltk
from nltk import word_tokenize

g=pd.read_csv('new2.csv')
labels=list(g)

for i in range(len(labels)):
	if labels[i].lower().find('caterpillar') > 0:
		caterpillar=labels[i]

def extract_transcript(transcript):
	try:
		return transcript.split(') ')[1]
	except:
		return ''

def animal_features(transcript, animal_list):
	transcript=transcript.lower().split(' ')
	count=0
	for j in range(len(transcript)):
		if transcript in animal_list:
			count=count+1
	return count 

def letterf_features(transcript):
	transcript=transcript.lower().split(' ')
	count=0
	words=list()
	for j in range(len(transcript)):
		if transcript[j].startswith('f') and transcript[j] not in words:
			count=count+1
			words.append(transcript[j])
	return count

def passage_features(transcript, reference):
	# similarity (https://stackoverflow.com/questions/1471153/string-similarity-metrics-in-python)
	# similarity
	seq=difflib.SequenceMatcher(a=transcript.lower(), b=reference.lower())
	# longest matching string
	match = seq.find_longest_match(0, len(transcript), 0, len(reference))
	
	return 100*seq.ratio() #, match.size, match.a, match.b

def mean_std(list_):
	array_=np.array(list_)
	return np.mean(array_), np.std(array_)
	
animals=g['Category: ANIMALS. Name all the animals you can think of as quickly as possible before the time elapses below.']

words=list()
stopwords=['um', 'think','hum','oh',"let's",'blue','name','uhm','brown',"i'm",'category','ok','uh',
		   'time','ah', 'yeah', 'hey', 'love', 'lot', 'god', 'eh', 'funny', 'sure', 'honey', 'sugar',
		   'doc', 'email', 'al', 'il', 'rap', 'count', 'talk', 'check', 'ha', 'anything', 'jack', 'cheap',
		   'wow', 'world', 'devil', 'gosh', 'mama', 'please', 'kind', 'king', 'thing', 'sorry', 'see',
		   'awesome', 'uhm', 'yellow', 'tail', 'need', 'mu', 'search', 'wizard', 'kid', 'wanna', 'mind', 'girl',
		   'giant', 'fire', 'care', 'steak', 'weather', 'war', 'window', 'rock', 'ego', 'word', 'camera', 'square',
		   'kiwi', 'pie', 'cheat', 'kit', 'grey', 'warm', 'dumb', 'border', 'auto', 'god', 'fear', 'die', 'author', 'mix',
		   'experience', 'grow', 'aw', 'doe', 'drive', 'stuck', 'number', 'oil', 'fan', 'pay', 'amazon', 'problem', 'jesus',
		   'laugh', "i'd", 'ghost', 'cause', 'target', 'pay', 'mingo', 'tire', 'strange', 'bar', 'canadian', 'beef', 
		   'wine', 'asp', 'poop', 'dollar', 'record', 'coca', 'exit', 'ceo', 'donald', 'blog', 'store', 'myth', 'act', 'ow',
		   'horny', 'alliana', 'gun', 'cina', 'firm', 'elf', 'walmart', 'remind', 'mr', 'underground', 'hurdle', 'payroll',
		   'commas',' audi', 'salon', 'milk']

for i in range(len(animals)):
	transcript=extract_transcript(animals[i]).lower().replace('.','').replace('?','').replace(',','').split()
	for j in range(len(transcript)):
		# cehck if the word is a noun
		if nltk.pos_tag(word_tokenize(transcript[j]))[0][1] == 'NN' and transcript[j] not in stopwords: 
			words=words+[transcript[j]]

unique_words=list(set(words))
unique_counts=dict()

for i in range(len(unique_words)):
	unique_counts[unique_words[i]]=words.count(unique_words[i])

g={k: v for k, v in sorted(unique_counts.items(), key=lambda item: item[1])}
print(list(g))
