######################################################################
##                     QUALITY METRICS                              ##
######################################################################
# define feature labels and extract unique quality features in the Voiceome 
import sys, os, json, time, shutil, argparse, random, math
import difflib
import nltk
from nltk import word_tokenize
import speech_recognition as sr

def transcribe(file, transcript_engine, allie_dir):
    # transcript types here.
    import os 
    import speech_recognition as sr

    # use the audio file as the audio source
    r = sr.Recognizer()
    settingsdir = allie_dir 

    # transcription imports (slows down on a per-file vs. folder basis if you load Wav2Vec model - not recommended)
    if transcript_engine == 'Azure':
        import azure.cognitiveservices.speech as speechsdk
    if transcript_engine == 'Wav2Vec':
        import os, pandas as pd, soundfile as sf, torch, glob
        from pathlib import Path
        from transformers import Wav2Vec2ForMaskedLM, Wav2Vec2Tokenizer
        tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
        model = Wav2Vec2ForMaskedLM.from_pretrained("facebook/wav2vec2-base-960h")
    else:
        tokenizer=''
        model=''

    with sr.AudioFile(file) as source:
        audio = r.record(source)  # read the entire audio file

    # now iterate through each transcription type
    if transcript_engine == 'DeepspeechDict':

        curdir=os.getcwd()
        os.chdir(settingsdir+'/features/audio_features/helpers')
        listdir=os.listdir()
        deepspeech_dir=os.getcwd()

        # download models if not in helper directory
        if 'deepspeech-0.7.0-models.pbmm' not in listdir:
            os.system('wget https://github.com/mozilla/DeepSpeech/releases/download/v0.7.0/deepspeech-0.7.0-models.pbmm --no-check-certificate')
        if 'deepspeech-0.7.0-models.scorer' not in listdir:
            os.system('wget https://github.com/mozilla/DeepSpeech/releases/download/v0.7.0/deepspeech-0.7.0-models.scorer --no-check-certificate')

        # initialize filenames
        textfile=file[0:-4]+'.txt'
        newaudio=file[0:-4]+'_newaudio.wav'
        
        if deepspeech_dir.endswith('/'):
            deepspeech_dir=deepspeech_dir[0:-1]

        # go back to main directory
        os.chdir(curdir)

        # convert audio file to 16000 Hz mono audio 
        os.system('ffmpeg -i "%s" -acodec pcm_s16le -ac 1 -ar 16000 "%s" -y'%(file, newaudio))
        command='deepspeech --model %s/deepspeech-0.7.0-models.pbmm --scorer %s/deepspeech-0.7.0-models.scorer --audio "%s" >> "%s"'%(deepspeech_dir, deepspeech_dir, newaudio, textfile)
        print(command)
        os.system(command)

        # get transcript
        transcript=open(textfile).read().replace('\n','')

        # remove temporary files
        os.remove(textfile)
        os.remove(newaudio)


    elif transcript_engine == 'DeepspeechNoDict':

        curdir=os.getcwd()
        os.chdir(settingsdir+'/features/audio_features/helpers')
        listdir=os.listdir()
        deepspeech_dir=os.getcwd()

        # download models if not in helper directory
        if 'deepspeech-0.7.0-models.pbmm' not in listdir:
            os.system('wget https://github.com/mozilla/DeepSpeech/releases/download/v0.7.0/deepspeech-0.7.0-models.pbmm --no-check-certificate')

        # initialize filenames
        textfile=file[0:-4]+'.txt'
        newaudio=file[0:-4]+'_newaudio.wav'
        
        if deepspeech_dir.endswith('/'):
            deepspeech_dir=deepspeech_dir[0:-1]

        # go back to main directory
        os.chdir(curdir)

        # convert audio file to 16000 Hz mono audio 
        os.system('ffmpeg -i "%s" -acodec pcm_s16le -ac 1 -ar 16000 "%s" -y'%(file, newaudio))
        command='deepspeech --model %s/deepspeech-0.7.0-models.pbmm --audio "%s" >> "%s"'%(deepspeech_dir, newaudio, textfile)
        print(command)
        os.system(command)

        # get transcript
        transcript=open(textfile).read().replace('\n','')

        # remove temporary files
        os.remove(textfile)
        os.remove(newaudio)


    elif transcript_engine == 'Wav2Vec':

        # load pretrained model
        audio_input, _ = sf.read(file)

        # transcribe
        input_values = tokenizer(audio_input, return_tensors="pt").input_values
        logits = model(input_values).logits
        predicted_ids = torch.argmax(logits, dim=-1)
        transcript = tokenizer.batch_decode(predicted_ids)[0].lower()

    elif transcript_engine == 'Azure':

        transcript=''
        done=False 

        def stop_cb(evt):
            print('CLOSING on {}'.format(evt))
            nonlocal done
            done = True

        def get_val(evt):
            nonlocal transcript 
            transcript = transcript+ ' ' +evt.result.text
            return transcript

        speech_config = speechsdk.SpeechConfig(subscription=os.environ['AZURE_SPEECH_KEY'], region=os.environ['AZURE_REGION'])
        speech_config.speech_recognition_language=os.environ['AZURE_SPEECH_RECOGNITION_LANGUAGE']
        audio_config = speechsdk.audio.AudioConfig(filename=file)
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
        stream = speechsdk.audio.PushAudioInputStream()

        # Connect callbacks to the events fired by the speech recognizer
        speech_recognizer.recognizing.connect(lambda evt: print('interim text: "{}"'.format(evt.result.text)))
        speech_recognizer.recognized.connect(lambda evt:  print('azure-streaming-stt: "{}"'.format(get_val(evt))))
        speech_recognizer.session_stopped.connect(lambda evt: print('SESSION STOPPED {}'.format(evt)))
        speech_recognizer.canceled.connect(lambda evt: print('CANCELED {}'.format(evt)))
        speech_recognizer.session_stopped.connect(stop_cb)
        speech_recognizer.canceled.connect(stop_cb)

        # start continuous speech recognition
        speech_recognizer.start_continuous_recognition()

        # push buffer chunks to stream
        buffer, rate = read_wav_file(file)
        audio_generator = simulate_stream(buffer)
        for chunk in audio_generator:
          stream.write(chunk)
          time.sleep(0.1)  # to give callback a chance against this fast loop

        # stop continuous speech recognition
        stream.close()
        while not done:
            time.sleep(0.5)

        speech_recognizer.stop_continuous_recognition()
        time.sleep(0.5)  # Let all callback run

    return transcript 

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
        if nltk.pos_tag(word_tokenize(transcript[j])) == 'NN' and transcript[j] not in stopwords:
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

def voiceome_featurize(audiofile, transcript_type, audiofile_directory, allie_dir):
    # go to audio file directory
    curdir=os.getcwd()
    os.chdir(audiofile_directory)

    labels = ['brownfox_feature', 'animal_feature', 'letterf_feature', 'caterpillar_feature', 
              'mandog_feature', 'tourbus_feature', 'bnt_feature', 'nonword_feature']
    features = list()

    # get transcript_type
    transcript = transcribe(audiofile, transcript_type, allie_dir)

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

    # return back to normal directory
    os.chdir(curdir)

    return features, labels