# voiceome
The [Voiceome Study](https://www.voiceome.org/) is the world’s largest clinical study to collect voice information labeled with health traits. The goal is to recruit between 10,000-100,000 patients into the study and track them at multiple time points to advance scientific understanding for vocal biomarkers and speed up the process for its commercialization.

[![](https://github.com/jim-schwoebel/voiceome/blob/main/assets/images/thumbnails/voiceome.png?raw=true)](https://www.youtube.com/watch?v=lCk_mffvJ0A&feature=emb_logo)

More information about the Voiceome study can be found @ [the wiki](https://github.com/jim-schwoebel/voiceome/wiki) and [website](https://voiceome.org).

## background/goals
One of the primary causes of slow translation of voice biomarker research is a result of small datasets. There have been many research studies that have shown that acoustic or linguistic voice features relate to health conditions like stress, schizophrenia, depression, bipolar disorder, stroke, and cardiovascular diseases. However, many of these studies have relatively small sample sizes (N<1,000 patients in each class), suffer from poor audio quality (e.g. use of different microphones and data collection techniques), and are difficult to access (e.g. large licensing fees to corporations and/or difficulty obtaining IRB access without close academic ties). These factors dramatically limit the ability to model the underlying data and correlate voice data to health traits, replicate peer-reviewed publications, as well as open up this work to the broader scientific community.

![](https://github.com/jim-schwoebel/voiceome/blob/main/assets/images/thumbnails/confounds.png?raw=true)

Therefore, the main goals of the Voiceome Study include:

- **Standardizing collection tools and features** - Standardize the tools and techniques used to collect and featurize voice samples for use in health-related research. <em> We have done this by building [SurveyLex](https://surveylex.com), a web-enabled survey tool for vocal biomarker research.</em>
- **Establishing reference ranges** - Create a standard set of normative ranges of [acoustic](https://github.com/jim-schwoebel/voiceome/tree/main/assets/references/A/acoustics) and [linguistic](https://github.com/jim-schwoebel/voiceome/tree/main/assets/references/A/linguistics) features across various ages, genders, microphone types, and dialects labeled with health information. <em>These are provided as [tables](https://github.com/jim-schwoebel/voiceome/tree/main/assets/references/A/acoustics) and scripts in this repository</em>.
- **Standardizing voice protocols** - Standardize the series of voice tasks used to collect speech samples for use in the voiceome. <em>These voice protocols can be found in the [wiki](https://github.com/jim-schwoebel/voiceome/wiki), and includes novel tasks like automated confrontational naming tasks and nonword tasks.</em>
- **Standardizing health trait labels** - Standardize the type of health trait labels tied to voice information to emit the most signal from the voice. <em>These are provided [here](https://github.com/jim-schwoebel/voiceome/wiki/16.-Health-labels#lichert-questions-custom-made).</em>
- **Creating machine learning models** - From Voiceome Study dataset, build and optimize novel machine learning models; to publish this work in academic journals openly. <em>These models will be published on in follow-on publications into the future.</em>
- **Creating an ethics framework** - Create a venue for legal, ethical, and security considerations for collecting voice data for health-related purposes. <em>This can be read in the [Voiceome strategic plan](https://drive.google.com/file/d/1Dme9tUq0eCepja_7Yg9sNqn_JWKaJxJm/view).</em>
- **Build a lasting community** - The Voiceome project will foster a lasting community and enthusiasm for the field of vocal biomarkers in general. <em>We do this through writing textbooks like [Voice Computing in Python](https://neurolex.ai/voicebook), collaborating with research organizations like the University of Washington and Biogen, and through training fellows through the [Innovation Fellows Program](http://neurolex.ai/research).</em>

## Clinical trial design
Anyone >18 years of age that could speak English was eligible to participate in the Voiceome Study (>6,000 participants completed the first survey). Each participant was randomly assigned one of three tracks (AAAA, ABAB, ABCD, or ACBD) and could participate in follow-on surveys separated by roughly three weeks in these tracks. Subjects were primarily recruited on Amazon Mechanical Turk with a paid incentive ($5-20/session), and anyone who completed 4 surveys was eligible to receive a health report.

| Overvew    |    Locations   |   
| ----------- | ----------- | 
|  ![](https://github.com/jim-schwoebel/voiceome/blob/main/assets/images/thumbnails/overview.png) | ![](https://github.com/jim-schwoebel/voiceome/blob/main/assets/images/thumbnails/locations.png) |

## Getting started
To get started, clone this repository:
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

## cleaning scripts 
-- cleaning scripts here (mono 16000 Hz from Allie)

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

Visualizers 
-- visualize scripts
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

| Survey fragment    |    Description   |   
| ----------- | ----------- | 
| [Consent form](https://github.com/jim-schwoebel/voiceome/wiki/0.-Consent-form) | A standard consent form to opt into the Voiceome study. |
| [Microphone check](https://github.com/jim-schwoebel/voiceome/wiki/00.-Microphone-check-task)| A fragment and information screen to test that a microphone is able to collect voice input from a browser. | 
| [Free speech task](https://github.com/jim-schwoebel/voiceome/wiki/01.-Free-speech-task) | A free speech prompt to collect extemporaneous speech from clinical study participants. | 
| [Category Naming Task](https://github.com/jim-schwoebel/voiceome/wiki/03.-Category-naming-task) | A prompt that asks participants to name as many animals as they can in one minute. | 
| [Letter F Task](https://github.com/jim-schwoebel/voiceome/wiki/04.-Letter-%7BFAS%7D-Tasks) | A prompt that asks participants to name as many words that start with the letter F as they can in one minute. | 
| [Paragraph Reading Task](https://github.com/jim-schwoebel/voiceome/wiki/05.-Paragraph-reading-task) | A prompt that asks participants to read the Caterpillar passage. | 
| [Sustained Phonation Task](https://github.com/jim-schwoebel/voiceome/wiki/06.-Sustained-phonation-('ahh')) | A prompt to ask users to hold a sustained phonation of 'ahh' for as long as they can in 30 seconds. | 
| [Papapa Task](https://github.com/jim-schwoebel/voiceome/wiki/07.-Pa-pa-pa-task) | A voice task to say puh-puh-puh as many times as a clinical study participant can in 10 seconds. | 
| [Pa-ta-ka Task](https://github.com/jim-schwoebel/voiceome/wiki/08.-Pa-ta-ka-task) | A voice task to say puh-tah-kah as many times as a clinical study participant can in 10 seconds. | 
| [Confrontational Naming Task](https://github.com/jim-schwoebel/voiceome/wiki/09.-Confrontational-naming-task) | Name 25 images back-to-back in a session. | 
| [Nonword Naming Task](https://github.com/jim-schwoebel/voiceome/wiki/10.-Nonword-task) | Name a series of 10 nonsense words in a session. | 
| [Immediate Recall Task](https://github.com/jim-schwoebel/voiceome/wiki/11.-Immediate-recall-task) | Recall 2 sentences played back in the browser immediately to test memory. | 
| [Spoken Diagnosis Task](https://github.com/jim-schwoebel/voiceome/wiki/12.-Spoken-diagnosis-task) | Asks individuals to name their clinical diagnoses (optional speech task). | 
| [Spoken Medication Task](https://github.com/jim-schwoebel/voiceome/wiki/13.-Spoken-medication-task) | Asks individuals to name their current medications that they are taking (optional speech task). | 
| [Confounding Questions](https://github.com/jim-schwoebel/voiceome/wiki/14.-Confounding-questions) | Survey section asking confounding questions like smoking histories, visual acuity, and other impairments. | 
| [Demographic Questions](https://github.com/jim-schwoebel/voiceome/wiki/15.-Demographic-questions) | A standard list of demographic questions | 
| [Health Labels](https://github.com/jim-schwoebel/voiceome/wiki/16.-Health-labels) | A standard list of health questionnaires that can be used as self-reported labels for vocal biomarker research. |
| [Fun Facts](https://github.com/jim-schwoebel/voiceome/wiki/17.-Fun-Facts) | Fun facts and other fragments in the survey that can be used to increase user engagement. |

### [Survey B](https://app.surveylex.com/surveys/061da3f0-a637-11eb-bcc9-eba67643f616)
![](https://github.com/jim-schwoebel/voiceome/blob/main/assets/images/B/B.gif)

### [Survey C](https://app.surveylex.com/surveys/a66494c0-a824-11ea-88c1-ab37bac1e1d4)
![](https://github.com/jim-schwoebel/voiceome/blob/main/assets/images/C/C.gif)

### [Survey D](https://app.surveylex.com/surveys/53737620-a637-11eb-bcc9-eba67643f616)
![](https://github.com/jim-schwoebel/voiceome/blob/main/assets/images/D/D.gif)

## Cite us
If you incorporate our work in your research, feel free to reference us with the APA format below:
```
Schwoebel, James, et al. "The Voiceome Study: A Longitudinal Normative Dataset and Protocol for Speech and Language Biomarker Research." Nature Methods. 2021.
```

## Data access

Data is accessible via a commercial license. 

If you are interested to license or access the Voiceome dataset, please reach out to Jim Schwoebel (VP of Data and Research @ Sonde) @ jim.schwoebel@gmail.com.

## Collaborators
[![](https://github.com/jim-schwoebel/voiceome/blob/main/assets/images/thumbnails/sonde.png)](https://sondehealth.com)
[![](https://github.com/jim-schwoebel/voiceome/blob/main/assets/images/thumbnails/collaborators.png)](https://voiceome.org)

## References
Voice Protocols
- [00. Microphone check task](https://github.com/jim-schwoebel/voiceome/wiki/00.-Microphone-check-task)
- [01. Free speech task](https://github.com/jim-schwoebel/voiceome/wiki/01.-Free-speech-task)
- [02. Picture description task](https://github.com/jim-schwoebel/voiceome/wiki/02.-Picture-description-task)
- [03. Category naming task](https://github.com/jim-schwoebel/voiceome/wiki/03.-Category-naming-task)
- [04. Letter {FAS} Tasks](https://github.com/jim-schwoebel/voiceome/wiki/04.-Letter-%7BFAS%7D-Tasks)
- [05. Paragraph reading task](https://github.com/jim-schwoebel/voiceome/wiki/05.-Paragraph-reading-task)
- [06. Sustained phonation ('ahh')](https://github.com/jim-schwoebel/voiceome/wiki/06.-Sustained-phonation-('ahh'))
- [07. Pa pa pa task](https://github.com/jim-schwoebel/voiceome/wiki/07.-Pa-pa-pa-task)
- [08. Pa ta ka task](https://github.com/jim-schwoebel/voiceome/wiki/08.-Pa-ta-ka-task)
- [09. Confrontational naming task](https://github.com/jim-schwoebel/voiceome/wiki/09.-Confrontational-naming-task)
- [10. Nonword task](https://github.com/jim-schwoebel/voiceome/wiki/10.-Nonword-task)
- [11. Immediate recall task](https://github.com/jim-schwoebel/voiceome/wiki/11.-Immediate-recall-task)
- [12. Spoken diagnosis task](https://github.com/jim-schwoebel/voiceome/wiki/12.-Spoken-diagnosis-task)
- [13. Spoken medication task](https://github.com/jim-schwoebel/voiceome/wiki/13.-Spoken-medication-task)

Health questionniares 
- [Confounding questions](https://github.com/jim-schwoebel/voiceome/wiki/14.-Confounding-questions)
- [Demographic questions](https://github.com/jim-schwoebel/voiceome/wiki/15.-Demographic-questions)
- [Custom lichert scales](https://github.com/jim-schwoebel/voiceome/wiki/16.-Health-labels#lichert-questions-custom-made)
- [PHQ-9](https://www.mdcalc.com/phq-9-patient-health-questionnaire-9)
- [GAD-7](https://patient.info/doctor/generalised-anxiety-disorder-assessment-gad-7)
- [Altman Self-rating scale](https://psychology-tools.com/test/altman-self-rating-mania-scale)
- [Audit-C](https://www.mdcalc.com/audit-c-alcohol-use)
- [Sheehan disability scale](http://memorialparkpsychiatry.com/doc/sheehan_disability_scale.pdf)
- [ADHD Self-rating Scale - Part A](https://psychology-tools.com/test/adult-adhd-self-report-scale)
- [Insomnia Severity Index](https://www.ons.org/sites/default/files/InsomniaSeverityIndex_ISI.pdf)
- [Stanford Sleepiness Scale](https://www.med.upenn.edu/cbti/assets/user-content/documents/Stanford%20Sleepiness%20Scale.pdf)
- [PTSD-5](https://www.ptsd.va.gov/professional/assessment/documents/pc-ptsd5-screen.pdf)

Other references 
- [Allie ML repository](https://github.com/jim-schwoebel/allie)
- [Voicebook](https://github.com/jim-schwoebel/voicebook)
- [SurveyLex](https://surveylex.com)
- [OpenSmile GeMAPS](https://sail.usc.edu/publications/files/eyben-preprinttaffc-2015.pdf)
- [Voiceome strategic plan](https://drive.google.com/file/d/1Dme9tUq0eCepja_7Yg9sNqn_JWKaJxJm/view)
- [Voice_datasets repo](https://github.com/jim-schwoebel/voice_datasets)
- [Amazon Mechanical Turk](https://www.mturk.com/)
