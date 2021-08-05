

import pandas as pd

df = pd.read_csv("ssn_files/all_years.csv")
#print(df.head(10)) # To confirm the correct data is loading

'''
n = input("Enter a name to learn how many times it's been registered with Social Security since 1880.")
dfn = df.query('Name == @n')
sum_names = dfn["Count"].sum()
print(dfn)
print(n,"has been used", sum_names, "times.")
'''

#find unique names values
uniquenames = df.Name.unique()

#sort values alpha
uniquenames.sort()

#display sorted values
print(uniquenames)

dfnewlist = []

for x in uniquenames:
    #make a new dataframe
    #insert unique name as column 1
    #insert sum of name count from df
    dfnewlist = dfn["Count"].sum()
    

#First, we need to make a new dataframe that shows the sum of the names and not the years.
#Second, we can sort the list and reset the index

#most_exp = df.sort_values(by="Price", ascending=False)
#most_exp.reset_index(drop=True, inplace=True) # reset index numbers to start with 0 at top




#by_count = df.sort_values('Count',ascending=True)
#print(by_count)