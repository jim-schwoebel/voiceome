import pandas as pd 
import numpy as np
import os, time 

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
	ids_=g['mTurk worker ID']
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

# get average distance between days 
for i in range(len(values_)):
	
	if len(values_[i]) == 1:
		print(values_[i])
		paths.append(list(values_[i][0])[0][0])
	if len(values_[i]) == 2:
		print(values_[i])
		day_dif=abs(list(values_[i][0].values())[0]-list(values_[i][1].values())[0])
		day_difs.append(day_dif)
		paths.append(list(values_[i][0])[0][0]+list(values_[i][1])[0][0])
	elif len(values_[i]) == 3:
		print(values_[i])
		day_dif=abs(list(values_[i][0].values())[0]-list(values_[i][1].values())[0])
		day_difs.append(day_dif)
		day_dif=abs(list(values_[i][1].values())[0]-list(values_[i][2].values())[0])
		day_difs.append(day_dif)
		paths.append(list(values_[i][0])[0][0]+list(values_[i][1])[0][0]+list(values_[i][2])[0][0])
	elif len(values_[i]) == 4:
		print(values_[i])
		day_dif=abs(list(values_[i][0].values())[0]-list(values_[i][1].values())[0])
		day_difs.append(day_dif)
		day_dif=abs(list(values_[i][1].values())[0]-list(values_[i][2].values())[0])
		day_difs.append(day_dif)
		day_dif=abs(list(values_[i][2].values())[0]-list(values_[i][3].values())[0])
		day_difs.append(day_dif)
		paths.append(list(values_[i][0])[0][0]+list(values_[i][1])[0][0]+list(values_[i][2])[0][0]+list(values_[i][3])[0][0])

	elif len(values_[i]) == 4:
		print(values_[i])
		day_dif=abs(list(values_[i][0].values())[0]-list(values_[i][1].values())[0])
		day_difs.append(day_dif)
		day_dif=abs(list(values_[i][1].values())[0]-list(values_[i][2].values())[0])
		day_difs.append(day_dif)
		day_dif=abs(list(values_[i][2].values())[0]-list(values_[i][3].values())[0])
		day_difs.append(day_dif)
		paths.append(list(values_[i][0])[0][0]+list(values_[i][1])[0][0]+list(values_[i][2])[0][0]+list(values_[i][3])[0][0])

print(np.mean(np.array(day_difs)))
print(np.std(np.array(day_difs)))
print(paths)
count=0

print('A')
print(paths.count('A'))
count=count+paths.count('A')
print('B')
print(paths.count('B'))
count=count+paths.count('B')
print('C')
print(paths.count('C'))
count=count+paths.count('C')
print('D')
print(paths.count('D'))
count=count+paths.count('D')
print('AA')
print(paths.count('AA'))
count=count+paths.count('AA')
print('AB')
print(paths.count('AB'))
count=count+paths.count('AB')
print('AC')
print(paths.count('AC'))
count=count+paths.count('AC')
print('AAA')
print(paths.count('AAA'))
count=count+paths.count('AAA')
print('ABA')
print(paths.count('ABA'))
count=count+paths.count('ABA')
print('ABC')
print(paths.count('ABC'))
count=count+paths.count('ABC')
print('ACB')
print(paths.count('ACB'))
count=count+paths.count('ACB')
print('AAAA')
print(paths.count('AAAA'))
count=count+paths.count('AAAA')
print('ABAB')
print(paths.count('ABAB'))
count=count+paths.count('ABAB')
print('ABCD')
print(paths.count('ABCD'))
count=count+paths.count('ABCD')
print('ACBD')
print(paths.count('ACBD'))
count=count+paths.count('ACBD')
print('OTHER')
print(len(paths)-count)
