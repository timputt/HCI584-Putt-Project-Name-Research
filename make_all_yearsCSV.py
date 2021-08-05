import pandas as pd
import re

#
# Creates a new csv file by combining each year's txt file from the US social security database.
#

from glob import glob
lst = glob("ssn_files/*.txt")
dflist = []

for fn in lst:
    #print(fn)
    numlist = re.findall(r'\d+', fn)
    year = int(numlist[0])
    df = pd.read_csv(fn, sep=",", header=None)
    df.insert(loc=3, column='3', value=year) # inserts the year from the file name as a column
    #print(df.head(10))
    dflist = dflist + [df]

dfbig = pd.concat(dflist, axis=0, ignore_index=True)
dfbig = dfbig.set_axis(["Name", "Gender", "Count", "Year"], axis=1) # sets the order of the columns
print(dfbig.head()) 
dfbig.to_csv('ssn_files/all_years.csv', mode="w+", index=False) # exports a single csv file that can be more easily analyzed


