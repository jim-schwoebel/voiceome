######################################################################
##                           IMPORTS                               ##
######################################################################
import sys, os, json, time, shutil, argparse, random, math
import difflib

directory=os.getcwd()

######################################################################
##                     QUALITY METRICS                              ##
######################################################################

def transcribe(transcript_type):
    if transcript_type == :
        # 
    elif transcript_type == :
        #
    elif transcript_type == :
        # 
        
def extract_transcript(transcript):
    try:
        return transcript.split(') ')[1]
    except:
        return ''

def animal_featurize(transcript):
    # clean transcript 
    transcript=transcript.lower().replace('.','').replace('?','').replace(',','').split()
    # stopwords calculated from manual review of all Voiceome samples
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
    count=0
    for j in range(len(transcript)):
        if nltk.pos_tag(word_tokenize(transcript[j])) == 'NN' and if transcript[j] not in stopwords:
            count=count+1

    return count 

def letterf_featurize(transcript):
    transcript=transcript.lower().split(' ')
    count=0
    words=list()
    for j in range(len(transcript)):
        if transcript[j].startswith('f') and transcript[j] not in words:
            count=count+1
            words.append(transcript[j])
    return count

# passage-related sequence matching features 
def brownfox_featurize(transcript, reference="The Quick Brown Fox jumps over the lazy dog."):
    seq=difflib.SequenceMatcher(a=transcript.lower(), b=reference.lower())
    return 100*seq.ratio()

def caterpillar_featurize(transcript, reference="Do you like amusement parks? Well, I sure do. To amuse myself, I went twice last spring. My most MEMORABLE moment was riding on the Caterpillar, which is a gigantic roller coaster high above the ground. When I saw how high the Caterpillar rose into the bright blue sky I knew it was for me. After waiting in line for thirty minutes, I made it to the front where the man measured my height to see if I was tall enough. I gave the man my coins, asked for change, and jumped on the cart. Tick, tick, tick, the Caterpillar climbed slowly up the tracks. It went SO high I could see the parking lot. Boy was I SCARED! I thought to myself, â€œThereâ€™s no turning back now.â€ People were so scared they screamed as we swiftly zoomed fast, fast, and faster along the tracks. As quickly  as it started, the Caterpillar came to a stop. Unfortunately, it was time to pack the car and drive home. That night I dreamt of the wild ride on the Caterpillar. Taking a trip to the amusement park and riding on the Caterpillar was my MOST memorable moment ever!"):
    seq=difflib.SequenceMatcher(a=transcript.lower(), b=reference.lower())
    return 100*seq.ratio()

def mandog_featurize(transcript, reference="the man saw the boy that the dog chased"):
    # similarity (https://stackoverflow.com/questions/1471153/string-similarity-metrics-in-python)
    seq=difflib.SequenceMatcher(a=transcript.lower(), b=reference.lower())
    return 100*seq.ratio()

def tourbus_featurize(transcript, reference="the tour bus is coming into the town to pick up the people from the hotel to go swimming."):
    seq=difflib.SequenceMatcher(a=transcript.lower(), b=reference.lower())
    return 100*seq.ratio()

def bnt_featurize(transcript):
    # use 'deepspeech_dict' setting in Allie ML framework
    transcript=transcript.lower().split()
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

def nonword_featurize(transcript):
    # use 'deepspeech_nodict' setting in Allie ML framework
    transcript=transcript.lower().split()
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

def voiceome_featurize(audiofile, transcript, directory):
    # define feature labels and extract unique quality features in the Voiceome 

    labels = ['brownfox_feature', 'animal_feature', 'letterf_feature', 'caterpillar_feature', 
              'mandog_feature', 'tourbus_feature', 'bnt_feature', 'nonword_feature']
    features = list()

    # get features 
    brownfox_feature=brownfox_featurize(transcript)
    features.append(brownfox_feature)
    animal_feature=animal_featurize(transcript)
    features.append(animal_feature)
    letterf_feature=letterf_featurize(transcript)
    features.append(letterf_feature)
    caterpillar_feature=caterpillar_featurize(transcript)
    features.append(caterpillar_feature)
    mandog_feature=mandog_featurize(transcript)
    features.append(mandog_feature)
    tourbus_feature=tourbus_featurize(transcript)
    features.append(tourbus_feature)
    bnt_feature=bnt_featurize(transcript)
    features.append(bnt_feature)
    nonword_feature=nonword_featurize(transcript)
    features.append(nonword_feature)

    return features, labels
