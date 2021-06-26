'''

| | | |     (_)                              
| | | | ___  _  ___ ___  ___  _ __ ___   ___ 
| | | |/ _ \| |/ __/ _ \/ _ \| '_ ` _ \ / _ \
\ \_/ / (_) | | (_|  __/ (_) | | | | | |  __/
 \___/ \___/|_|\___\___|\___/|_| |_| |_|\___|


This is a command-line interface for the Voiceome repository.

This makes it easy-to-call many common APIs for the Voiceome dataset.

which include:

	- Clean API - {link}
	- Featurize API - {link}
	- Quality API - {link}
	- Reference API - {link}
	- Test API - {link}
	- Url API - {link}
	- Visualize API - {link}

All of these commands will ingest the default settings via 
the settings.json document, so be sure to set the right settings
when calling the API.

Usage: cli.py [options]

Options:
  -h, --help            show this help message and exit
  --c=command, --command=command
                        the target command (cleaning API = 'clean',  features
                        API = 'features',  quality API = 'quality',
                        references API = 'reference',  samples API = 'sample',
                        testing API = 'test',  urls API = 'urls',  visualize
                        API = 'visualize',  list/change default settings =
                        'settings')
  --a=age_gender, --agegender=age_gender
                        specify the age and gender in CamelCase for references
                        ('TwentiesMale' =  male aged 20s); if not used will
                        default to settings.json value.
  --d=dir, --dir=dir    an array of the target directory (or directories) that
                        contains sample files all APIs (e.g.
                        '/Users/jim/desktop/allie/train_dir/teens/')
  --e=feature_embedding, --embedding=feature_embedding
                        the feature embedding to use for reference ranges
                        (e.g. 'OpenSmile'); if not used it will default to
                        settings.json value.
  --f=feature, --feature=feature
                        the feature value in a feature embedding to use for a
                        reference range (e.g.
                        'F0semitoneFrom27.5Hz_sma3nz_amean'); if not used it
                        will default to settings.json value.
  --fi=file, --file=file
                        an audio file to extract relevant quality metrics and
                        transcribe (e.g. 'test.wav')
  --t=task, --task=task
                        the task type to focus on (e.g. 'microphone_task'); if
                        not used it will default to settings.json value.
  --v=visualizationtype, --vtype=visualizationtype
                        the visualization type that you'd like to use - two
                        options: ['bar', 'bar_cohorts']
  --verbosity=verbosity
                        whether or not to display visualizations/charts on the
                        screen ([True or False]).
  --u=urls, --urls=urls
                        the url links for surveys in the Voiceome Study
                        (useful for cloning surveys via the SurveyLex
                        interface).

If you have any questions or would like to contribute to our community,
please reach out to Jim Schwoebel @ jim.schwoebel@gmail.com.
'''
import os, shutil, time, json
from optparse import OptionParser
from tqdm import tqdm
from pyfiglet import Figlet
from beautifultable import BeautifulTable
import matplotlib.pyplot as plt
import numpy as np

# helper function to render modules and functions
def render(text, f):
	print(f.renderText(text))

print('--------------------------------------------------------------')
f=Figlet(font='doom')
render('Voiceome',f)
print('--------------------------------------------------------------')
print('For help, type ```python3 cli.py --help```')
print('--------------------------------------------------------------')
print('For more info, visit: \nhttps://github.com/jim-schwoebel/voiceome')
print('--------------------------------------------------------------')

###############################################################
##                    HELPER FUNCTIONS                       ##
###############################################################

def clean_folder(allie_dir, target_directory):
	'''
	Cleans audio to Mono 16000Hz by folder using the Allie ML framework/FFmpeg.
	'''
	cur_dir=os.getcwd()
	os.chdir(allie_dir)
	os.system('python3 allie.py --command clean --dir %s --sampletype audio'%(target_directory))
	os.chdir(cur_dir)

def featurize_folder(allie_dir, target_directory):
	'''
	Featurizes audio by folder using the Allie ML framework/FFmpeg,
	transcribes relative to the settings specified in the Allie ML framework
	(here it is ['deepspeech_dict', 'deepspeech_nodict'])
	'''
	cur_dir=os.getcwd()
	os.chdir(allie_dir)
	os.system('python3 allie.py --command features --dir %s --sampletype audio'%(target_directory))
	os.chdir(cur_dir)

def get_quality_features(folder):
	'''
	Gets quality features upon having access to a reference folder.
	'''
	pass 

def visualize():
	'''
	visualize data with 2 specified settings.
	'''
	pass 

def get_references():
	'''
	gets references, as specified in prior scripts - outputs as a beautiful table.
	'''
	pass 

def change_settings(settings, feature_options):
	print(settings)
	print('\n')
	settingslist=list(settings)
	textinput=input('Would you like to change any of these settings? Yes (-y) or No (-n)\n')
	if textinput.lower().replace(' ','') in ['yes','y']:
		textinput=input('What setting would you like to change?\n')
		while textinput not in settingslist and textinput.lower() != 'version':
			print('Setting not recognized, options are:')
			time.sleep(0.5)
			for i in range(len(settingslist)):
				if settingslist[i] != 'version':
					print('- '+settingslist[i])
					time.sleep(0.05)
			textinput=input('What setting would you like to change?\n')

		if textinput == 'FeatureEmbedding':
			print('options are: ')
			new_options=list(feature_options)
			print(new_options)
			newsetting=input('What setting would you like to set here?\n')
			while newsetting not in new_options:
				print(newsetting + ' is not a recognized embedding. Options include')
				print(new_options)
				newsetting=input('What setting would you like to set here?\n')

		elif textinput == 'FeatureType':
			print('options are: ')
			new_options=feature_options[settings['FeatureEmbedding']]
			print(new_options)
			newsetting=input('What setting would you like to set here?\n')
			while newsetting not in new_options:
				print(newsetting + ' is not a recognized feature. Options include')
				print(new_options)
				newsetting=input('What setting would you like to set here?\n')
		else:
			newsetting=input('What setting would you like to set here?\n')

		# curdir 
		if str(newsetting).title() in ['True']:
			newsetting=True 
		elif str(newsetting).title() in ['False']:
			newsetting=False

		settings[textinput]=newsetting

		print(type(newsetting))
		jsonfile=open('settings.json','w')
		json.dump(settings,jsonfile)
		jsonfile.close()

def print_urls():
	'''
	A imple script to output URL links for surveys in the Voiceome study. 
	This will make it easier to clone surveys @ SurveyLex.com and replicate our work.
	'''
	render('Survey Links',f)
	print('(useful for cloning surveys @ https://surveylex.com)')
	print('--------------------------------------------------------------')
	print('Survey A:')
	print('https://app.surveylex.com/surveys/8a32cbb0-cc8a-11eb-9ea3-938cc8b6d71e')
	print('--------------------------------------------------------------')
	print('Survey B:')
	print('https://app.surveylex.com/surveys/061da3f0-a637-11eb-bcc9-eba67643f616')
	print('--------------------------------------------------------------')
	print('Survey C:')
	print('https://app.surveylex.com/surveys/a66494c0-a824-11ea-88c1-ab37bac1e1d4')
	print('--------------------------------------------------------------')
	print('Survey D:')
	print('https://app.surveylex.com/surveys/53737620-a637-11eb-bcc9-eba67643f616')
	print('--------------------------------------------------------------')

def get_samples(task):
	if task == 'consent':
		os.system('open -a "Google Chrome" https://github.com/jim-schwoebel/voiceome/wiki/0.-Consent-form')
	elif task == 'microphone_task':
		os.system('open -a "Google Chrome" https://drive.google.com/file/d/1c54zKMuBxCririQrrbvKBuJG6c0UpgOK/view?usp=sharing')
	elif task == 'freespeech_task':
		os.system('open -a "Google Chrome" https://drive.google.com/file/d/1RcC8PY84rPg7qZKA6BFMXc2XmBElXM6e/view?usp=sharing')
	elif task == 'category_task':
		os.system('open -a "Google Chrome" https://drive.google.com/file/d/114XDxQwd621pQM5JYukXPRm5QONTpaGW/view?usp=sharing')
	elif task == 'letterf_task':
		os.system('open -a "Google Chrome" https://drive.google.com/file/d/1m-gRiiaPS4m7bFx7B22rgC5ZsBsejaZ9/view?usp=sharing')
	elif task == 'paragraph_task':
		os.system('open -a "Google Chrome" https://drive.google.com/file/d/1pF4Jw6vTL3GOewZOn-dceD4z645ACEzg/view?usp=sharing')
	elif task == 'phonation_task':
		os.system('open -a "Google Chrome" https://drive.google.com/file/d/1XUrfVM_dnDeA21jaHRXtn6guspZczTeV/view?usp=sharing')
	elif task == 'papapa_task':
		os.system('open -a "Google Chrome" https://drive.google.com/file/d/1nqknAogTF90Zw6Cckcg85CjObVoYSpBG/view?usp=sharing')
	elif task == 'pataka_task':
		os.system('open -a "Google Chrome" https://drive.google.com/file/d/1WFlkKbyUCREtyhybN-TFVGs3h8-Yj4nc/view?usp=sharing')
	elif task == 'bnt_task':
		os.system('open -a "Google Chrome" https://drive.google.com/file/d/1HgPxr0Kiz2z5PNtJ10iXAZnN0dnxhQJQ/view?usp=sharing')
	elif task == 'nonword_task':
		os.system('open -a "Google Chrome" https://drive.google.com/file/d/1yaKH85Gm6kvuSjThKMkWnofWUS-VvMkG/view?usp=sharing')
	elif task == 'recall_task':
		os.system('open -a "Google Chrome" https://drive.google.com/file/d/1OpNdamMRar9eJx2q3iouzKVZf02nCyLB/view?usp=sharing')
	elif task == 'diagnosis_task':
		os.system('open -a "Google Chrome" https://drive.google.com/file/d/13v6Sj5GB6dDUWWTBaIbG2qGX9pWDjbEM/view?usp=sharing')
	elif task == 'medication_task': 
		os.system('open -a "Google Chrome" https://drive.google.com/file/d/1I7PwZbK2xu9PPNyYoJ8qyW1bWk2qlyFC/view?usp=sharing')
	elif task == 'confounds':
		os.system('open -a "Google Chrome" https://github.com/jim-schwoebel/voiceome/wiki/14.-Confounding-questions')
	elif task == 'demographics':
		os.system('open -a "Google Chrome" https://github.com/jim-schwoebel/voiceome/wiki/15.-Demographic-questions')
	elif task == 'heath_labels':
		os.system('open -a "Google Chrome" https://github.com/jim-schwoebel/voiceome/wiki/16.-Health-labels')
	elif task == 'fun_facts':
		os.system('open -a "Google Chrome" https://github.com/jim-schwoebel/voiceome/wiki/17.-Fun-Facts')
	else:
		print('%s not recognized. Please insert another task and try again.')
		print('--------------------------------------------------------------')
		print('options include:')
		print('--------------------------------------------------------------')
		print(['consent',
			   'microphone_task',
			   'freespeech_task',
			   'category_task',
			   'letterf_task',
			   'paragraph_task',
			   'phonation_task',
			   'papapa_task',
			   'pataka_task',
			   'bnt_task',
			   'nonword_task',
			   'recall_task',
			   'diagnosis_task',
			   'medication_task',
			   'confounds',
			   'demographics',
			   'health_labels',
			   'fun_facts'])
		print('--------------------------------------------------------------')

def command_error(command, commands):
	print('ERROR - %s is not a valid command in the Voiceome CLI. Please use one of these commands'%(str(command)))
	print('\n')
	for i in range(len(commands)):
		print(' - '+commands[i])
	print('\n\n')


def get_reference(task, feature_embedding, feature, agegender, basedir):

    curdir=os.getcwd()

    os.chdir(basedir)
    os.chdir('data')
    os.chdir('references')

    # go to proper location
    if task in ['microphone_task', 'freespeech_task', 'picture_task', 'category_task',
                'letterf_task', 'paragraph_task', 'ahh_task', 'papapa_task', 'pataka_task',
                'mandog_task', 'tourbus_task', 'diagnosis_task', 'medication_task']:
        os.chdir('main_tasks')

    elif task in ['mushroom_task', 'bicycle_task', 'camel_task', 'camera_task', 'chicken_task', 
                  'dinosaur_task', 'balloon_task', 'glasses_task', 'gorilla_task', 'volcano_task', 
                  'asparagus_task', 'pizza_task', 'railroad_task', 'scissors_task', 'shovel_task', 
                  'flamingo_task', 'suitcase_task', 'telephone_task', 'ladder_task', 'toothbrush_task', 
                  'hammer_task', 'coconut_task', 'wallet_task', 'pineapple_task', 'cactus_task']:
        os.chdir('bnt_task')

    elif task in ['plive_task', 'broe_task', 'jome_task', 'zulx_task', 'zowl_task', 
                  'vave_task', 'fwov_task', 'nayb_task', 'kwaj_task', 'bwiz_task']:
        os.chdir('nonword_task')

    # 00. Microphone check task = 'microphone_task'
    if task == 'microphone_task': 
        data=json.load(open('00_mic_check.json'))

    # 01. Free speech task = 'freespeech_task'
    elif task == 'freespeech_task':
        data=json.load(open('01_free_speech.json'))

    # 02. Picture description task = 'picture_task'
    elif task == 'picture_task':
        data=json.load(open('02_picture_description.json'))

    # 03. Category naming task = 'category_task'
    elif task == 'category_task':
        data=json.load(open('03_animal_naming.json'))

    # 04. Letter {FAS} Tasks = 'leterf_task'
    elif task == 'letterf_task':
        data=json.load(open('04_letter_f_naming.json'))

    # 05. Paragraph reading task = 'paragraph_task'
    elif task == 'paragraph_task':
        data=json.load(open('05_caterpillar_reading.json'))

    # 06. Sustained phonation ('ahh') = 'ahh_task'
    elif task == 'ahh_task':
        data=json.load(open('06_sustained_ahh.json'))

    # 07. Pa pa pa task = 'papapa_task'
    elif task == 'papapa_task':
        data=json.load(open('07_pa_pa_pa.json'))

    # 08. Pa taska ka task - 'pataka_task'
    elif task == 'pataka_task':
        data=json.load(open('08_pa_ta_ka.json'))

    # 09. Confrontational naming task (different images) - 'bnt_task'
    elif task == 'mushroom_task':
        data=json.load(open('01_Mushroom.json'))
    elif task == 'bicycle_task':
        data=json.load(open('02_Bicycle.json'))
    elif task == 'camel_task':
        data=json.load(open('03_Camel.json'))
    elif task == 'camera_task':
        data=json.load(open('04_Camera.json'))
    elif task == 'chicken_task':
        data=json.load(open('05_Chicken.json'))
    elif task == 'dinosaur_task':
        data=json.load(open('06_Dinosaur.json'))
    elif task == 'balloon_task':
        data=json.load(open('07_Balloon.json'))
    elif task == 'glasses_task':
        data=json.load(open('08_Glasses.json'))
    elif task == 'gorilla_task':
        data=json.load(open('09_Gorilla.json'))
    elif task == 'volcano_task':
        data=json.load(open('10_Volcano.json'))
    elif task == 'asparagus_task':
        data=json.load(open('11_Asparagus.json'))
    elif task == 'pizza_task':
        data=json.load(open('12_Pizza.json'))
    elif task == 'railroad_task':
        data=json.load(open('13_Railroad.json'))
    elif task == 'scissors_task':
        data=json.load(open('14_Scissors.json'))
    elif task == 'shovel_task':
        data=json.load(open('15_Shovel.json'))
    elif task == 'flamingo_task':
        data=json.load(open('16_Flamingo.json'))
    elif task == 'suitcase_task':
        data=json.load(open('17_Suitcase.json'))
    elif task == 'telephone_task':
        data=json.load(open('18_Telephone.json'))
    elif task == 'ladder_task':
        data=json.load(open('19_Ladder.json'))
    elif task == 'toothbrush_task':
        data=json.load(open('20_Toothbrush.json'))
    elif task == 'hammer_task':
        data=json.load(open('21_Hammer.json'))
    elif task == 'coconut_task':
        data=json.load(open('22_Coconut.json'))
    elif task == 'wallet_task':
        data=json.load(open('23_Wallet.json'))
    elif task == 'pineapple_task':
        data=json.load(open('24_Pineapple.json'))
    elif task == 'cactus_task':
        data=json.load(open('25_Cactus.json'))


    # 10. Nonword task (different nonwords) - 'nonword_task'
    elif task == 'plive_task':
        data=json.load(open('01_Plive.json'))
    elif task == 'broe_task':
        data=json.load(open('02_Fwov.json'))
    elif task == 'jome_task':
        data=json.load(open('03_Zowl.json'))
    elif task == 'zulx_task':
        data=json.load(open('04_Zulx.json'))
    elif task == 'zowl_task':
        data=json.load(open('05_Vave.json'))
    elif task == 'vave_task':
        data=json.load(open('06_Kwaj.json'))
    elif task == 'fwov_task':
        data=json.load(open('07_Jome.json'))
    elif task == 'nayb_task':
        data=json.load(open('08_Bwiz.json'))
    elif task == 'kwaj_task':
        data=json.load(open('09_Broe.json'))
    elif task == 'bwiz_task':
        data=json.load(open('10_Nayb.json'))

    # 11. Immediate recall task -  'mandog_task' or 'tourbus_task'
    elif task == 'mandog_task':
        data=json.load(open('45_repeat_mandog.json'))

    elif task == 'tourbus_task':
        data=json.load(open('47_repeat_schoolbus.json'))

    # 12. Spoken diagnosis task - 'diagnosis_task'
    elif task == 'diagnosis_task':
        data=json.load(open('48_diagnosis_task.json'))

    # 13. Spoken medication task - 'medication_task'
    elif task == 'medication_task':
        data=json.load(open('49_medication_task.json'))

    # calculate possible featurestypes here 
    os.chdir(basedir)
    os.chdir('data')
    os.chdir('options')
    options=json.load(open('feature_options.json'))
    feature_embeddings=list(options)
    features=list()
    for i in range(len(feature_embeddings)):
        features=features+options[feature_embeddings[i]]

    # print(features)

    # age options
    agegenders=['TwentiesMale', 'TwentiesFemale', 'ThirtiesMale', 'ThirtiesFemale', 'FourtiesMale', 'FourtiesFemale', 'FiftiesMale', 'FiftiesFemale', 'SixtiesMale', 'SixtiesFemale', 'AllAgesGenders']

    os.chdir(curdir)

    # return results 
    if feature_embedding in feature_embeddings and feature in features and agegender in agegenders:
        return data[feature_embedding][feature][agegender]
    else:
        return 'ERROR - FeatureType, Feature, or Age not recognize. Please check these settings and try again.'

def reference_task_embedding(task, feature_embedding, agegender, basedir):
    # get all options 
    os.chdir(basedir)
    os.chdir('data')
    os.chdir('options')

    feature_options=json.load(open('feature_options.json'))
    feature_embeddings=list(feature_options)

    agegender_options=json.load(open('agegender_options.json'))
    agegenders=agegender_options['AgeGenderOptions']

    names=list()
    means=list()
    stds=list()
    ages=list()
    samplenums=list()

    if feature_embedding in feature_embeddings and agegender in agegenders:
        features=feature_options[feature_embedding]

        for i in range(len(features)):
            data=get_reference(task, feature_embedding, features[i], agegender, basedir)
            names.append(features[i])
            means.append(data['AverageValue'])
            stds.append(data['StdValue'])
            ages.append(agegender)
            samplenums.append(data['SampleNumber'])

    elif feature_embedding not in feature_embeddings:
        print('ERROR - [%s] is not a recognized feature embedding'%(feature_embedding))
    elif agegender not in agegenders:
        print('ERROR - [%s] is not a recognized age and gender'%(agegender))
       
    return names, means, stds, ages, samplenums

def reference_feature_across_tasks(feature_embedding, feature, agegender, basedir):
    # get all options 
    os.chdir(basedir)
    os.chdir('data')
    os.chdir('options')

    feature_options=json.load(open('feature_options.json'))
    feature_embeddings=list(feature_options)        

    agegender_options=json.load(open('agegender_options.json'))
    agegenders=agegender_options['AgeGenderOptions']

    task_options=json.load(open('task_options.json'))
    tasks=task_options['AllTasks']

    names=list()
    means=list()
    stds=list()
    ages=list()
    samplenums=list()

    if agegender in agegenders and feature_embedding in feature_embeddings:
        features=feature_options[feature_embedding]

        for i in range(len(tasks)):
            data=get_reference(tasks[i], feature_embedding, feature, agegender, basedir)
            names.append(tasks[i])
            means.append(data['AverageValue'])
            stds.append(data['StdValue'])
            ages.append(agegender)
            samplenums.append(data['SampleNumber'])

    elif feature_embedding not in feature_embeddings:
        print('ERROR - [%s] is not a recognized feature embedding'%(feature_embedding))
    elif agegender not in agegenders:
        print('ERROR - [%s] is not a recognized age and gender'%(agegender))
       
    return names, means, stds, ages, samplenums

def visualize_bar(feature, feature_embedding, names, means, stds, agegender, basedir, show):
    os.chdir(basedir)
    os.chdir('data')
    os.chdir('visualizations')
    plt.title(agegender)
    plt.bar(names, means, yerr=stds)
    plt.xticks(rotation='vertical')
    plt.ylabel('%s'%(feature))
    plt.xlabel('Task type')
    plt.tight_layout()
    plt.savefig(feature_embedding+'_'+feature+'.png')
    if show == True:
        plt.show()
    os.chdir(basedir)

def visualize_bar_cohorts(feature, feature_embedding, names, means_1, stds_1, agegender_1, means_2, stds_2, agegender_2, basedir, show):
    os.chdir(basedir)
    os.chdir('data')
    os.chdir('visualizations')

    labels = names
    men_means = means_1
    women_means = means_2

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, men_means, width, label=agegender_1)
    rects2 = ax.bar(x + width/2, women_means, width, label=agegender_2)

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel(feature)
    ax.set_title(agegender_1 + ' | ' + agegender_2)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    plt.xticks(rotation='vertical')

    fig.tight_layout()
    plt.savefig(feature_embedding+'_'+feature+'_'+agegender_1+'_'+agegender_2+'.png')

    if show==True:
        plt.show()
    os.chdir(basedir)

###############################################################
##                     INITIALIZATION                        ##
###############################################################

# initialize variables for the test 
cur_dir=os.getcwd()
allie_dir = os.getcwd()+'/data/test/allie/'
settings=json.load(open(cur_dir+'/settings.json'))
feature_options=json.load(open(cur_dir+'/data/options/feature_options.json'))
agegender_options=json.load(open(cur_dir+'/data/options/agegender_options.json'))['AgeGenderOptions']
transcription_engine=settings['TranscriptEngine']

# for if/then statements later
commands=['clean', 'features', 'quality', 'reference', 'test', 'visualize', 'settings']


# get all the options from the terminal
parser = OptionParser()
parser.add_option("--c", "--command", dest="command",
                  help="the target command (cleaning API = 'clean', \n"+
	                  "features API = 'features', \n"+
	                  "quality API = 'quality', \n"+
	                  "references API = 'reference', \n"+
	                  "samples API = 'sample', \n"
	                  "testing API = 'test', \n"+
	                  "urls API = 'urls', \n"+
	                  "visualize API = 'visualize', \n" +
	                  "list/change default settings = 'settings')", metavar="command")
parser.add_option("--a", "--agegender", dest="age_gender",
				  help="specify the age and gender in CamelCase for references ('TwentiesMale' =  male aged 20s); if not used will default to settings.json value.", metavar="age_gender", 
				  action='append')
parser.add_option("--d", "--dir", dest="dir",
                  help="an array of the target directory (or directories) that contains sample files all APIs (e.g. '/Users/jim/desktop/allie/train_dir/teens/')", metavar="dir",
                  action='append')
parser.add_option("--e", "--embedding", dest="feature_embedding",
				  help="the feature embedding to use for reference ranges (e.g. 'OpenSmile'); if not used it will default to settings.json value.", metavar="feature_embedding")
parser.add_option("--f", "--feature", dest="feature",
				  help="the feature value in a feature embedding to use for a reference range (e.g. 'F0semitoneFrom27.5Hz_sma3nz_amean'); if not used it will default to settings.json value.", metavar="feature")
parser.add_option("--fi", "--file", dest="file",
				  help="an audio file to extract relevant quality metrics and transcribe (e.g. 'test.wav')", metavar="file")
parser.add_option("--t", "--task", dest="task",
				  help="the task type to focus on (e.g. 'microphone_task'); if not used it will default to settings.json value.", metavar="task")
parser.add_option("--v", "--vtype", dest="visualizationtype",
				  help="the visualization type that you'd like to use - two options: ['bar', 'bar_cohorts']", metavar='visualizationtype')
parser.add_option("--verbosity", dest="verbosity",
				  help="whether or not to display visualizations/charts on the screen ([True or False]).", metavar='verbosity')
parser.add_option("--u", "--urls", dest="urls",
				  help="the url links for surveys in the Voiceome Study (useful for cloning surveys via the SurveyLex interface).", metavar="urls")

# parse arguments
(options, args) = parser.parse_args()

# pull arguments from CLI
try:
	agegender = options.age_gender
	if agegender is None:
		agegender = settings['DefaultAgeGender']
except:
	agegender = settings['DefaultAgeGender']
try:
	command = options.command.lower().replace(' ','')
except:
	pass
try:
	directories=options.dir
except:
	directories=[os.getcwd()]
try:
	feature_embedding = options.feature_embedding
	if feature_embedding is None:
		feature_embedding=settings['FeatureEmbedding']
except:
	feature_embedding=settings['FeatureEmbedding']
try:
	feature = options.feature
	if feature is None:
		feature=settings['FeatureType']
except:
	feature=settings['FeatureType']
try:
	file = options.file
except:
	pass
try:
	task = options.task
	if task is None:
		task=settings['Task']
except:
	task=settings['Task']
try:
	urls = options.urls.lower()
except:
	pass
try:
	vtype = options.visualizationtype.lower()
	if vtype is None:
		vtype = 'table_across_tasks'
except:
	vtype = 'table_across_tasks'
try:
	verbosity=options.verbosity.title()
	if verbosity == 'True':
		verbosity=True
	elif verbosity=='False':
		verbosity=False
	elif verbosity is None:
		verbosity=True
except:
	verbosity=True

# now pursue relevant command passed
commands=['clean', 'features', 'quality', 'reference', 'samples', 'settings', 'test', 'visualize', 'urls']

# try:
if str(command) != 'None' and command in commands:

	if command == 'clean':
		'''
		Clean audio files to be mono 16000Hz using Allie API.

		sample command:
			python3 cli.py --command clean --dir /Users/jimschwoebel/desktop/files
		'''
		for i in range(len(directories)):
			clean_folder(allie_dir, directories[i])

	elif command == 'features':
		'''
		featurize using Allie (all features) - transcribes with deepspeech_dict and deepspeech_nodict for analysis

		sample command:
			python3 cli.py --command features --dir /Users/jimschwoebel/desktop/files
		'''
		for i in range(len(directories)):
			featurize_folder(allie_dir, directories[i])

	elif command == 'quality':
		'''
		get quality references - need certain folder formatted appropriately with surveylex export ('./data/test')

		sample command:
			python3 cli.py --command quality --file test.wav

			OR, optionally specify the directory of the audio file if not in the current directory.

			python3 cli.py --command quality --file test.wav --dir /Users/jimschwoebel/desktop
		'''
		if directories is None:
			directories=[os.getcwd()]

		if len(directories) == 1:
			import voiceome_features as vf 
			features, labels = vf.voiceome_featurize(file, transcription_engine, directories[0], allie_dir)
			features_dict = dict(zip(labels, features))
			print('--------------------------------------------------------------')
			render('METRICS - %s'%(file.upper()),f)
			print('--------------------------------------------------------------')
			print(features_dict)
			print('--------------------------------------------------------------')
		else:
			print('You need to specify a --dir and --file (wavfile) in order to transcribe audio and featurize it with quality metrics.')

	elif command == 'reference':
		'''
		get reference ranges across an age and gender for a specific task and feature.
		'''
		# try:
		if vtype == 'table_by_feature':
			'''
			sample command:
				python3 cli.py --command reference --vtype table_by_feature --agegender TwentiesMale
			'''
			data=get_reference(task, feature_embedding, feature, agegender[0], cur_dir)
			print(data)
		elif vtype == 'table_by_embedding':
			'''
			sample command:
				python3 cli.py --command reference --vtype table_by_embedding --agegender TwentiesMale
			'''
			names, means, stds, ages, samplenums =reference_task_embedding(task, feature_embedding, agegender[0], cur_dir)
			table = BeautifulTable()
			table.columns.header = ["Task", "FeatureType", "Feature", "AgeGender", "Average", "Standard Deviation", "Sample Number"]
			for i in range(len(means)):
			    table.rows.append([task, feature_embedding, names[i], agegender, means[i], stds[i], samplenums[i]])
			print(table)
		elif vtype == 'table_across_tasks':
			'''
			sample command:
				python3 cli.py --command reference --vtype table_across_tasks --agegender TwentiesMale
			'''
			names, means, stds, ages, samplenums =reference_feature_across_tasks(feature_embedding, feature, agegender[0], cur_dir)
			table = BeautifulTable()
			table.columns.header = ["Task", "FeatureType", "Feature", "AgeGender", "Average", "Standard Deviation", "Sample Number"]
			for i in range(len(means)):
			    table.rows.append([names[i], feature_embedding, feature, agegender, means[i], stds[i], samplenums[i]])
			print(table)
		# except:
			# print('ERROR - reference does not exist for feature_embedding=%s, feature=%s, and agegender=%s. This may be updated later.'%(feature_embedding, feature, agegender))

	elif command == 'samples':
		'''
		sample command:
			python3 cli.py --command samples 
		'''
		get_samples(task)
	
	elif command == 'test':
		'''
		unit tests on data (transform voiceome.py to be the unit test script)

		sample command:
			python3 cli.py --command test 
		'''
		os.system('python3 test.py')
		
	elif command == 'urls':
		'''
		gets urls for all the Voiceome surveys.
		
		sample command:
			python3 cli.py --command urls
		'''
		print_urls()

	elif command == 'visualize':
		# display in a chart that you can save to desktop and also save to computer
		if vtype == 'bar':
			# visualize these as a bar chart 
			'''
			sample command:
				python3 cli.py --command visualize --agegender FourtiesMale --vtype bar --agegender ThirtiesMale
			'''
			names, means, stds, ages, samplenums =reference_feature_across_tasks(feature_embedding, feature, agegender[0], cur_dir)
			if verbosity == True:
				visualize_bar(feature, feature_embedding, names, means, stds, agegender[0], cur_dir, True)
			else:
				visualize_bar(feature, feature_embedding, names, means, stds, agegender[0], cur_dir, False)

		elif vtype == 'bar_cohorts':
			# visualize these as a bar chart 
			'''
			sample command: 
				python3 cli.py --command visualize --agegender FourtiesMale --vtype bar_cohorts --agegender ThirtiesMale --agegender FiftiesMale
			'''
			if len(agegender) > 1:
				names, means, stds, ages, samplenums =reference_feature_across_tasks(feature_embedding, feature, agegender[0], cur_dir)
				names_2, means_2, stds_2, ages_2, samplenums =reference_feature_across_tasks(feature_embedding, feature, agegender[1], cur_dir)
				if verbosity == True:
					visualize_bar_cohorts(feature, feature_embedding, names, means, stds, agegender[0], means_2, stds_2, agegender[1], cur_dir, True)
				else:
					visualize_bar_cohorts(feature, feature_embedding, names, means, stds, agegender[0], means_2, stds_2, agegender[1], cur_dir, False)
			else:
				print('ERROR - you need to pass at least 2 instances of agegender in order for it to be recognized.')

		else:
			print("Visualization type (%s) not recognized. Please try again with a new --vtype paramater (options: ['bar', 'bar_cohorts'])."%(vtype))
	elif command == 'settings':
		'''
		Change various settings within the voiceome API in settings.json

		sample command:
			python3 cli.py --command settings 
		'''
		change_settings(settings, feature_options)

else:	
	command_error(command, commands)

# except:
		# print('ERROR - no command provided in the Voiceome CLI. \n\nPlease use one of these commands. \n')
		# for i in range(len(commands)):
		# 	print(' - '+commands[i])
		# print('\n')
		# print('Sample usage: \npython3 voiceome.py --command help --dir /Users/jimschwoebel/desktop/allie/train_dir/females --sampletype audio')
		# print('\nFor additional help, type in:')
		# print('python3 allie.py -h\n')
