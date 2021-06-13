import json

data=dict()

data['SurveyA'] = 'https://app.surveylex.com/surveys/e1f88ee0-a636-11eb-bcc9-eba67643f616'
data['SurveyB'] = 'https://app.surveylex.com/surveys/061da3f0-a637-11eb-bcc9-eba67643f616'
data['SurveyC'] = 'https://app.surveylex.com/surveys/a66494c0-a824-11ea-88c1-ab37bac1e1d4'
data['SurveyD'] = 'https://app.surveylex.com/surveys/53737620-a637-11eb-bcc9-eba67643f616'

jsonfile=open('urls.json','w')
json.dump(data,jsonfile)
jsonfile.close()