# voiceome
The Voiceome is the largest clinical study in the world to collect voice data labeled with health information. More info @ https://www.voiceome.org/ and [the wiki](https://github.com/jim-schwoebel/voiceome/wiki).

## background
Why we created this study. 

## scripts
Here are list of scripts used to generate figures in the paper, so our work can be reproduced.
### data cleaning
Cleaning voice data from spreadsheets (table)

| Script     |    Description   |   Utility |
| ----------- | ----------- | ----------- |
| test | test | test |

### featurization
We built some featurization scripts for figures in paper (table).

| Script     |    Description   |   Utility |
| ----------- | ----------- | ----------- |
| test | test | test |


### generating references 
Age/gender-matched controls.

| Script     |    Description   |   Utility |
| ----------- | ----------- | ----------- |
| test | test | test |


### visualization
Visualization scripts (table).

| Script     |    Description   |   Utility |
| ----------- | ----------- | ----------- |
| test | test | test |

## references 
To load the reference data from Survey A, you can call a python script (load_references.py):

```
git clone git@github.com:jim-schwoebel/voiceome.git
cd voiceome
pip3 install -r requirements.txt
```

You now can load the python script to call the protocol (.TXT) and references:
```
import .scripts.references

## protocols 
Protocol URLs
A-https://app.surveylex.com/surveys/e1f88ee0-a636-11eb-bcc9-eba67643f616
B-https://app.surveylex.com/surveys/061da3f0-a637-11eb-bcc9-eba67643f616
C-https://app.surveylex.com/surveys/a66494c0-a824-11ea-88c1-ab37bac1e1d4
D-https://app.surveylex.com/surveys/53737620-a637-11eb-bcc9-eba67643f616

## question text 
0. Consent form
-- get SurveyLex text 
00. Microphone check task
-- get SurveyLex text 
01. Free speech task
-- get SurveyLex text
02. Picture description task
-- get SurveyLex text
03. Category naming task
-- get SurveyLex text
04. Letter {FAS} Tasks
-- get SurveyLex text
05. Paragraph reading task
-- get SurveyLex text
06. Sustained phonation ('ahh')
-- get SurveyLex text
07. Pa pa pa task
-- get SurveyLex text
08. Pa ta ka task
-- get SurveyLex text
09. Confrontational naming task
-- get SurveyLex text
10. Nonword task
-- get SurveyLex text
11. Immediate recall task
-- get SurveyLex text
12. Spoken diagnosis task
-- get SurveyLex text
13. Spoken medication task
-- get SurveyLex text
14. Confounding questions
-- get SurveyLex text
15. Demographic questions
-- get SurveyLex text
16. Health labels
-- get SurveyLex text
17. Fun Facts
-- get SurveyLex text

## featurizers 

Take in audio and get back feature embeddings / quality checks for each task per the paper implementations.

00. Microphone check task
-- .JSON
01. Free speech task
-- .JSON
02. Picture description task
-- .JSON
03. Category naming task
-- .JSON
04. Letter {FAS} Tasks
-- .JSON
05. Paragraph reading task
-- .JSON
06. Sustained phonation ('ahh')
-- .JSON
07. Pa pa pa task
-- .JSON
08. Pa ta ka task
-- .JSON
09. Confrontational naming task
-- .JSON
10. Nonword task
-- .JSON
11. Immediate recall task
-- .JSON
12. Spoken diagnosis task
-- .JSON
13. Spoken medication task
-- .JSON

## references 
Types of features include Acoustic (OPENSMILE GeMAPS + Prosody_Features) and Linguistic (Features in Allie here)

00. Microphone check task
-- .JSON
01. Free speech task
-- .JSON
02. Picture description task
-- .JSON
03. Category naming task
-- .JSON
04. Letter {FAS} Tasks
-- .JSON
05. Paragraph reading task
-- .JSON
06. Sustained phonation ('ahh')
-- .JSON
07. Pa pa pa task
-- .JSON
08. Pa ta ka task
-- .JSON
09. Confrontational naming task
-- .JSON
10. Nonword task
-- .JSON
11. Immediate recall task
-- .JSON
12. Spoken diagnosis task
-- .JSON
13. Spoken medication task
-- .JSON
14. Confounding questions
-- .JSON
15. Demographic questions
-- .JSON
16. Health labels
-- .JSON
17. Fun Facts
-- .JSON
```

## surveys 
Here are the 4 main surveys used in the Voiceome clinical study:

| Survey     |    Link    |   Number of completions |
| ----------- | ----------- | ----------- |
| Survey A      | [https://app.surveylex.com/surveys/e1f88ee0-a636-11eb-bcc9-eba67643f616](https://app.surveylex.com/surveys/e1f88ee0-a636-11eb-bcc9-eba67643f616)      | Title       |
| Survey B  | [https://app.surveylex.com/surveys/061da3f0-a637-11eb-bcc9-eba67643f616](https://app.surveylex.com/surveys/061da3f0-a637-11eb-bcc9-eba67643f616) | 1400 |
| Survey C | [https://app.surveylex.com/surveys/a66494c0-a824-11ea-88c1-ab37bac1e1d4](https://app.surveylex.com/surveys/a66494c0-a824-11ea-88c1-ab37bac1e1d4) | 800 |
| Survey D | [https://app.surveylex.com/surveys/53737620-a637-11eb-bcc9-eba67643f616](https://app.surveylex.com/surveys/53737620-a637-11eb-bcc9-eba67643f616) | 100 |

Previews for each of these surveys are provided below as .GIFs so that you can quickly visualize the survey experience for clinical study participants.

Note you can clone these surveys @ https://surveylex.com and replicate our work in other patient populations.

### [Survey A](https://app.surveylex.com/surveys/e1f88ee0-a636-11eb-bcc9-eba67643f616)
![](https://github.com/jim-schwoebel/voiceome/blob/main/assets/images/A/A.gif)

### [Survey B](https://app.surveylex.com/surveys/061da3f0-a637-11eb-bcc9-eba67643f616)
![](https://github.com/jim-schwoebel/voiceome/blob/main/assets/images/B/B.gif)

### [Survey C](https://app.surveylex.com/surveys/a66494c0-a824-11ea-88c1-ab37bac1e1d4)
![](https://github.com/jim-schwoebel/voiceome/blob/main/assets/images/C/C.gif)

### [Survey D](https://app.surveylex.com/surveys/53737620-a637-11eb-bcc9-eba67643f616)
![](https://github.com/jim-schwoebel/voiceome/blob/main/assets/images/D/D.gif)

## Cite us!!
Feel free to cite or work using the format below:
```
Citation TBA
```

## Data access

Data is accessible via a commercial license. 

If you are interested to license or access the Voiceome dataset, please reach out to Jim Schwoebel (VP of Data and Research @ Sonde) @ jim.schwoebel@gmail.com.

## References
General references 
- [Allie ML repository](https://github.com/jim-schwoebel/allie)
- [Voicebook](https://github.com/jim-schwoebel/voicebook)
- [SurveyLex](https://surveylex.com)
- [OpenSmile GeMAPS](https://sail.usc.edu/publications/files/eyben-preprinttaffc-2015.pdf)

Protocols
- [00. Microphone check task]()
- [01. Free speech task]()
- [02. Picture description task]()
- [03. Category naming task]()
- [04. Letter {FAS} Tasks]()
- [05. Paragraph reading task]()
- [06. Sustained phonation ('ahh')]()
- [07. Pa pa pa task]()
- [08. Pa ta ka task]()
- [09. Confrontational naming task]()
- [10. Nonword task]()
- [11. Immediate recall task]()
- [12. Spoken diagnosis task]()
- [13. Spoken medication task]()

Health labels
- [PHQ-9](https://www.mdcalc.com/phq-9-patient-health-questionnaire-9)
- [GAD-7](https://patient.info/doctor/generalised-anxiety-disorder-assessment-gad-7)
- [Altman Self-rating scale](https://psychology-tools.com/test/altman-self-rating-mania-scale)
- [Audit-C](https://www.mdcalc.com/audit-c-alcohol-use)
- [Sheehan disability scale](http://memorialparkpsychiatry.com/doc/sheehan_disability_scale.pdf)
- [ADHD Self-rating Scale - Part A](https://psychology-tools.com/test/adult-adhd-self-report-scale)
- [Insomnia Severity Index](https://www.ons.org/sites/default/files/InsomniaSeverityIndex_ISI.pdf)
- [Stanford Sleepiness Scale](https://www.med.upenn.edu/cbti/assets/user-content/documents/Stanford%20Sleepiness%20Scale.pdf)
- [PTSD-5](https://www.ptsd.va.gov/professional/assessment/documents/pc-ptsd5-screen.pdf)

Synergistic datasets
- [Voice_datasets repo](https://github.com/jim-schwoebel/voice_datasets)
- [Coswara]()
- [mPower]()
