import os, re, time
import pandas as pd
try:
		import datacleaner
except:
		os.system('pip3 install datacleaner==0.1.5')
		import datacleaner

def clean_csv(csvfile):
		'''
		clean csv with helper functions in this file.
		'''

		#################################################################
		##                          HELPER FUNCTIONS                   ##
		#################################################################

		'''
		Calculate net scores of inventories and reformat csv files accordingly.
		'''

		def categorize_csv(csvfile):
				'''
				catgorize sections of the csv columns based on various types of questions. 
				generally, we will not touch start_columns or audio_questions in this section, 
				as they are important to keep intact for analysis.
				'''
				start_columns=['sessionId', 
										'startTime', 
										'mTurk worker ID'] 

				audio_questions=[#normal 
												'Please click the start button and then say:\n\n"The quick brown fox jumps over the lazy dog."\n\nYou may press the Stop button if you finish before the timer runs out.', 
												'Tell us about a recent happy memory based on experiences from the past month.', 
												'Tell us everything you see going on in this picture.\n\n<center>![Aphasia image](http://www.neurolex.co/uploads/alphasia.png)</center>', 
												'Category: ANIMALS. Name all the animals you can think of as quickly as possible before the time elapses below.', 
												'Letter: F. Name all the words beginning with the letter F you can think of as quickly as possible before the time elapses below.', 
												'Please read aloud the following passage:\n"Do you like amusement parks? Well, I sure do. To amuse myself, I went twice last spring. My most MEMORABLE moment was riding on the Caterpillar, which is a gigantic roller coaster high above the ground. When I saw how high the Caterpillar rose into the bright blue sky I knew it was for me. After waiting in line for thirty minutes, I made it to the front where the man measured my height to see if I was tall enough. I gave the man my coins, asked for change, and jumped on the cart. Tick, tick, tick, the Caterpillar climbed slowly up the tracks. It went SO high I could see the parking lot. Boy was I SCARED! I thought to myself, “There’s no turning back now.” People were so scared they screamed as we swiftly zoomed fast, fast, and faster along the tracks. As quickly  as it started, the Caterpillar came to a stop. Unfortunately, it was time to pack the car and drive home. That night I dreamt of the wild ride on the Caterpillar. Taking a trip to the amusement park and riding on the Caterpillar was my MOST memorable moment ever!"', 
												'The goal of this task is to determine how long you can make the vowel sound “/a/” such as when one says the words “cheetah” or “hallelujah.” Click on the sample below to hear an example of the sound. When ready please start the recording, take a deep breath, and then say /a/ for as long as you can sustain the sound. Stop the recording when finished.\n\n[](https://s3.amazonaws.com/www.voiceome.org/data/Aaaaa.mp3).', 
												'The goal of this task is to repeat a single sound as quickly and accurately as possible. The sound for this task is “puh” such as the sound one makes when saying “possible” or “probable.” When ready, start the recording by clicking the timer below and say “puh-puh-puh” repeatedly as quickly and accurately as possible in the time allowed.', 
												'The goal of this task is to repeat 3 different sounds in order as quickly and accurately as possible. The sounds for this task are “puh,” “tuh,”, and “kuh.”\n\n---\n\nAs before “puh” is the sound as when someone says “possible,” “tuh” is the sound as in “tongue,” and “kuh” is the sound as in “karate.”\n\n---\n\nWhen ready, start the recording by clicking the timer below and say “puh-tuh-kuh” repeatedly in that order as quickly and accurately as possible in the time allowed.', 
												'Name this image \n![](https://www.voiceome.org/bnt_images/01_Mushroom.png)', 
												#BNT_imgaes
												'Name this image \n![](https://www.voiceome.org/bnt_images/02_Bicycle.jpg)', 
												'Name this image \n![](https://www.voiceome.org/bnt_images/03_Camel.png)', 
												'Name this image \n![](https://www.voiceome.org/bnt_images/04_Camera.png)', 
												'Name this image \n![](https://www.voiceome.org/bnt_images/05_Chicken.png)', 
												'Name this image \n![](https://www.voiceome.org/bnt_images/06_Dinosaur.jpg)', 
												'Name this image \n![](https://www.voiceome.org/bnt_images/07_Balloon.png)', 
												'Name this image \n![](https://www.voiceome.org/bnt_images/08_Glasses.png)', 
												'Name this image \n![](https://www.voiceome.org/bnt_images/09_Gorilla.png)', 
												'Name this image \n![](https://www.voiceome.org/bnt_images/10_Volcano.png)', 
												'Name this image \n![](https://www.voiceome.org/bnt_images/11_Asparagus.png)', 
												'Name this image \n![](https://www.voiceome.org/bnt_images/12_Pizza_.png)', 
												'Name this image \n![](https://www.voiceome.org/bnt_images/13_Railroad.png)', 
												'Name this image \n![](https://www.voiceome.org/bnt_images/14_Scissors_.png)', 
												'Name this image \n![](https://www.voiceome.org/bnt_images/15_Shovel.png)', 
												'Name this image \n![](https://www.voiceome.org/bnt_images/16_Flamingo.png)', 
												'Name this image \n![](https://www.voiceome.org/bnt_images/17_Suitcase.png)', 
												'Name this image \n![](https://www.voiceome.org/bnt_images/18_Telephone.png)', 
												'Name this image \n![](https://www.voiceome.org/bnt_images/19_Ladder_.jpg)', 
												'Name this image \n![](https://www.voiceome.org/bnt_images/20_Toothbrush_.png)', 
												'Name this image \n![](https://www.voiceome.org/bnt_images/21_Hammer_.png)', 
												'Name this image \n![](https://www.voiceome.org/bnt_images/22_Coconut_3.png)', 
												'Name this image \n![](https://www.voiceome.org/bnt_images/23_Wallet_3.png)', 
												'Name this image \n![](https://www.voiceome.org/bnt_images/24_Pineapple.png)', 
												'Name this image \n![](https://www.voiceome.org/bnt_images/25_Cactus_.png)', 
												# nonwords
												'Speak the nonsense word you see below:\n\n<h1><center>plive</center></h1>', 
												'Speak the nonsense word you see below:\n\n<h1><center>fwov</center></h1>', 
												'Speak the nonsense word you see below:\n\n<h1><center>zowl</center></h1>', 
												'Speak the nonsense word you see below:\n\n<h1><center>zulx</center></h1>', 
												'Speak the nonsense word you see below:\n\n<h1><center>vave</center></h1>', 
												'Speak the nonsense word you see below:\n\n<h1><center>kwaj</center></h1>', 
												'Speak the nonsense word you see below:\n\n<h1><center>jome</center></h1>', 
												'Speak the nonsense word you see below:\n\n<h1><center>bwiz</center></h1>', 
												'Speak the nonsense word you see below:\n\n<h1><center>broe</center></h1>', 
												'Speak the nonsense word you see below:\n\n<h1><center>nayb</center></h1>', 

												'Please listen carefully to the following audio clip once.\n\n[autoplay](https://s3.amazonaws.com/www.voiceome.org/data/mandog.mp3)', 
												'Please repeat back what you just heard as accurately as possible. You may press the stop button if you finish before the timer runs out.', 
												'Please listen carefully to the following audio clip once.\n\n[autoplay](https://s3.amazonaws.com/www.voiceome.org/data/tourbus.mp3)', 
												'Please repeat back what you just heard as accurately as possible. You may press the stop button if you finish before the timer runs out..1', 

												'Please state any chronic or active medical conditions for which you are treated by a healthcare professional. For example, one might say “high blood pressure” or “depression.” When ready to respond, please click below to record your response. When finished, feel free to stop the recording to advance to the next slide.', 
												'Please list the names of all prescription medications or daily supplements which you are actively taking. When ready to respond, please click below to record your response. When finished, feel free to stop the recording to advance to the next slide.']

				confounds=['Do you currently smoke tobacco or any other substance on a regular basis (daily or weekly)?', 
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
								'How many hours were you asleep last night?']

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

				demographic=['With which gender do you most identify? ', 
										 'What is your age in years? (e.g. 25).', 
										 'What is your highest level of education?', 
										 'What is your current employment status? ', 
										 'What is your marital status?', 
										 'What is your total household income?', 
										 'What is your fluency with the English language?', 
										 "What is your height? (e.g. 5'10'').", 'What is your weight in pounds? (e.g. 150 lbs).', 
										 'Do you have a cold today? Note that some symptoms of a cold include having a sore throat, runny nose, cough, congestion, and/or sinus pressure.', 
										 'How would you best describe yourself? Select all options that apply.']

				covid=['The following questions will help us further assess whether or not you are experiencing COVID-19 related symptoms. Please answer these questions to the best of your ability.\n\n---\n\nHave you ever been tested for COVID-19?', 
										 'If you have been tested for COVID-19, when was your test performed?', 
										 'Do you have a fever or feel too hot?', 
										 'Do you feel chills or shivers (feel too cold)?', 
										 'Do you have a persistent cough (coughing a lot for more than an hour, or 3 or more coughing episodes in 24 hours)?', 
										 'Are you experiencing unusual fatigue?', 
										 'Are you experiencing unusual shortness of breath or have trouble breathing?', 
										 'Do you have a sore or painful throat?', 
										 'Do you have loss of smell / taste?', 
										 'Do you have an unusually hoarse voice?', 
										 'Are you feeling an unusual chest pain or tightness in your chest?', 
										 'Have you been skipping meals?']

				phq9=['**Over the last 2 weeks, how often have you been\nbothered by any of the following problems?**\n\n---\n\nLittle interest or pleasure in doing things', 
							' Feeling down, depressed, or hopeless', 
							'Trouble falling or staying asleep, or sleeping too much', 
							'Feeling tired or having little energy', 
							'Poor appetite or overeating', 
							'Feeling bad about yourself or that you are a failure or have let yourself or your family down', 
							'Trouble concentrating on things, such as reading the newspaper or watching television', 
							'Moving or speaking so slowly that other people could have noticed. Or the opposite being so figety or restless that you have been moving around a lot more than usual', 
							'Thoughts that you would be better off dead, or of hurting yourself']

				gad7=['**Over the last 2 weeks, how often have you been\nbothered by the following problems?**\n\n---\n\nFeeling nervous, anxious, or on edge', 
							'Not being able to stop or control worrying ', 
							'Worrying too much about different things', 
							'Trouble relaxing ', 
							"Being so restless that it's hard to sit still ", 
							'Becoming easily annoyed or irritable ', 
							'Feeling afraid as if something awful might happen']

				altman=['**There are 5 statement groups on this questionnaire: read each group of statements carefully. Choose one statement in each group that best describes the way you have been feeling the past week.**\n\nPlease note: the word "occasionally" when used here means once or twice; "often" means several times or more and "frequently" means most of the time.\n\n---\n\nStatement 1', 
								'Statement 2 ', 
								'Statement 3', 
								'Statement 4', 
								'Statement 5'] 

				auditc=['How often do you have a drink containing alcohol?', 
								'How many standard drinks containing alcohol do you have on a typical day?', 
								'How often do you have six or more drinks on one occasion?'] 

				sheehan=['The next few questions assess how any disability or disorder you have impairs your daily functioning. If you have no disabilities, you may answer 0 to all of these questions.\n\n---\n\n**Work / school responsibilities**\n\nThe symptoms from my disability or disorder have disrupted my job responsibilities or school work (0 - not at all to 10 - extremely):\n\n![](https://s3.amazonaws.com/www.voiceome.org/data/Screen+Shot+2020-03-12+at+1.21.28+AM.png)', 
										 '**Social life / leisure activities**\n\nThe symptoms from my disability or disorder have disrupted my social life / leisure activities (0 - not at all to 10 - extremely):\n\n![](https://s3.amazonaws.com/www.voiceome.org/data/Screen+Shot+2020-03-12+at+1.21.28+AM.png)', 
										 '**Family life / home responsibilities**\n\nThe symptoms from my disability or disorder have disrupted my family life / home responsibilities (0 - not at all to 10 - extremely):\n\n![](https://s3.amazonaws.com/www.voiceome.org/data/Screen+Shot+2020-03-12+at+1.21.28+AM.png)']

				adhd=['**Please answer the questions below, rating yourself on each of the criteria shown using the scale on the right side of the page. As you answer each question, pick the answer that best describes how you have felt and conducted yourself over the past 6 months.**\n\n---\n\nHow often do you have trouble wrapping up the final details of a project, once the challenging parts have been done?', 
								'How often do you have difficulty getting things in order when you have to do a task that requires organization?', 
								'How often do you have problems remembering appointments or obligations?', 
								'When you have a task that requires a lot of thought, how often do you avoid or delay getting started?  ', 
								'How often do you fidget or squirm with your hands or feet when you have to sit down for a long time?  ', 
								'How often do you feel overly active and compelled to do things, like you were driven by a motor?'] 

				insomnia=['**In thinking about your sleep patterns throughout the past 2 WEEKS, please respond to the following questions.**\n\n---\n\nDifficulty falling asleep', 
									'Difficulty staying asleep', 
									'Problems waking up too early', 
									'How SATISFIED/DISSATISFIED are you with your CURRENT sleep pattern?', 
									'How NOTICEABLE to others do you think your sleep problem is in terms of impairing the quality of your life?', 
									'How WORRIED/DISTRESSED are you about your current sleep problem?', 
									'To what extent do you consider your sleep problem to INTERFERE with your daily functioning (e.g. daytime fatigue, mood, ability to function at work/daily chores, concentration, memory, mood, etc.) CURRENTLY?']

				ptsd=['**Sometimes things happen to people that are unusually or especially frightening, horrible, or traumatic. For example: a serious accident or fire, a physical or sexual assault or abuse, an earthquake or flood, a war, seeing someone be killed or seriously injured, or having a loved one die through homicide or suicide.**\n\n---\n\nHave you ever experienced this kind of event?'] 

				stanford=['The Stanford Sleepiness Scale is comprised of a rating from 1 to 7 as described below. Please select the rating which best describes your current state.']

				return start_columns, audio_questions, confounds, scales, demographic, covid, phq9, gad7, altman, auditc, sheehan, adhd, insomnia, ptsd, stanford 

		def extract_numbers(string_):
				# print(string_)
				try:
						number_=re.findall("\d+",string_)[0][0]
						return int(number_)
				except:
						return int(string_)

		def unique_mapping(column_data):
				'''
				Convert a unique list of strings into numerical values.
				'''

				# convert to list 
				column_data=list(column_data)

				# calculate unique values / sort to keep deterministic at scale
				unique_values=list(set(list(column_data)))
				unique_values.sort()

				new_values=list()
				for i in range(len(unique_values)):
						new_values.append(i)

				mapping_=dict(zip(unique_values, new_values))

				new_column=list()

				for i in range(len(column_data)):
						new_column.append(mapping_[column_data[i]])

				return new_column

		def make_numerical(column_data):
				column_data=list(column_data)
				new_column=list()
				for i in range(len(column_data)):
						new_column.append(extract_numbers(column_data[i]))
				return new_column

		def clean_confounds(data, columns):
				'''
				converts all the confounding variables logged into 
				integer values.

				confounds=['Do you currently smoke tobacco or any other substance on a regular basis (daily or weekly)?', 
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
										'How many hours were you asleep last night?']

				'''
				# iterate through all columns here to get values
				for i in range(len(columns)):
						column=data[columns[i]]
						new_column=unique_mapping(column)
						data[columns[i]]=new_column

				return data

		def clean_scales(data, columns):
				'''
				converts all the static scales to integer values.

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

				'''
				# iterate through all columns here to get values
				for i in range(len(columns)):
						column=data[columns[i]]
						new_column=make_numerical(column)
						data[columns[i]]=new_column

				return data

		def clean_demographics(data, columns):
				'''
				cleans demographic scale values to integers,
				and sums them up in a new column.

				demographic=['With which gender do you most identify? ', 
										 'What is your age in years? (e.g. 25).', 
										 'What is your highest level of education?', 
										 'What is your current employment status? ', 
										 'What is your marital status?', 
										 'What is your total household income?', 
										 'What is your fluency with the English language?', 
										 "What is your height? (e.g. 5'10'').", 
										 'What is your weight in pounds? (e.g. 150 lbs).', 
										 'Do you have a cold today? Note that some symptoms of a cold include having a sore throat, runny nose, cough, congestion, and/or sinus pressure.', 
										 'How would you best describe yourself? Select all options that apply.']
				'''
				def reformat_heights(height_array):
						new_heights=list()
						height_array=list(height_array)
						for i in range(len(height_array)):
								# is a number 
								height=0
								skip=False
								for j in range(len(height_array[i])):
										if height_array[i][j] in ['0','1','2','3','4','5','6','7','8','9'] and skip==False:
												height = 12*int(height_array[i][j])
												skip=True 
										elif height_array[i][j] in ['0','1','2','3','4','5','6','7','8','9']:
												if height_array[i:i+1] in ['10','11']:
														height=height+int(height_array[i][j:j+1])
												else:
														height=height+int(height_array[i][j])
								new_heights.append(height)
						return new_heights

				def reformat_weight(weight_array):
						new_weights=list()
						for i in range(len(weight_array)):
								new_weights.append(int(weight_array[i].split(' ')[0]))
						return new_weights

				for i in range(len(columns)):
						if columns[i] == "What is your height? (e.g. 5'10'').":
								new_column=reformat_heights(data[columns[i]])
						elif columns[i] == 'What is your weight in pounds? (e.g. 150 lbs).':
								new_column=reformat_weight(data[columns[i]])
						elif columns[i] == 'What is your age in years? (e.g. 25).':
								new_column=make_numerical(data[columns[i]])
						else:
								new_column=unique_mapping(data[columns[i]])

						data[columns[i]]=new_column

				return data

		def clean_covid(data, columns):
				'''
				cleans COVID-19 scale values to integers,
				and sums them up in a new column.

				covid=['The following questions will help us further assess whether or not you are experiencing COVID-19 related symptoms. Please answer these questions to the best of your ability.\n\n---\n\nHave you ever been tested for COVID-19?', 
										 'If you have been tested for COVID-19, when was your test performed?', 
										 'Do you have a fever or feel too hot?', 
										 'Do you feel chills or shivers (feel too cold)?', 
										 'Do you have a persistent cough (coughing a lot for more than an hour, or 3 or more coughing episodes in 24 hours)?', 
										 'Are you experiencing unusual fatigue?', 
										 'Are you experiencing unusual shortness of breath or have trouble breathing?', 
										 'Do you have a sore or painful throat?', 
										 'Do you have loss of smell / taste?', 
										 'Do you have an unusually hoarse voice?', 
										 'Are you feeling an unusual chest pain or tightness in your chest?', 
										 'Have you been skipping meals?']
				'''
				def not_covid_cols(data):
						columns=list(data)
						covid=['The following questions will help us further assess whether or not you are experiencing COVID-19 related symptoms. Please answer these questions to the best of your ability.\n\n---\n\nHave you ever been tested for COVID-19?', 
												 'If you have been tested for COVID-19, when was your test performed?', 
												 'Do you have a fever or feel too hot?', 
												 'Do you feel chills or shivers (feel too cold)?', 
												 'Do you have a persistent cough (coughing a lot for more than an hour, or 3 or more coughing episodes in 24 hours)?', 
												 'Are you experiencing unusual fatigue?', 
												 'Are you experiencing unusual shortness of breath or have trouble breathing?', 
												 'Do you have a sore or painful throat?', 
												 'Do you have loss of smell / taste?', 
												 'Do you have an unusually hoarse voice?', 
												 'Are you feeling an unusual chest pain or tightness in your chest?', 
												 'Have you been skipping meals?']
						drop_cols=list()
						for i in range(len(columns)):
								if columns[i] not in covid:
										drop_cols.append(columns[i])
						return drop_cols

				def get_covid_scores(data):
						# print(data)
						scores=list()
						labels=list(data)
						# print(labels)
						for i in range(len(data)):
								value=0
								data_=data.iloc[i,:]
								for j in range(len(data_)):
										temp_value=data_[j]
										value=value+temp_value 
								scores.append(value)
						return scores

				# calculate unique numerical values
				for i in range(len(columns)):
						new_column=unique_mapping(data[columns[i]])
						data[columns[i]]=new_column

				# now sum these values 
				notcovid=not_covid_cols(data)
				covid_data=data.drop(columns=notcovid)
				covid_scores=get_covid_scores(covid_data)
				data['c19_scores']=covid_scores

				return data

		def clean_phq9(data, columns):
				'''
				cleans PHQ-9 scale values to integers,
				and sums them up in a new column.

				phq9=['**Over the last 2 weeks, how often have you been\nbothered by any of the following problems?**\n\n---\n\nLittle interest or pleasure in doing things', 
							' Feeling down, depressed, or hopeless', 
							'Trouble falling or staying asleep, or sleeping too much', 
							'Feeling tired or having little energy', 
							'Poor appetite or overeating', 
							'Feeling bad about yourself or that you are a failure or have let yourself or your family down', 
							'Trouble concentrating on things, such as reading the newspaper or watching television', 
							'Moving or speaking so slowly that other people could have noticed. Or the opposite being so figety or restless that you have been moving around a lot more than usual', 
							'Thoughts that you would be better off dead, or of hurting yourself']
				'''
				def get_phq9_score(data):
						# print(data)
						scores=list()
						labels=list(data)
						# print(labels)
						for i in range(len(data)):
								value=0
								data_=data.iloc[i,:]
								for j in range(len(data_)):
										temp_value=extract_numbers(data_[j])
										value=value+temp_value 
								scores.append(value)
						return scores
				
				def not_phq9_cols(data):
						columns=list(data)
						phq9=['**Over the last 2 weeks, how often have you been\nbothered by any of the following problems?**\n\n---\n\nLittle interest or pleasure in doing things', 
							' Feeling down, depressed, or hopeless', 
							'Trouble falling or staying asleep, or sleeping too much', 
							'Feeling tired or having little energy', 
							'Poor appetite or overeating', 
							'Feeling bad about yourself or that you are a failure or have let yourself or your family down', 
							'Trouble concentrating on things, such as reading the newspaper or watching television', 
							'Moving or speaking so slowly that other people could have noticed. Or the opposite being so figety or restless that you have been moving around a lot more than usual', 
							'Thoughts that you would be better off dead, or of hurting yourself']
						drop_cols=list()
						for i in range(len(columns)):
								if columns[i] not in phq9:
										drop_cols.append(columns[i])
						return drop_cols
				
				# calculate unique numerical values
				for i in range(len(columns)):
						new_column=make_numerical(data[columns[i]])
						data[columns[i]]=new_column

				# make a new columns on net phq9
				notphq9=not_phq9_cols(data)
				phq_data=data.drop(columns=notphq9)
				phq9_scores=get_phq9_score(phq_data)
				data['phq9'] = phq9_scores

				return data

		def clean_gad7(data, columns):
				'''
				cleans GAD-7 scale values to integers,
				and sums them up in a new column.

				gad7=['**Over the last 2 weeks, how often have you been\nbothered by the following problems?**\n\n---\n\nFeeling nervous, anxious, or on edge', 
							'Not being able to stop or control worrying ', 
							'Worrying too much about different things', 
							'Trouble relaxing ', 
							"Being so restless that it's hard to sit still ", 
							'Becoming easily annoyed or irritable ', 
							'Feeling afraid as if something awful might happen']
				'''

				def get_gad7_score(data):
						# print(data)
						scores=list()
						labels=list(data)
						# print(labels)
						for i in range(len(data)):
								value=0
								data_=data.iloc[i,:]
								for j in range(len(data_)):
										temp_value=extract_numbers(data_[j])
										value=value+temp_value 
								scores.append(value)
						return scores
				
				def not_gad7_cols(data):
						columns=list(data)
						gad7=['**Over the last 2 weeks, how often have you been\nbothered by the following problems?**\n\n---\n\nFeeling nervous, anxious, or on edge', 
									'Not being able to stop or control worrying ', 
									'Worrying too much about different things', 
									'Trouble relaxing ', 
									"Being so restless that it's hard to sit still ", 
									'Becoming easily annoyed or irritable ', 
									'Feeling afraid as if something awful might happen']
						drop_cols=list()
						for i in range(len(columns)):
								if columns[i] not in gad7:
										drop_cols.append(columns[i])
						return drop_cols
				
				# calculate unique numerical values
				for i in range(len(columns)):
						new_column=make_numerical(data[columns[i]])
						data[columns[i]]=new_column

				# make a new columns on net phq9
				notgad7=not_gad7_cols(data)
				gad_data=data.drop(columns=notgad7)
				gad7_scores=get_gad7_score(gad_data)
				data['gad7'] = gad7_scores

				return data

		def clean_altman(data, columns):
				'''
				cleans Altman self-rating scale scale values to integers,
				and sums them up in a new column.

				altman=['**There are 5 statement groups on this questionnaire: read each group of statements carefully. Choose one statement in each group that best describes the way you have been feeling the past week.**\n\nPlease note: the word "occasionally" when used here means once or twice; "often" means several times or more and "frequently" means most of the time.\n\n---\n\nStatement 1', 
								'Statement 2 ', 
								'Statement 3', 
								'Statement 4', 
								'Statement 5'] 
				'''
				def get_altman_score(data):
						# print(data)
						scores=list()
						labels=list(data)
						# print(labels)
						for i in range(len(data)):
								value=0
								data_=data.iloc[i,:]
								for j in range(len(data_)):
										temp_value=data_[j]
										value=value+temp_value 
								scores.append(value)
						return scores

				def not_altman_cols(data):
						columns=list(data)
						altman=['**There are 5 statement groups on this questionnaire: read each group of statements carefully. Choose one statement in each group that best describes the way you have been feeling the past week.**\n\nPlease note: the word "occasionally" when used here means once or twice; "often" means several times or more and "frequently" means most of the time.\n\n---\n\nStatement 1', 
										'Statement 2 ', 
										'Statement 3', 
										'Statement 4', 
										'Statement 5'] 
						drop_cols=list()
						for i in range(len(columns)):
								if columns[i] not in altman:
										drop_cols.append(columns[i])
						return drop_cols

				# calculate unique numerical values
				for i in range(len(columns)):
						new_column=make_numerical(data[columns[i]])
						data[columns[i]]=new_column

				# now sum all the columns 
				notaltman=not_altman_cols(data)
				altman_data=data.drop(columns=notaltman)
				altman_scores=get_altman_score(altman_data)
				data['altman_selfrating'] = altman_scores

				return data

		def clean_auditc(data, columns):
				'''
				cleans AUDIT-C scale values to integers,
				and sums them up in a new column.

				auditc=['How often do you have a drink containing alcohol?', 
								'How many standard drinks containing alcohol do you have on a typical day?', 
								'How often do you have six or more drinks on one occasion?'] 
				'''
				# calculate unique numerical values
				for i in range(len(columns)):
						new_column=unique_mapping(data[columns[i]])
						data[columns[i]]=new_column

				return data

		def clean_sheehan(data, columns):
				'''
				cleans sheehan disability scale values to integers,
				and sums them up in a new column.

			 sheehan=['The next few questions assess how any disability or disorder you have impairs your daily functioning. If you have no disabilities, you may answer 0 to all of these questions.\n\n---\n\n**Work / school responsibilities**\n\nThe symptoms from my disability or disorder have disrupted my job responsibilities or school work (0 - not at all to 10 - extremely):\n\n![](https://s3.amazonaws.com/www.voiceome.org/data/Screen+Shot+2020-03-12+at+1.21.28+AM.png)', 
								'**Social life / leisure activities**\n\nThe symptoms from my disability or disorder have disrupted my social life / leisure activities (0 - not at all to 10 - extremely):\n\n![](https://s3.amazonaws.com/www.voiceome.org/data/Screen+Shot+2020-03-12+at+1.21.28+AM.png)', 
								'**Family life / home responsibilities**\n\nThe symptoms from my disability or disorder have disrupted my family life / home responsibilities (0 - not at all to 10 - extremely):\n\n![](https://s3.amazonaws.com/www.voiceome.org/data/Screen+Shot+2020-03-12+at+1.21.28+AM.png)']

				'''
				# sum the scores
				def get_sheehan_score(data):
								scores=list()
								labels=list(data)
								# print(labels)
								for i in range(len(data)):
										value=0
										data_=data.iloc[i,:]
										for j in range(len(data_)):
												temp_value=data_[j]
												value=value+temp_value 
										scores.append(value)
								return scores

				def not_sheehan_cols(data):
						columns=list(data)
						sheehan=['The next few questions assess how any disability or disorder you have impairs your daily functioning. If you have no disabilities, you may answer 0 to all of these questions.\n\n---\n\n**Work / school responsibilities**\n\nThe symptoms from my disability or disorder have disrupted my job responsibilities or school work (0 - not at all to 10 - extremely):\n\n![](https://s3.amazonaws.com/www.voiceome.org/data/Screen+Shot+2020-03-12+at+1.21.28+AM.png)', 
										 '**Social life / leisure activities**\n\nThe symptoms from my disability or disorder have disrupted my social life / leisure activities (0 - not at all to 10 - extremely):\n\n![](https://s3.amazonaws.com/www.voiceome.org/data/Screen+Shot+2020-03-12+at+1.21.28+AM.png)', 
											'**Family life / home responsibilities**\n\nThe symptoms from my disability or disorder have disrupted my family life / home responsibilities (0 - not at all to 10 - extremely):\n\n![](https://s3.amazonaws.com/www.voiceome.org/data/Screen+Shot+2020-03-12+at+1.21.28+AM.png)']
						drop_cols=list()
						for i in range(len(columns)):
								if columns[i] not in sheehan:
										drop_cols.append(columns[i])
						return drop_cols

				# calculate unique numerical values
				for i in range(len(columns)):
						new_column=make_numerical(data[columns[i]])
						data[columns[i]]=new_column

				# add a summed column
				notsheehan=not_sheehan_cols(data)
				sheehan_data=data.drop(columns=notsheehan)
				sheehan_scores=get_sheehan_score(sheehan_data)
				data['sheehan_disability_rating'] = sheehan_scores

				return data

		def clean_adhd(data, columns):
				'''
				cleans adhd self-rating scale values to integers,
				and sums them up in a new column.

				adhd=['**Please answer the questions below, rating yourself on each of the criteria shown using the scale on the right side of the page. As you answer each question, pick the answer that best describes how you have felt and conducted yourself over the past 6 months.**\n\n---\n\nHow often do you have trouble wrapping up the final details of a project, once the challenging parts have been done?', 
								'How often do you have difficulty getting things in order when you have to do a task that requires organization?', 
								'How often do you have problems remembering appointments or obligations?', 
								'When you have a task that requires a lot of thought, how often do you avoid or delay getting started?  ', 
								'How often do you fidget or squirm with your hands or feet when you have to sit down for a long time?  ', 
								'How often do you feel overly active and compelled to do things, like you were driven by a motor?'] 
				'''
				def get_adhd_score(data):
								# print(data)
								scores=list()
								labels=list(data)
								# print(labels)
								for i in range(len(data)):
										value=0
										data_=data.iloc[i,:]
										for j in range(len(data_)):
												temp_value=data_[j]
												value=value+temp_value 
										scores.append(value)
								return scores

				def not_adhd_cols(data):
						columns=list(data)
						adhd=['**Please answer the questions below, rating yourself on each of the criteria shown using the scale on the right side of the page. As you answer each question, pick the answer that best describes how you have felt and conducted yourself over the past 6 months.**\n\n---\n\nHow often do you have trouble wrapping up the final details of a project, once the challenging parts have been done?', 
										'How often do you have difficulty getting things in order when you have to do a task that requires organization?', 
										'How often do you have problems remembering appointments or obligations?', 
										'When you have a task that requires a lot of thought, how often do you avoid or delay getting started?  ', 
										'How often do you fidget or squirm with your hands or feet when you have to sit down for a long time?  ', 
										'How often do you feel overly active and compelled to do things, like you were driven by a motor?'] 
						drop_cols=list()
						for i in range(len(columns)):
								if columns[i] not in adhd:
										drop_cols.append(columns[i])
						return drop_cols

				def make_adhd_numerical(column):
						new_columns=list()

						for j in range(len(column)):
								if column[j].find('Never') >= 0:
										new_columns.append(0)
								elif column[j].find('Rarely') >= 0:
										new_columns.append(1)
								elif column[j].find('Sometimes') >= 0:
										new_columns.append(2)
								elif column[j].find('Often') >= 0:
										new_columns.append(3)
								elif column[j].find('Very Often') >= 0:
										new_columns.append(4)

						return new_columns

				# calculate unique numerical values
				for i in range(len(columns)):
						new_column=make_adhd_numerical(data[columns[i]])
						data[columns[i]]=new_column

				# add a summed column
				notadhd=not_adhd_cols(data)
				adhd_data=data.drop(columns=notadhd)
				adhd_scores=get_adhd_score(adhd_data)
				data['adhd_selfrating'] = adhd_scores

				return data

		def clean_insomnia(data, columns):
				'''
				cleans insomnia index score values to integers,
				and sums them up in a new column.

				insomnia=['**In thinking about your sleep patterns throughout the past 2 WEEKS, please respond to the following questions.**\n\n---\n\nDifficulty falling asleep', 
									'Difficulty staying asleep', 
									'Problems waking up too early', 
									'How SATISFIED/DISSATISFIED are you with your CURRENT sleep pattern?', 
									'How NOTICEABLE to others do you think your sleep problem is in terms of impairing the quality of your life?', 
									'How WORRIED/DISTRESSED are you about your current sleep problem?', 
									'To what extent do you consider your sleep problem to INTERFERE with your daily functioning (e.g. daytime fatigue, mood, ability to function at work/daily chores, concentration, memory, mood, etc.) CURRENTLY?']
				'''

				def get_insomnia_score(data):
								# print(data)
								scores=list()
								labels=list(data)
								# print(labels)
								for i in range(len(data)):
										value=0
										data_=data.iloc[i,:]
										for j in range(len(data_)):
												temp_value=data_[j]
												value=value+temp_value 
										scores.append(value)
								return scores

				def not_insomnia_cols(data):
						columns=list(data)
						insomnia=['**In thinking about your sleep patterns throughout the past 2 WEEKS, please respond to the following questions.**\n\n---\n\nDifficulty falling asleep', 
											'Difficulty staying asleep', 
											'Problems waking up too early', 
											'How SATISFIED/DISSATISFIED are you with your CURRENT sleep pattern?', 
											'How NOTICEABLE to others do you think your sleep problem is in terms of impairing the quality of your life?', 
											'How WORRIED/DISTRESSED are you about your current sleep problem?', 
											'To what extent do you consider your sleep problem to INTERFERE with your daily functioning (e.g. daytime fatigue, mood, ability to function at work/daily chores, concentration, memory, mood, etc.) CURRENTLY?']
						drop_cols=list()
						for i in range(len(columns)):
								if columns[i] not in insomnia:
										drop_cols.append(columns[i])
						return drop_cols

				# calculate unique numerical values
				for i in range(len(columns)):
						new_column=make_numerical(data[columns[i]])
						data[columns[i]]=new_column

				# add a summed column
				notinsomnia=not_insomnia_cols(data)
				insomnia_data=data.drop(columns=notinsomnia)
				insomnia_scores=get_insomnia_score(insomnia_data)
				data['insomnia_severity_index'] = insomnia_scores

				return data

		def clean_ptsd(data, columns):
				'''
				cleans ptsd score value so that it becomes an 
				integer as opposed to string. 
				
				ptsd=['**Sometimes things happen to people that are unusually or especially frightening, horrible, or traumatic. For example: a serious accident or fire, a physical or sexual assault or abuse, an earthquake or flood, a war, seeing someone be killed or seriously injured, or having a loved one die through homicide or suicide.**\n\n---\n\nHave you ever experienced this kind of event?']    
				'''
				# calculate unique numerical values
				for i in range(len(columns)):
						new_column=unique_mapping(data[columns[i]])
						data[columns[i]]=new_column

				return data

		def clean_stanford(data, columns):
				'''
				cleans the stanford sleepiness scale value 
				so that it becomes an integer as opposed to 
				string.

				stanford=['The Stanford Sleepiness Scale is comprised of a rating from 1 to 7 as described below. Please select the rating which best describes your current state.']
				'''
				# calculate unique numerical values
				for i in range(len(columns)):
						new_column=make_numerical(data[columns[i]])
						data[columns[i]]=new_column

				return data

		def calculate_bmi(data):
				'''
				Calculates a simple body mass measurement using 
				height and weight measurments. Assumes that height 
				has been corrected to cm and weight corrected to lbs
				as integer values.

				# Formula: weight (lb) / [height (in)]2 x 703
				https://www.cdc.gov/nccdphp/dnpao/growthcharts/training/bmiage/page5_2.html
				'''

				# these should already be formatted properly
				weight=list(data["What is your weight in pounds? (e.g. 150 lbs)."])
				height=list(data["What is your height? (e.g. 5'10'')."])

				bmis=list()
				for i in range(len(weight)):
						bmi=(weight[i] / height[i] / height[i])*703
						bmis.append(bmi)

				data['bmis']=bmis
				return data

		def calculate_ages(data):
				'''
				Reformat ages to align with the common voice project (Mozilla firefox).
				This assumes all ages have been cleaned to be integer values.
				'''
				ages=list(data['What is your age in years? (e.g. 25).'])
				new_ages=list()

				if len(ages) == 1:
						i=0
						if ages[i] > 17 and ages[i] < 20:
								new_ages.append('teens')
						elif ages[i] >= 20 and ages[i] < 30:
								new_ages.append('twenties')
						elif ages[i] >= 30 and ages[i] < 40:
								new_ages.append('thirties')
						elif ages[i] >= 40 and ages[i] < 50:
								new_ages.append('fourties')
						elif ages[i] >= 50 and ages[i] < 60:
								new_ages.append('fifties')
						elif ages[i] >= 60:
								new_ages.append('sixties')
				else:

						for i in range(len(ages)):
								if ages[i] > 17 and ages[i] < 20:
										new_ages.append('teens')
								elif ages[i] >= 20 and ages[i] < 30:
										new_ages.append('twenties')
								elif ages[i] >= 30 and ages[i] < 40:
										new_ages.append('thirties')
								elif ages[i] >= 40 and ages[i] < 50:
										new_ages.append('fourties')
								elif ages[i] >= 50 and ages[i] < 60:
										new_ages.append('fifties')
								elif ages[i] >= 60:
										new_ages.append('sixties')

				data['commonvoice_ages'] = new_ages

				return data
				
		start_column, audio_questions, confounds, scales, demographic, covid, phq9, gad7, altman, auditc, sheehan, adhd, insomnia, ptsd, stanford = categorize_csv(csvfile)

		data=pd.read_csv(csvfile)

		# clean the data down a pipeline 
		data=clean_confounds(data, confounds)
		data=clean_scales(data, scales)
		data=clean_demographics(data, demographic)
		data=clean_covid(data, covid)
		data=clean_phq9(data, phq9)
		data=clean_gad7(data, gad7)
		data=clean_altman(data, altman)
		data=clean_auditc(data, auditc)
		data=clean_sheehan(data, sheehan)
		data=clean_adhd(data, adhd)
		data=clean_insomnia(data, insomnia)
		data=clean_ptsd(data, ptsd)
		data=clean_stanford(data, stanford)

		# some additional data manipulations
		data=calculate_bmi(data)
		data=calculate_ages(data)

		return data

data=clean_csv('data.csv')
data.to_csv('clean.csv', index=False)