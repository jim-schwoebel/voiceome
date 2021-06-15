# Voiceome
The [Voiceome Study](https://www.voiceome.org/) is the world’s largest clinical study to collect voice information labeled with health traits. The goal is to recruit between 10,000-100,000 patients into the study and track them at multiple time points to advance scientific understanding for vocal biomarkers and speed up the process for its commercialization.

[![](https://github.com/jim-schwoebel/voiceome/blob/main/assets/images/thumbnails/voiceome.png?raw=true)](https://www.youtube.com/watch?v=lCk_mffvJ0A&feature=emb_logo)

More information about the Voiceome study can be found @ [the wiki](https://github.com/jim-schwoebel/voiceome/wiki) and [website](https://voiceome.org).

## Background/goals
One of the primary causes of slow translation of voice biomarker research is a result of small datasets. There have been many research studies that have shown that acoustic or linguistic voice features relate to health conditions like stress, schizophrenia, depression, bipolar disorder, stroke, and cardiovascular diseases. However, many of these studies have relatively small sample sizes (N<1,000 patients in each class), suffer from poor audio quality (e.g. use of different microphones and data collection techniques), and are difficult to access (e.g. large licensing fees to corporations and/or difficulty obtaining IRB access without close academic ties). These factors dramatically limit the ability to model the underlying data and correlate voice data to health traits, replicate peer-reviewed publications, as well as open up this work to the broader scientific community.

![](https://github.com/jim-schwoebel/voiceome/blob/main/assets/images/thumbnails/confounds.png?raw=true)

Therefore, the main goals of the Voiceome Study include:

- **Standardizing collection tools and features** - Standardize the tools and techniques used to collect and featurize voice samples for use in health-related research. <em> We have done this by building [SurveyLex](https://surveylex.com), a web-enabled survey tool for vocal biomarker research.</em>
- **Establishing reference ranges** - Create a standard set of normative ranges of [acoustic](https://github.com/jim-schwoebel/voiceome/tree/main/assets/references/A/acoustics) and [linguistic](https://github.com/jim-schwoebel/voiceome/tree/main/assets/references/A/linguistics) features across various ages, genders, microphone types, and dialects labeled with health information. <em>These are provided as [tables](https://github.com/jim-schwoebel/voiceome/tree/main/assets/references/A/acoustics) and [standardized scripts with the Allie ML Framework](https://github.com/jim-schwoebel/allie) in this repository</em>.
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
This assumes you are using a MacOS-related computer.

### MacOS
To get started, clone this repository in a virtual environment and install requirements.txt (note this can take 10 minutes):
```
git clone git@github.com:jim-schwoebel/voiceome.git
cd voiceome
pip3 install virtualenv
virtualenv env 
source env/bin/activate
pip3 install -r requirements.txt
```

Now install various libraries with Homebrew (if you don't have Homebrew, install it before this step [following these instructions](https://brew.sh/)):
```
brew install ffmpeg sox autoconf automake m4 libtool
```

Now download [Xcode](https://www.freecodecamp.org/news/how-to-download-and-install-xcode/) if you have not done so already from the app store:
```
Open the App Store on your mac.
1. Sign in.
2. Search for Xcode.
3. Click install or update.
```
Next, install OpenSMILE:
```
cd scripts/features/helpers/opensmile/opensmile-2.3.0
bash autogen.sh
bash autogen.sh
./configure
make -j4 ; make
make install
```

Optionally, if you want to transcribe data with Microsoft Azure (this was the transcriber used in the Voiceome paper), update the ['settings.json'](https://github.com/jim-schwoebel/voiceome/blob/main/settings.json) Azure Key:
```
{"AzureKey": "KEY_GOES_HERE", 
...}
```

Now create a SurveyLex account and a survey @ SurveyLex.com - clone SurveyLex A link as a replicated template.
```
https://www.surveylex.com/
```

Collect your sample data on the SurveyLex A survey.
```
Sample data page (paste video here)
```

Download results (audio files + responses).
```

```

Put survey results in data/test/ folder and run voiceome.py to calculate results.

### Linux OS
```
git clone git@github.com:jim-schwoebel/voiceome.git
cd voiceome
pip3 install virtualenv
virtualenv env 
source env/bin/activate
pip3 install -r requirements-linux.txt
```

### Tests
You now can load the python script to call the protocol (.TXT) and references:
```
import .scripts.references

## protocols
def get_urls():
  A-https://app.surveylex.com/surveys/e1f88ee0-a636-11eb-bcc9-eba67643f616
  B-https://app.surveylex.com/surveys/061da3f0-a637-11eb-bcc9-eba67643f616
  C-https://app.surveylex.com/surveys/a66494c0-a824-11ea-88c1-ab37bac1e1d4
  D-https://app.surveylex.com/surveys/53737620-a637-11eb-bcc9-eba67643f616

def get_questions():
  --> questions 
  --> sample responses 
  --> sample audio
  --> sample features
  From surveylex export (sample.csv)

def clean_audio(audiofile):
  --> clean audio into mono 16000 Hz with Allie script

def transcribe_audio():
  --> transcribe using Microsoft Azure with a key
  
def featurize_audio(audiofile, embedding):
  if / elif
  --> featurize audio file (acoustic)
  --> featurize audio file (linguistic)

def check_quality(audiofile, task):
  --> quality references 
 
def get_reference(task, embedding, feature, age):
  00. Microphone check task
  01. Free speech task
  02. Picture description task
  03. Category naming task
  04. Letter {FAS} Tasks
  05. Paragraph reading task
  06. Sustained phonation ('ahh')
  07. Pa pa pa task
  08. Pa ta ka task
  09. Confrontational naming task
  10. Nonword task
  11. Immediate recall task
  12. Spoken diagnosis task
  13. Spoken medication task

def visualize(task):
-- visualize scripts
```

You can then get references for a specific feature within an embedding:
```
+---------+---------+------------------+---------+---------+----------+--------+
|  Task   | Feature |     Feature      | AgeGend | Average | Standard | Sample |
|         |  Type   |                  |   er    |         |  Deviati |  Numbe |
|         |         |                  |         |         |    on    |   r    |
+---------+---------+------------------+---------+---------+----------+--------+
| microph | Opensmi | F0semitoneFrom27 | AllAges | 30.258  |  6.547   |  2466  |
| one_tas | leFeatu | .5Hz_sma3nz_amea | Genders |         |          |        |
|    k    |   res   |        n         |         |         |          |        |
+---------+---------+------------------+---------+---------+----------+--------+
```
You can also get all the features for a specific age/gender and speech task:
```
+--------+---------+---------------------+--------+----------+---------+-------+
|  Task  | Feature |       Feature       | AgeGen | Average  | Standar | Sampl |
|        |  Type   |                     |  der   |          | d Devia | e Num |
|        |         |                     |        |          |  tion   |  ber  |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | F0semitoneFrom27.5H | AllAge |  30.258  |  6.547  | 2466  |
| hone_t | leFeatu |   z_sma3nz_amean    | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | F0semitoneFrom27.5H | AllAge |  0.134   |  0.09   | 2466  |
| hone_t | leFeatu | z_sma3nz_stddevNorm | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | F0semitoneFrom27.5H | AllAge |  27.806  |  6.854  | 2466  |
| hone_t | leFeatu | z_sma3nz_percentile | sGende |          |         |       |
|  ask   |   res   |        20.0         |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | F0semitoneFrom27.5H | AllAge |  29.863  |  6.792  | 2466  |
| hone_t | leFeatu | z_sma3nz_percentile | sGende |          |         |       |
|  ask   |   res   |        50.0         |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | F0semitoneFrom27.5H | AllAge |  32.277  |  6.962  | 2466  |
| hone_t | leFeatu | z_sma3nz_percentile | sGende |          |         |       |
|  ask   |   res   |        80.0         |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | F0semitoneFrom27.5H | AllAge |  4.471   |  3.678  | 2466  |
| hone_t | leFeatu | z_sma3nz_pctlrange0 | sGende |          |         |       |
|  ask   |   res   |         -2          |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | F0semitoneFrom27.5H | AllAge | 169.055  | 241.752 | 2466  |
| hone_t | leFeatu | z_sma3nz_meanRising | sGende |          |         |       |
|  ask   |   res   |        Slope        |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | F0semitoneFrom27.5H | AllAge | 165.449  | 258.389 | 2466  |
| hone_t | leFeatu | z_sma3nz_stddevRisi | sGende |          |         |       |
|  ask   |   res   |       ngSlope       |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | F0semitoneFrom27.5H | AllAge |  65.253  | 108.258 | 2466  |
| hone_t | leFeatu | z_sma3nz_meanFallin | sGende |          |         |       |
|  ask   |   res   |       gSlope        |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | F0semitoneFrom27.5H | AllAge |  67.611  | 143.412 | 2466  |
| hone_t | leFeatu | z_sma3nz_stddevFall | sGende |          |         |       |
|  ask   |   res   |      ingSlope       |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | loudness_sma3_amean | AllAge |  0.365   |  0.277  | 2466  |
| hone_t | leFeatu |                     | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | loudness_sma3_stdde | AllAge |  0.938   |  0.278  | 2466  |
| hone_t | leFeatu |        vNorm        | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | loudness_sma3_perce | AllAge |  0.094   |  0.111  | 2466  |
| hone_t | leFeatu |      ntile20.0      | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | loudness_sma3_perce | AllAge |  0.231   |  0.21   | 2466  |
| hone_t | leFeatu |      ntile50.0      | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | loudness_sma3_perce | AllAge |  0.628   |  0.499  | 2466  |
| hone_t | leFeatu |      ntile80.0      | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | loudness_sma3_pctlr | AllAge |  0.534   |  0.446  | 2466  |
| hone_t | leFeatu |       ange0-2       | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | loudness_sma3_meanR | AllAge |  7.091   |  5.202  | 2466  |
| hone_t | leFeatu |     isingSlope      | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | loudness_sma3_stdde | AllAge |  4.103   |  3.196  | 2466  |
| hone_t | leFeatu |    vRisingSlope     | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | loudness_sma3_meanF | AllAge |   5.02   |  3.834  | 2466  |
| hone_t | leFeatu |     allingSlope     | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | loudness_sma3_stdde | AllAge |   2.96   |  2.462  | 2466  |
| hone_t | leFeatu |    vFallingSlope    | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | jitterLocal_sma3nz_ | AllAge |  0.029   |  0.013  | 2466  |
| hone_t | leFeatu |        amean        | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | jitterLocal_sma3nz_ | AllAge |  1.228   |  0.467  | 2466  |
| hone_t | leFeatu |     stddevNorm      | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | shimmerLocaldB_sma3 | AllAge |  1.321   |  0.359  | 2466  |
| hone_t | leFeatu |      nz_amean       | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | shimmerLocaldB_sma3 | AllAge |  0.827   |  0.189  | 2466  |
| hone_t | leFeatu |    nz_stddevNorm    | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | HNRdBACF_sma3nz_ame | AllAge |  6.201   |  2.411  | 2466  |
| hone_t | leFeatu |         an          | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | HNRdBACF_sma3nz_std | AllAge |  0.593   |  2.226  | 2466  |
| hone_t | leFeatu |       devNorm       | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | logRelF0-H1-H2_sma3 | AllAge |  4.971   |  6.175  | 2466  |
| hone_t | leFeatu |      nz_amean       | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | logRelF0-H1-H2_sma3 | AllAge |  1.799   | 87.279  | 2466  |
| hone_t | leFeatu |    nz_stddevNorm    | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | logRelF0-H1-A3_sma3 | AllAge |  22.207  |  7.702  | 2466  |
| hone_t | leFeatu |      nz_amean       | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | logRelF0-H1-A3_sma3 | AllAge |  0.568   |  2.625  | 2466  |
| hone_t | leFeatu |    nz_stddevNorm    | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | F1frequency_sma3nz_ | AllAge | 622.454  | 123.019 | 2466  |
| hone_t | leFeatu |        amean        | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | F1frequency_sma3nz_ | AllAge |  0.268   |  0.071  | 2466  |
| hone_t | leFeatu |     stddevNorm      | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | F1bandwidth_sma3nz_ | AllAge | 1416.315 | 204.453 | 2466  |
| hone_t | leFeatu |        amean        | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | F1bandwidth_sma3nz_ | AllAge |  0.154   |  0.045  | 2466  |
| hone_t | leFeatu |     stddevNorm      | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | F1amplitudeLogRelF0 | AllAge | -134.965 | 24.788  | 2466  |
| hone_t | leFeatu |    _sma3nz_amean    | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | F1amplitudeLogRelF0 | AllAge |  -0.66   |  0.203  | 2466  |
| hone_t | leFeatu | _sma3nz_stddevNorm  | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | F2frequency_sma3nz_ | AllAge | 1532.885 | 227.086 | 2466  |
| hone_t | leFeatu |        amean        | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | F2frequency_sma3nz_ | AllAge |  0.132   |  0.032  | 2466  |
| hone_t | leFeatu |     stddevNorm      | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | F2amplitudeLogRelF0 | AllAge | -135.562 | 24.285  | 2466  |
| hone_t | leFeatu |    _sma3nz_amean    | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | F2amplitudeLogRelF0 | AllAge |  -0.625  |  0.184  | 2466  |
| hone_t | leFeatu | _sma3nz_stddevNorm  | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | F3frequency_sma3nz_ | AllAge | 2498.829 | 351.12  | 2466  |
| hone_t | leFeatu |        amean        | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | F3frequency_sma3nz_ | AllAge |  0.081   |  0.02   | 2466  |
| hone_t | leFeatu |     stddevNorm      | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | F3amplitudeLogRelF0 | AllAge | -138.061 |  23.45  | 2466  |
| hone_t | leFeatu |    _sma3nz_amean    | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | F3amplitudeLogRelF0 | AllAge |  -0.586  |  0.168  | 2466  |
| hone_t | leFeatu | _sma3nz_stddevNorm  | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | alphaRatioV_sma3nz_ | AllAge | -12.686  |  5.009  | 2466  |
| hone_t | leFeatu |        amean        | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | alphaRatioV_sma3nz_ | AllAge |  -0.719  |  1.985  | 2466  |
| hone_t | leFeatu |     stddevNorm      | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | hammarbergIndexV_sm | AllAge |  24.405  |  6.37   | 2466  |
| hone_t | leFeatu |     a3nz_amean      | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | hammarbergIndexV_sm | AllAge |  0.377   |  0.211  | 2466  |
| hone_t | leFeatu |   a3nz_stddevNorm   | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | slopeV0-500_sma3nz_ | AllAge |  0.042   |  0.033  | 2466  |
| hone_t | leFeatu |        amean        | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | slopeV0-500_sma3nz_ | AllAge |   0.42   |  19.24  | 2466  |
| hone_t | leFeatu |     stddevNorm      | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | slopeV500-1500_sma3 | AllAge |  -0.014  |  0.011  | 2466  |
| hone_t | leFeatu |      nz_amean       | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | slopeV500-1500_sma3 | AllAge |  -1.153  |  90.51  | 2466  |
| hone_t | leFeatu |    nz_stddevNorm    | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | alphaRatioUV_sma3nz | AllAge |  -7.893  |  6.042  | 2466  |
| hone_t | leFeatu |       _amean        | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | hammarbergIndexUV_s | AllAge |  17.478  |  7.116  | 2466  |
| hone_t | leFeatu |     ma3nz_amean     | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | slopeUV0-500_sma3nz | AllAge |  0.018   |  0.036  | 2466  |
| hone_t | leFeatu |       _amean        | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | slopeUV500-1500_sma | AllAge |   0.01   |  0.011  | 2466  |
| hone_t | leFeatu |      3nz_amean      | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | loudnessPeaksPerSec | AllAge |  2.816   |  1.034  | 2466  |
| hone_t | leFeatu |                     | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | VoicedSegmentsPerSe | AllAge |  1.926   |  0.711  | 2466  |
| hone_t | leFeatu |          c          | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | MeanVoicedSegmentLe | AllAge |   0.18   |  0.096  | 2466  |
| hone_t | leFeatu |       ngthSec       | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | StddevVoicedSegment | AllAge |  0.141   |  0.085  | 2466  |
| hone_t | leFeatu |      LengthSec      | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | MeanUnvoicedSegment | AllAge |  0.463   |  0.934  | 2466  |
| hone_t | leFeatu |       Length        | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
| microp | Opensmi | StddevUnvoicedSegme | AllAge |  0.427   |  0.342  | 2466  |
| hone_t | leFeatu |      ntLength       | sGende |          |         |       |
|  ask   |   res   |                     |   rs   |          |         |       |
+--------+---------+---------------------+--------+----------+---------+-------+
```

You can also get how a specific feature is distributed across speech tasks:
```
+----------+------------+-----------+---------+---------+------------+---------+
|   Task   | FeatureTyp |  Feature  | AgeGend | Average | Standard D | Sample  |
|          |     e      |           |   er    |         |  eviation  | Number  |
+----------+------------+-----------+---------+---------+------------+---------+
| micropho | OpensmileF | microphon | AllAges | 24.907  |   5.774    |   371   |
| ne_task  |  eatures   |  e_task   | Genders |         |            |         |
+----------+------------+-----------+---------+---------+------------+---------+
| micropho | OpensmileF | freespeec | AllAges | 24.839  |   5.125    |   371   |
| ne_task  |  eatures   |  h_task   | Genders |         |            |         |
+----------+------------+-----------+---------+---------+------------+---------+
| micropho | OpensmileF | picture_t | AllAges |  25.07  |    4.71    |   371   |
| ne_task  |  eatures   |    ask    | Genders |         |            |         |
+----------+------------+-----------+---------+---------+------------+---------+
| micropho | OpensmileF | category_ | AllAges | 25.659  |   5.474    |   371   |
| ne_task  |  eatures   |   task    | Genders |         |            |         |
+----------+------------+-----------+---------+---------+------------+---------+
| micropho | OpensmileF | letterf_t | AllAges | 25.638  |   5.578    |   371   |
| ne_task  |  eatures   |    ask    | Genders |         |            |         |
+----------+------------+-----------+---------+---------+------------+---------+
| micropho | OpensmileF | paragraph | AllAges | 25.474  |   5.653    |   369   |
| ne_task  |  eatures   |   _task   | Genders |         |            |         |
+----------+------------+-----------+---------+---------+------------+---------+
| micropho | OpensmileF | ahh_task  | AllAges | 26.309  |   6.227    |   371   |
| ne_task  |  eatures   |           | Genders |         |            |         |
+----------+------------+-----------+---------+---------+------------+---------+
| micropho | OpensmileF | papapa_ta | AllAges | 25.475  |    7.77    |   371   |
| ne_task  |  eatures   |    sk     | Genders |         |            |         |
+----------+------------+-----------+---------+---------+------------+---------+
| micropho | OpensmileF | pataka_ta | AllAges | 25.626  |   7.049    |   371   |
| ne_task  |  eatures   |    sk     | Genders |         |            |         |
+----------+------------+-----------+---------+---------+------------+---------+
| micropho | OpensmileF | mandog_ta | AllAges |  24.25  |    8.59    |   371   |
| ne_task  |  eatures   |    sk     | Genders |         |            |         |
+----------+------------+-----------+---------+---------+------------+---------+
| micropho | OpensmileF | tourbus_t | AllAges | 24.281  |   7.271    |   371   |
| ne_task  |  eatures   |    ask    | Genders |         |            |         |
+----------+------------+-----------+---------+---------+------------+---------+
| micropho | OpensmileF | diagnosis | AllAges | 24.382  |   6.588    |   335   |
| ne_task  |  eatures   |   _task   | Genders |         |            |         |
+----------+------------+-----------+---------+---------+------------+---------+
| micropho | OpensmileF | medicatio | AllAges | 24.601  |   6.445    |   323   |
| ne_task  |  eatures   |  n_task   | Genders |         |            |         |
+----------+------------+-----------+---------+---------+------------+---------+
```

If you have any thing else you'd find valuable - feel free to [suggest some new features here!](https://github.com/jim-schwoebel/voiceome/issues/new)

## Changing settings

[Settings.json](https://github.com/jim-schwoebel/voiceome/blob/main/settings.json) specifies various settings for the API. The configuration options are listed in the table below. Note all possible options are listed out in the [options folder](https://github.com/jim-schwoebel/voiceome/tree/main/data/options) as .JSON files.

| Setting     |    Default option   |  All Options | Description |
| ----------- | ----------- | ----------- | ----------- |
| 'AzureKey' | 'TEST' | Any string related to the Azure string | Azure key for API usage in transcription. | 
| 'Features' | 'opensmile_features' | ['opensmile_features', 'prosody_features' 'pause_features', 'audiotext_features'] | The default feature embedding to use to calculate features/references. |
| 'FeatureType' | 'F0semitoneFrom27.5Hz_sma3nz_amean' |  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'space', 'numbers', 'capletters', 'cc', 'cd', 'dt', 'ex', 'in', 'jj', 'jjr', 'jjs', 'ls', 'md', 'nn', 'nnp', 'nns', 'pdt', 'pos', 'prp', 'prp2', 'rbr', 'rbs', 'rp', 'to', 'uh', 'vb', 'vbd', 'vbg', 'vbn', 'vbp', 'vbz', 'wdt', 'wp', 'wrb', 'polarity', 'subjectivity', 'repeat', 'uniquewords', 'n_sents', 'n_words', 'n_chars', 'n_syllables', 'n_unique_words', 'n_long_words', 'n_monosyllable_words', 'n_polysyllable_words', 'flesch_kincaid_grade_level', 'flesch_reading_ease', 'smog_index', 'gunning_fog_index', 'coleman_liau_index', 'automated_readability_index', 'lix', 'gulpease_index', 'wiener_sachtextformel', 'PROPN', 'ADP', 'DET', 'NUM', 'PUNCT', 'SPACE', 'VERB', 'NOUN', 'ADV', 'CCONJ', 'PRON', 'ADJ', 'SYM', 'PART', 'INTJ', 'X', 'pos_other', 'NNP', 'IN', 'DT', 'CD', 'NNPS', ',', '_SP', 'VBZ', 'NN', 'RB', 'CC', '', 'NNS', '.', 'PRP', 'MD', 'VB', 'HYPH', 'VBD', 'JJ', ':', '-LRB-', '$', '-RRB-', 'VBG', 'VBN', 'NFP', 'RBR', 'POS', 'VBP', 'RP', 'JJS', 'PRP$', 'EX', 'JJR', 'WP', 'WDT', 'TO', 'WRB', 'PDT', 'AFX', 'RBS', 'UH', 'WP$', 'FW', 'XX', 'LS', 'ADD', 'tag_other', 'compound', 'ROOT', 'prep', 'det', 'pobj', 'nummod', 'punct', 'nsubj', 'advmod', 'conj', 'aux', 'dobj', 'nmod', 'acl', 'appos', 'npadvmod', 'amod', 'agent', 'case', 'intj', 'prt', 'pcomp', 'ccomp', 'attr', 'dep', 'acomp', 'poss', 'auxpass', 'expl', 'mark', 'nsubjpass', 'quantmod', 'advcl', 'relcl', 'oprd', 'neg', 'xcomp', 'csubj', 'predet', 'parataxis', 'dative', 'preconj', 'csubjpass', 'meta', 'dep_other', 'shape_other', 'mean sentence polarity', 'std sentence polarity', 'max sentence polarity', 'min sentence polarity', 'median sentence polarity', 'mean sentence subjectivity', 'std sentence subjectivity', 'max sentence subjectivity', 'min sentence subjectivity', 'median sentence subjectivity', 'character count', 'word count', 'sentence number', 'words per sentence', 'unique chunk noun text', 'unique chunk root text', 'unique chunk root head text', 'chunkdep ROOT', 'chunkdep pobj', 'chunkdep nsubj', 'chunkdep dobj', 'chunkdep conj', 'chunkdep appos', 'chunkdep attr', 'chunkdep nsubjpass', 'chunkdep dative', 'chunkdep pcomp', 'number of named entities', 'PERSON', 'NORP', 'FAC', 'ORG', 'GPE', 'LOC', 'PRODUCT', 'EVENT', 'WORK_OF_ART', 'LAW', 'LANGUAGE', 'DATE', 'TIME', 'PERCENT', 'MONEY', 'QUANTITY', 'ORDINAL', 'CARDINAL', 'filler ratio', 'type token ratio', 'standardized word entropy', 'question ratio', 'number ratio', 'Brunets Index', 'Honores statistic', 'datewords freq', 'word number', 'five word count', 'max word length', 'min word length', 'variance of vocabulary', 'std of vocabulary', 'sentencenum', 'periods', 'questions', 'interjections', 'repeatavg', 'filler_ratio', 'type_token_ratio', 'standardized_word_entropy', 'question_ratio', 'number_ratio', 'brunets_index', 'honores_statistic', 'pronoun_to_noun_ratio', 'F0semitoneFrom27.5Hz_sma3nz_amean', 'F0semitoneFrom27.5Hz_sma3nz_stddevNorm', 'F0semitoneFrom27.5Hz_sma3nz_percentile20.0', 'F0semitoneFrom27.5Hz_sma3nz_percentile50.0', 'F0semitoneFrom27.5Hz_sma3nz_percentile80.0', 'F0semitoneFrom27.5Hz_sma3nz_pctlrange0-2', 'F0semitoneFrom27.5Hz_sma3nz_meanRisingSlope', 'F0semitoneFrom27.5Hz_sma3nz_stddevRisingSlope', 'F0semitoneFrom27.5Hz_sma3nz_meanFallingSlope', 'F0semitoneFrom27.5Hz_sma3nz_stddevFallingSlope', 'loudness_sma3_amean', 'loudness_sma3_stddevNorm', 'loudness_sma3_percentile20.0', 'loudness_sma3_percentile50.0', 'loudness_sma3_percentile80.0', 'loudness_sma3_pctlrange0-2', 'loudness_sma3_meanRisingSlope', 'loudness_sma3_stddevRisingSlope', 'loudness_sma3_meanFallingSlope', 'loudness_sma3_stddevFallingSlope', 'jitterLocal_sma3nz_amean', 'jitterLocal_sma3nz_stddevNorm', 'shimmerLocaldB_sma3nz_amean', 'shimmerLocaldB_sma3nz_stddevNorm', 'HNRdBACF_sma3nz_amean', 'HNRdBACF_sma3nz_stddevNorm', 'logRelF0-H1-H2_sma3nz_amean', 'logRelF0-H1-H2_sma3nz_stddevNorm', 'logRelF0-H1-A3_sma3nz_amean', 'logRelF0-H1-A3_sma3nz_stddevNorm', 'F1frequency_sma3nz_amean', 'F1frequency_sma3nz_stddevNorm', 'F1bandwidth_sma3nz_amean', 'F1bandwidth_sma3nz_stddevNorm', 'F1amplitudeLogRelF0_sma3nz_amean', 'F1amplitudeLogRelF0_sma3nz_stddevNorm', 'F2frequency_sma3nz_amean', 'F2frequency_sma3nz_stddevNorm', 'F2amplitudeLogRelF0_sma3nz_amean', 'F2amplitudeLogRelF0_sma3nz_stddevNorm', 'F3frequency_sma3nz_amean', 'F3frequency_sma3nz_stddevNorm', 'F3amplitudeLogRelF0_sma3nz_amean', 'F3amplitudeLogRelF0_sma3nz_stddevNorm', 'alphaRatioV_sma3nz_amean', 'alphaRatioV_sma3nz_stddevNorm', 'hammarbergIndexV_sma3nz_amean', 'hammarbergIndexV_sma3nz_stddevNorm', 'slopeV0-500_sma3nz_amean', 'slopeV0-500_sma3nz_stddevNorm', 'slopeV500-1500_sma3nz_amean', 'slopeV500-1500_sma3nz_stddevNorm', 'alphaRatioUV_sma3nz_amean', 'hammarbergIndexUV_sma3nz_amean', 'slopeUV0-500_sma3nz_amean', 'slopeUV500-1500_sma3nz_amean', 'loudnessPeaksPerSec', 'VoicedSegmentsPerSec', 'MeanVoicedSegmentLengthSec', 'StddevVoicedSegmentLengthSec', 'MeanUnvoicedSegmentLength', 'StddevUnvoicedSegmentLength', 'Speech_Time_VADInt_1', 'Total_Time_VADInt_1', 'Pause_Time_VADInt_1', 'Pause_Percentage_VADInt_1', 'Pause_Speech_Ratio_VADInt_1', 'Mean_Pause_Length_VADInt_1', 'Pause_Variability_VADInt_1', 'Speech_Time_VADInt_2', 'Total_Time_VADInt_2', 'Pause_Time_VADInt_2', 'Pause_Percentage_VADInt_2', 'Pause_Speech_Ratio_VADInt_2', 'Mean_Pause_Length_VADInt_2', 'Pause_Variability_VADInt_2', 'Speech_Time_VADInt_3', 'Total_Time_VADInt_3', 'Pause_Time_VADInt_3', 'Pause_Percentage_VADInt_3', 'Pause_Speech_Ratio_VADInt_3', 'Mean_Pause_Length_VADInt_3', 'Pause_Variability_VADInt_3', 'UtteranceNumber', 'PauseNumber', 'AveragePauseLength', 'StdPauseLength', 'TimeToFirstPhonation', 'TimeToLastPhonation', 'UtterancePerMin', 'WordsPerMin', 'Duration'] | The default feature label for sorting data. |
| 'Task' | 'microphone_task' | ['microphone_task', 'freespeech_task', 'picture_task', 'category_task', 'letterf_task', 'paragraph_task', 'ahh_task', 'papapa_task', 'pataka_task', 'confrontational_task', 'nonword_task', 'recall_mandog_task', 'recall_tourbus_task', 'diagnosis_task', 'medication_task'] | The default task to customize API usage. | 
| 'TranscriptEngine' | "azure" | ["azure", "deepspeech_dict", "deepspeech_nodict", "wav2vec"] | The default transcription engine to use for audiotext_features. | 
| 'CleanAudio' | True | [True, False] | Whether or not you should clean audio files during featurization to mono16000Hz. | 
| 'DefaultAgeGender' | 'all' | ['TwentiesMale', 'TwentiesFemale', 'ThirtiesMale', 'ThirtiesFemale', 'FourtiesMale]', 'FourtiesFemale', 'FiftiesMale', 'FiftiesFemale', 'SixtiesMale', 'SixtiesFemale', 'AllAgesGenders'] | The default age and gender to use for reference ranges. | 

## surveys 
Here are the 4 main surveys used in the Voiceome clinical study:

| Survey     |    Link    |   Number of completions |
| ----------- | ----------- | ----------- |
| Survey A      | [https://app.surveylex.com/surveys/8a32cbb0-cc8a-11eb-9ea3-938cc8b6d71e](https://app.surveylex.com/surveys/8a32cbb0-cc8a-11eb-9ea3-938cc8b6d71e), but for new studies recommend a slightly altered survey [here](https://app.surveylex.com/surveys/2f5b97d0-cc94-11eb-8595-0ba9699e9d53).      | 6,426     |
| Survey B  | [https://app.surveylex.com/surveys/061da3f0-a637-11eb-bcc9-eba67643f616](https://app.surveylex.com/surveys/061da3f0-a637-11eb-bcc9-eba67643f616) | 1400 |
| Survey C | [https://app.surveylex.com/surveys/a66494c0-a824-11ea-88c1-ab37bac1e1d4](https://app.surveylex.com/surveys/a66494c0-a824-11ea-88c1-ab37bac1e1d4) | 800 |
| Survey D | [https://app.surveylex.com/surveys/53737620-a637-11eb-bcc9-eba67643f616](https://app.surveylex.com/surveys/53737620-a637-11eb-bcc9-eba67643f616) | 100 |

Previews for each of these surveys are provided below as .GIFs so that you can quickly visualize the survey experience for clinical study participants.

Note you can clone these surveys @ https://surveylex.com and replicate our work in other patient populations.

### [Survey A](https://app.surveylex.com/surveys/8a32cbb0-cc8a-11eb-9ea3-938cc8b6d71e)
![](https://github.com/jim-schwoebel/voiceome/blob/main/assets/images/A/A.gif)

| Survey fragment    |    Description   | Sample Audio |   
| ----------- | ----------- |  ----------- | 
| [Consent form](https://github.com/jim-schwoebel/voiceome/wiki/0.-Consent-form) | A standard consent form to opt into the Voiceome study. | n/a | 
| [Microphone check](https://github.com/jim-schwoebel/voiceome/wiki/00.-Microphone-check-task)| A fragment and information screen to test that a microphone is able to collect voice input from a browser. | [![](https://github.com/jim-schwoebel/voiceome/blob/main/assets/images/thumbnails/play.svg)](https://drive.google.com/file/d/1c54zKMuBxCririQrrbvKBuJG6c0UpgOK/view?usp=sharing) |
| [Free speech task](https://github.com/jim-schwoebel/voiceome/wiki/01.-Free-speech-task) | A free speech prompt to collect extemporaneous speech from clinical study participants. | [![](https://github.com/jim-schwoebel/voiceome/blob/main/assets/images/thumbnails/play.svg)](https://drive.google.com/file/d/1RcC8PY84rPg7qZKA6BFMXc2XmBElXM6e/view?usp=sharing) |
| [Category Naming Task](https://github.com/jim-schwoebel/voiceome/wiki/03.-Category-naming-task) | A prompt that asks participants to name as many animals as they can in one minute. | [![](https://github.com/jim-schwoebel/voiceome/blob/main/assets/images/thumbnails/play.svg)](https://drive.google.com/file/d/114XDxQwd621pQM5JYukXPRm5QONTpaGW/view?usp=sharing) |
| [Letter F Task](https://github.com/jim-schwoebel/voiceome/wiki/04.-Letter-%7BFAS%7D-Tasks) | A prompt that asks participants to name as many words that start with the letter F as they can in one minute. | [![](https://github.com/jim-schwoebel/voiceome/blob/main/assets/images/thumbnails/play.svg)](https://drive.google.com/file/d/1m-gRiiaPS4m7bFx7B22rgC5ZsBsejaZ9/view?usp=sharing) |
| [Paragraph Reading Task](https://github.com/jim-schwoebel/voiceome/wiki/05.-Paragraph-reading-task) | A prompt that asks participants to read the Caterpillar passage. | [![](https://github.com/jim-schwoebel/voiceome/blob/main/assets/images/thumbnails/play.svg)](https://drive.google.com/file/d/1pF4Jw6vTL3GOewZOn-dceD4z645ACEzg/view?usp=sharing) |
| [Sustained Phonation Task](https://github.com/jim-schwoebel/voiceome/wiki/06.-Sustained-phonation-('ahh')) | A prompt to ask users to hold a sustained phonation of 'ahh' for as long as they can in 30 seconds. | [![](https://github.com/jim-schwoebel/voiceome/blob/main/assets/images/thumbnails/play.svg)](https://drive.google.com/file/d/1XUrfVM_dnDeA21jaHRXtn6guspZczTeV/view?usp=sharing) |
| [Papapa Task](https://github.com/jim-schwoebel/voiceome/wiki/07.-Pa-pa-pa-task) | A voice task to say puh-puh-puh as many times as a clinical study participant can in 10 seconds. | [![](https://github.com/jim-schwoebel/voiceome/blob/main/assets/images/thumbnails/play.svg)](https://drive.google.com/file/d/1nqknAogTF90Zw6Cckcg85CjObVoYSpBG/view?usp=sharing) |
| [Pa-ta-ka Task](https://github.com/jim-schwoebel/voiceome/wiki/08.-Pa-ta-ka-task) | A voice task to say puh-tah-kah as many times as a clinical study participant can in 10 seconds. | [![](https://github.com/jim-schwoebel/voiceome/blob/main/assets/images/thumbnails/play.svg)](https://drive.google.com/file/d/1WFlkKbyUCREtyhybN-TFVGs3h8-Yj4nc/view?usp=sharing) |
| [Confrontational Naming Task](https://github.com/jim-schwoebel/voiceome/wiki/09.-Confrontational-naming-task) | Name 25 images back-to-back in a session. | [![](https://github.com/jim-schwoebel/voiceome/blob/main/assets/images/thumbnails/play.svg)](https://drive.google.com/file/d/1HgPxr0Kiz2z5PNtJ10iXAZnN0dnxhQJQ/view?usp=sharing) |
| [Nonword Naming Task](https://github.com/jim-schwoebel/voiceome/wiki/10.-Nonword-task) | Name a series of 10 nonsense words in a session. | [![](https://github.com/jim-schwoebel/voiceome/blob/main/assets/images/thumbnails/play.svg)](https://drive.google.com/file/d/1yaKH85Gm6kvuSjThKMkWnofWUS-VvMkG/view?usp=sharing) |
| [Immediate Recall Tasks](https://github.com/jim-schwoebel/voiceome/wiki/11.-Immediate-recall-task) | Recall 2 sentences played back in the browser immediately to test memory. | [![](https://github.com/jim-schwoebel/voiceome/blob/main/assets/images/thumbnails/play.svg)](https://drive.google.com/file/d/1OpNdamMRar9eJx2q3iouzKVZf02nCyLB/view?usp=sharing) |
| [Spoken Diagnosis Task](https://github.com/jim-schwoebel/voiceome/wiki/12.-Spoken-diagnosis-task) | Asks individuals to name their clinical diagnoses (optional speech task). | [![](https://github.com/jim-schwoebel/voiceome/blob/main/assets/images/thumbnails/play.svg)](https://drive.google.com/file/d/13v6Sj5GB6dDUWWTBaIbG2qGX9pWDjbEM/view?usp=sharing) |
| [Spoken Medication Task](https://github.com/jim-schwoebel/voiceome/wiki/13.-Spoken-medication-task) | Asks individuals to name their current medications that they are taking (optional speech task). | [![](https://github.com/jim-schwoebel/voiceome/blob/main/assets/images/thumbnails/play.svg)](https://drive.google.com/file/d/1I7PwZbK2xu9PPNyYoJ8qyW1bWk2qlyFC/view?usp=sharing) |
| [Confounding Questions](https://github.com/jim-schwoebel/voiceome/wiki/14.-Confounding-questions) | Survey section asking confounding questions like smoking histories, visual acuity, and other impairments. | n/a|
| [Demographic Questions](https://github.com/jim-schwoebel/voiceome/wiki/15.-Demographic-questions) | A standard list of demographic questions | n/a |
| [Health Labels](https://github.com/jim-schwoebel/voiceome/wiki/16.-Health-labels) | A standard list of health questionnaires that can be used as self-reported labels for vocal biomarker research. | n/a |
| [Fun Facts](https://github.com/jim-schwoebel/voiceome/wiki/17.-Fun-Facts) | Fun facts and other fragments in the survey that can be used to increase user engagement. | n/a |

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
We have tried to make acoustic and linguistic feature reference ranges for each task as open as possible. These are available in this repository under an Apache 2.0 license.

The sample audio and spreadsheets released in this repository are also released under an Apache 2.0 license. They were recorded by Jim Schwoebel in a controlled setting, cloning the protocol on the SurveyLex product. We did not use any sample data from participants here to protect their identities.

Also, note that OpenSMILE GeMAPS features are for research-only use. Keep this in mind if you are working on commercial deployments. Read more about their dual licensing model [here](https://github.com/audeering/opensmile). Since this repository was in the scope of research, we fall within this dual license model and can publish these references openly.

Raw audio data and .CSV labels for the Voiceome Study is accessible via a commercial license. If you are interested to license or access the Voiceome dataset, please reach out to Jim Schwoebel (VP of Data and Research @ Sonde) @ jim.schwoebel@gmail.com.

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
