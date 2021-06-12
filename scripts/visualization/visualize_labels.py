import pandas as pd
import os, shutil, time
import seaborn as sns
import matplotlib.pyplot as plt

def convert(list_):
	unique=list(set(list_))
	unique_dict=dict()
	newlist=list()
	for i in range(len(unique)):
		unique_dict[unique[i]]=i
	for i in range(len(list_)):
		newlist.append(unique_dict[list_[i]])
	return newlist 

def get_survey(csvfile):
	if csvfile.find('A1') > 0:
		return 'A1'
	elif csvfile.find('A2') > 0:
		return 'A2'
	elif csvfile.find('A3') > 0:
		return 'A3'
	elif csvfile.find('A4') > 0:
		return 'A4'
	elif csvfile.find('B1') > 0:
		return 'B1'
	elif csvfile.find('B2') > 0:
		return 'B2'
	elif csvfile.find('B3') > 0:
		return 'B3'
	elif csvfile.find('C2') > 0:
		return 'C2'
	elif csvfile.find('C3') > 0:
		return 'C3'
	elif csvfile.find('D4') > 0:
		return 'D4'
	else:
		return 'OTHER'

def convert_gender(list_):
	genders=list()
	for i in range(len(list_)):
		gender=list_[i]
		if gender not in ['Male', 'Female']:
			if gender.lower().find('male') >= 0:
				gender='Male'
			elif gender.lower().find('female') >=0:
				gender='Female'
			else: 
				gender='Male'
		else:
			gender=gender
		genders.append(gender)
	return genders

labels=['Do you currently smoke tobacco or any other substance on a regular basis (daily or weekly)?',
	'How many years have you smoked for or did you smoke for? If you have smoked for less than 1 year, please select 0.',
	'How many cigarettes a day did/do you smoke on average? ',
	'Have you ever had any surgery or radiation around your head or neck?',
	'What time did you wake up this morning?',
	'How many times per week do you exercise for more than 30 minutes with at least a moderate intensity?',
	'Did you exercise with moderate or more intensity for at least 30 minutes today?',
	'Do you suffer from high blood pressure, heart disease, or other related conditions?',
	'I consider myself:',
	'Do you have significant oral or dental problems which might affect your ability to speak clearly?',
	'Do you have normal hearing or if requiring assistive hearing devices, then is your corrected hearing functionally normal?',
	'Do you have normal vision or if requiring glasses or contacts, then is your corrected vision functionally normal?',
	'Do you have a history of dyslexia, learning disability, or attention-deficit disorders?',
	'How many hours were you asleep last night?',
	'On a scale of 1-10, **how well do you feel** right now? (1 - not at all well, 10 - extremely well).',
	'On a scale of 1-10, how **stressed** are you right now? (1 - not at all stressed, 10 - extremely stressed).',
	'On a scale of 1-10, how **tired** are you right now? (1 - not tired at all, 10 - extremely tired)',
	'On a scale of 1-10, how **happy** are you right now? (1 - not at all happy, 10 - extremely happy).',
	'On a scale of 1-10, how **hydrated** do you feel right now? (1- not at all hydrated, 10- extremely hydrated).',
	'On a scale of 1-10, how **hungry** are you right now? (1 - not at all hungry, 10 - extremely hungry).',
	'On a scale of 1-10, how severe are your **allergies** right now? (1- no allergies at all, 10 - extremely severe).',
	'On a scale of 1-10, how severe of a **headache** do you have right now? (1 - no headache at all, 10 - extremely severe).',
	'On a scale 1-10, how severe is the **pain** you feel right now? (1 - no pain at all, 10 - extremely severe).\xa0',
	'On a scale 1-10, how **sore is your throat** right now? (1 - no sore throat at all, 10 - extremely severe).',
	'How **severe is your acne or other skin condition**? (1 - no acne at all, 10 - extremely severe).',
	'On a scale from 1-10, how would you rate your **overall quality of life?** (1- not at all good, 10 - extremely good).',
	'With which gender do you most identify? ', 'What is your age in years? (e.g. 25).', 'What is your highest level of education?',
	'What is your current employment status? ', 'What is your marital status?', 'What is your total household income?',
	'What is your fluency with the English language?', "What is your height? (e.g. 5'10'').",
	'What is your weight in pounds? (e.g. 150 lbs).',
	'Do you have a cold today? Note that some symptoms of a cold include having a sore throat, runny nose, cough, congestion, and/or sinus pressure.',
	'How would you best describe yourself? Select all options that apply.',
	'The following questions will help us further assess whether or not you are experiencing COVID-19 related symptoms. Please answer these questions to the best of your ability.  ---  Have you ever been tested for COVID-19?',
	'If you have been tested for COVID-19, when was your test performed?',
	'Do you have a fever or feel too hot?',
	'Do you feel chills or shivers (feel too cold)?',
	'Do you have a persistent cough (coughing a lot for more than an hour, or 3 or more coughing episodes in 24 hours)?',
	'Are you experiencing unusual fatigue?',
	'Are you experiencing unusual shortness of breath or have trouble breathing?',
	'Do you have a sore or painful throat?', 'Do you have loss of smell / taste?',
	'Do you have an unusually hoarse voice?',
	'Are you feeling an unusual chest pain or tightness in your chest?',
	'Have you been skipping meals?',
	'**Over the last 2 weeks, how often have you been bothered by any of the following problems?**  ---  Little interest or pleasure in doing things',
	' Feeling down, depressed, or hopeless',
	'Trouble falling or staying asleep, or sleeping too much',
	'Feeling tired or having little energy',
	'Poor appetite or overeating',
	'Feeling bad about yourself or that you are a failure or have let yourself or your family down',
	'Trouble concentrating on things, such as reading the newspaper or watching television',
	'Moving or speaking so slowly that other people could have noticed. Or the opposite being so figety or restless that you have been moving around a lot more than usual',
	'Thoughts that you would be better off dead, or of hurting yourself',
	'**Over the last 2 weeks, how often have you been bothered by the following problems?**  ---  Feeling nervous, anxious, or on edge', 'Not being able to stop or control worrying ',
	'Worrying too much about different things',
	'Trouble relaxing ',
	"Being so restless that it's hard to sit still ",
	'Becoming easily annoyed or irritable ',
	'Feeling afraid as if something awful might happen',
	'**There are 5 statement groups on this questionnaire: read each group of statements carefully. Choose one statement in each group that best describes the way you have been feeling the past week.**  Please note: the word "occasionally" when used here means once or twice; "often" means several times or more and "frequently" means most of the time.  ---  Statement 1',
	'Statement 2 ',
	'Statement 3',
	'Statement 4',
	'Statement 5',
	'How often do you have a drink containing alcohol?',
	'How many standard drinks containing alcohol do you have on a typical day?',
	'How often do you have six or more drinks on one occasion?',
	'The next few questions assess how any disability or disorder you have impairs your daily functioning. If you have no disabilities, you may answer 0 to all of these questions.  ---  **Work / school responsibilities**  The symptoms from my disability or disorder have disrupted my job responsibilities or school work (0 - not at all to 10 - extremely):  ![](https://s3.amazonaws.com/www.voiceome.org/data/Screen+Shot+2020-03-12+at+1.21.28+AM.png)',
	'**Social life / leisure activities**  The symptoms from my disability or disorder have disrupted my social life / leisure activities (0 - not at all to 10 - extremely):  ![](https://s3.amazonaws.com/www.voiceome.org/data/Screen+Shot+2020-03-12+at+1.21.28+AM.png)',
	'**Family life / home responsibilities**  The symptoms from my disability or disorder have disrupted my family life / home responsibilities (0 - not at all to 10 - extremely):  ![](https://s3.amazonaws.com/www.voiceome.org/data/Screen+Shot+2020-03-12+at+1.21.28+AM.png)',
	'**Please answer the questions below, rating yourself on each of the criteria shown using the scale on the right side of the page. As you answer each question, pick the answer that best describes how you have felt and conducted yourself over the past 6 months.**  ---  How often do you have trouble wrapping up the final details of a project, once the challenging parts have been done?',
	'How often do you have difficulty getting things in order when you have to do a task that requires organization?',
	'How often do you have problems remembering appointments or obligations?',
	'When you have a task that requires a lot of thought, how often do you avoid or delay getting started?  ',
	'How often do you fidget or squirm with your hands or feet when you have to sit down for a long time?  ',
	'How often do you feel overly active and compelled to do things, like you were driven by a motor?',
	'**In thinking about your sleep patterns throughout the past 2 WEEKS, please respond to the following questions.**  ---  Difficulty falling asleep',
	'Difficulty staying asleep',
	'Problems waking up too early',
	'How SATISFIED/DISSATISFIED are you with your CURRENT sleep pattern?',
	'How NOTICEABLE to others do you think your sleep problem is in terms of impairing the quality of your life?',
	'How WORRIED/DISTRESSED are you about your current sleep problem?',
	'To what extent do you consider your sleep problem to INTERFERE with your daily functioning (e.g. daytime fatigue, mood, ability to function at work/daily chores, concentration, memory, mood, etc.) CURRENTLY?',
	'**Sometimes things happen to people that are unusually or especially frightening, horrible, or traumatic. For example: a serious accident or fire, a physical or sexual assault or abuse, an earthquake or flood, a war, seeing someone be killed or seriously injured, or having a loved one die through homicide or suicide.**  ---  Have you ever experienced this kind of event?',
	'The Stanford Sleepiness Scale is comprised of a rating from 1 to 7 as described below. Please select the rating which best describes your current state.']
	# 'bmis',
	# 'phq9_depression',
	# 'gad7_anxiety',
	# 'altman_mania',
	# 'adhd_selfrating',
	# 'severity_insomnia',
	# 'common_voice_age']

scales=['On a scale of 1-10, **how well do you feel** right now? (1 - not at all well, 10 - extremely well).',
	'On a scale of 1-10, how **stressed** are you right now? (1 - not at all stressed, 10 - extremely stressed).',
	'On a scale of 1-10, how **tired** are you right now? (1 - not tired at all, 10 - extremely tired)',
	'On a scale of 1-10, how **happy** are you right now? (1 - not at all happy, 10 - extremely happy).',
	'On a scale of 1-10, how **hydrated** do you feel right now? (1- not at all hydrated, 10- extremely hydrated).',
	'On a scale of 1-10, how **hungry** are you right now? (1 - not at all hungry, 10 - extremely hungry).',
	'On a scale of 1-10, how severe are your **allergies** right now? (1- no allergies at all, 10 - extremely severe).',
	'On a scale of 1-10, how severe of a **headache** do you have right now? (1 - no headache at all, 10 - extremely severe).',
	'On a scale 1-10, how severe is the **pain** you feel right now? (1 - no pain at all, 10 - extremely severe).\xa0',
	'On a scale 1-10, how **sore is your throat** right now? (1 - no sore throat at all, 10 - extremely severe).',
	'How **severe is your acne or other skin condition**? (1 - no acne at all, 10 - extremely severe).',
	'On a scale from 1-10, how would you rate your **overall quality of life?** (1- not at all good, 10 - extremely good).']

# now get all of these labels formatted appropriately for the visualization 
curdir=os.getcwd()
os.chdir('clean')
csvfiles=list()
listdir=os.listdir()
for i in range(len(listdir)):
	if listdir[i].endswith('.csv'):
		csvfiles.append(listdir[i])

os.chdir(curdir)

visualization_dir=os.getcwd()+'/visualizations'

folder='visualizations'
try:
	os.mkdir(folder)
	os.chdir(folder)
except:
	shutil.rmtree(folder)
	os.mkdir(folder)
	os.chdir(folder)

for i in range(len(labels)):
	try:

		x_axis=list()
		x=list()
		y=list()
		genders=list()

		for j in range(len(csvfiles)):
			os.chdir(curdir)
			os.chdir('clean')
			g=pd.read_csv(csvfiles[j])
			survey=get_survey(csvfiles[j])
			for k in range(len(g)):
				x_axis.append(survey)

			y=y+list(g[labels[i]])

			genders=genders+convert_gender(list(g['With which gender do you most identify? ']))

		fig=sns.violinplot(x=x_axis, y=convert(y), hue=genders, split=True, scale="count")
		fig = fig.get_figure()
		
		os.chdir(visualization_dir)
		title=labels[i][0:20].replace(' ','_')
		plt.title(title)
		plt.xlabel('survey number')
		plt.ylabel('value')
		fig.tight_layout()
		fig.savefig('%s.png'%(str(i)+'_'+title))
		plt.close(fig)

	except:
		pass


# correlation plots with feature removal if corr > 0.90
# https://towardsdatascience.com/feature-selection-correlation-and-p-value-da8921bfb3cf

# now remove correlated features
# --> p values
# --> https://towardsdatascience.com/the-next-level-of-data-visualization-in-python-dd6e99039d5e / https://github.com/WillKoehrsen/Data-Analysis/blob/master/plotly/Plotly%20Whirlwind%20Introduction.ipynb- plotly for correlation heatmap and scatterplot matrix
# --> https://seaborn.pydata.org/tutorial/distributions.html

os.chdir(curdir)
os.chdir('clean')
data=pd.read_csv('clean_Voiceome_A1_mTurk_push2.csv')
data=data[scales]
corr = data.corr()

os.chdir(visualization_dir)
plt.figure(figsize=(12,12))
fig=sns.heatmap(corr)
fig = fig.get_figure()
plt.title('Rating scale heatmap', size=20)
fig.tight_layout()
fig.savefig('heatmap.png')
plt.close(fig)
