import pandas as pd 
import numpy as np
import os, time, shutil
from tqdm import tqdm

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

def ytd_tonum(datestring):
    split=datestring.split('-')
    month=split[1]
    day=split[2]
    year=split[0]
    # all the years are the same, so ignore this
    # taken from https://www.timeanddate.com/calendar/months/
    if month == '01':
        # days in the month prior
        days=0
        
    elif month == '02':
        days=31
        
    elif month == '03':
        days=31+28
    
    elif month == '04':
        days=31+28+31
        
    elif month == '05':
        days=31+28+31+30
        
    elif month == '06':
        days=31+28+31+30+31
        
    elif month == '07':
        days=31+28+31+30+31+30
    
    elif month == '08':
        days=31+28+31+30+31+30+31
        
    elif month == '09':
        days=31+28+31+30+31+30+31+31
        
    elif month == '10':
        days=31+28+31+30+31+30+31+31+30
        
    elif month == '11':
        days=31+28+31+30+31+30+31+31+30+31
        
    elif month == '12':
        days=31+28+31+30+31+30+31+31+30+31+30

    if year == '2020':
    	days=int(day)+days
    elif year == '2019':
    	days=int(day)+days-365

    return days

listdir=os.listdir()
csv_files=list()
for i in range(len(listdir)):
	if listdir[i].endswith('.csv'):
		csv_files.append(listdir[i])

count=0
id_dict=dict()
id_list=list()

for i in range(len(csv_files)):
	g=pd.read_csv(csv_files[i])
	ids_=g['Email address']
	starts=g['startTime']
	survey=get_survey(csv_files[i])

	for j in range(len(g)):
		row=g.iloc[j,:]

		null_num=sum(pd.isnull(row))
		if null_num > 50:
			count=count+1 
		else:
			if ids_[j] in id_list: 
				if {survey:ytd_tonum(starts[j][0:10])} not in id_dict[ids_[j]]:
					id_dict[ids_[j]]=id_dict[ids_[j]]+[{survey:ytd_tonum(starts[j][0:10])}]
			else:
				id_dict[ids_[j]]=[{survey:ytd_tonum(starts[j][0:10])}]
			
			id_list.append(ids_[j])

print(count)
print(len(set(id_list)))
print(id_dict)

ids_=list(id_dict)
values_=list(id_dict.values())
yes=list()

day_difs=list()
paths=list()

sessions_2=list()
new_csvfiles=list()

# get average distance between days 
for i in range(len(values_)):
	if len(values_[i]) > 1:
		sessions_2.append(ids_[i])
		print(id_dict[ids_[i]])

for i in range(len(csv_files)):
	data=pd.read_csv(csv_files[i])
	sessions=data['sessionId']
	keep_ind=list()
	delete_ind=list()
	for j in range(len(sessions)):
		# print(sessions[j])
		# print(sum(pd.isnull(data.iloc[j,:])))
		if sum(pd.isnull(data.iloc[j,:])) < 50:
			keep_ind.append(j)
			print('here')
		else:
			delete_ind.append(j)

	print(keep_ind)
	new_dataframe= data.loc[keep_ind,:]
	new_dataframe.to_csv('clean_'+csv_files[i], index=False)
	new_csvfiles.append('clean_'+csv_files[i])

# curdir=os.getcwd()
# # now copy all the data from the new csvfiles 
# for i in range(len(new_csvfiles)):
# 	data=pd.read_csv(new_csvfiles[i])
# 	folder=new_csvfiles[i].replace('clean_','').replace('.csv','')
# 	os.mkdir(folder)
# 	# get sessions 
# 	sessions=data['sessionId']
# 	for j in tqdm(range(len(sessions))):
# 		shutil.copytree('/mnt/f/audio_datasets/2020_voiceome/all/'+folder+'/'+sessions[j], curdir+'/'+folder+'/'+sessions[j])

