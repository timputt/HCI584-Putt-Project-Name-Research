#This is my playground testing file
'''
import pandas as pd
df = pd.read_csv('ssn_files/yob1880.txt', sep=",", header=None)

print(df)
'''


import pandas as pd
import re

from glob import glob
lst = glob("ssn_files/*.txt")
dflist = []

for fn in lst:
    #print(fn)
    numlist = re.findall(r'\d+', fn)
    year = int(numlist[0])
    df = pd.read_csv(fn, sep=",", header=None)
    df.insert(loc=3, column='3', value=year) # insert as new index 2
    #print(df.head(10))
    dflist = dflist + [df]

dfbig = pd.concat(dflist, axis=0, ignore_index=True)
dfbig = dfbig.set_axis(["Name", "Gender", "Count", "Year"], axis=1)
print(dfbig.head()) 
dfbig.to_csv('ssn_files/all_years.csv', mode="w+", index=False)


