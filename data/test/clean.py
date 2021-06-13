import os
import pandas as pd
try:
    import datacleaner
except:
    os.system('pip3 install datacleaner==0.1.5')
    import datacleaner

def clean_csv(csvfile, basedir):
    '''
    https://github.com/rhiever/datacleaner
    '''
    input_dataframe=pd.read_csv(csvfile)
    newframe=datacleaner.autoclean(input_dataframe, drop_nans=False, copy=False, ignore_update_check=False)
    newfile='clean_'+csvfile
    newframe.to_csv(newfile, index=False)
    return [newfile]

file=clean_csv('data.csv', os.getcwd())

# need to calculate GAD-7, PHQ-9, insomnia_severity, and a few others