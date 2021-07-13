import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("ssn_files/all_years.csv")
#print(df.head(10)) # To confirm the correct data is loading

'''
n = input("Enter a name to learn how many times it's been registered with Social Security since 1880.")
dfn = df.query('Name == @n')
sum_names = dfn["Count"].sum()
print(dfn)
print(n,"has been used", sum_names, "times.")
'''

# find unique names values
uniquenames = df.Name.unique()   # FYI: returns a numpy array!


# for testing only(!): draw X random samples
#uniquenames = np.random.choice(uniquenames, 1000)
# Once this works for you, comment this out to run it for all names

# sort values alpha
uniquenames.sort()   

# display sorted values
print(uniquenames)


def make_unique_name_df(uniquenames, df):
    '''returns a df with stats about unique names'''
    uniquenames_stats = []
    for un in uniquenames:
        print(un, end=" ") # DEBUG print out current name, no linebreaks

        # make a subset (dataframe) of all rows where Name == un, 
        dfun = df[df["Name"] == un]

        genders = np.unique(dfun["Gender"].values)# get array of and get unique values
        #if len(genders) == 2:
        #    print("***")

        for gender in genders: # Same name could be used for both genders!
            print(gender, end=", ")

            dfung = dfun[dfun["Gender"] == gender] # narrow further down by gender

            # sum() the Count column
            count_sum = dfung["Count"].sum()
        
            # Get some year-related stats: when seen first and last, peaked (most often) in which year 
            first = dfung["Year"].min()  # smallest = earliest year
            last = dfung["Year"].max()
            row_when_largest = dfung.nlargest(1, "Count")  # Datframe (just 1 row) with the 1 largest year (could be >1) 
            largest_Series = row_when_largest["Year"] # Series (really just a single cell ...)
            largest = largest_Series.values[0] # value of that one (first) cell

            # Note on Peak: as this uses absolute numbers, this heavily favours recent years! Ex:  Adam might have been 1% of all
            # people in 1880 but that's only 5000 people, in 2020 its 8000 (so it peaks in 2020) but it's only 0.1% of all people in 2020

            # Could also extract a histogram (maybe bin at 10 years chunks)
            # https://numpy.org/doc/stable/reference/generated/numpy.histogram.html

            # append list of properties for this name uniquenames_stats
            uniquenames_stats.append([un, count_sum, gender, first, last, largest])
    print("\n", "Done!")

    # Make datarame from list and define column names
    df_name_stats = pd.DataFrame(uniquenames_stats, columns=["Name", "Count", "Gender", "First", "Last", "Peak"])
    #print(df_name_stats.head())

    return df_name_stats


# run  this only if you want to create a new df! 
#df_name_stats = make_unique_name_df(uniquenames, df)
#df_name_stats.to_csv("name_stats.csv", index=False)


# Once you have created your df, comment out the above 2 lines!
df_name_stats = pd.read_csv("name_stats.csv")

df_name_stats.sort_values(by="Count", inplace=True, ascending=False) # sort internally by Count, descending
df_name_stats.reset_index(drop=True, inplace=True) # re-index
print(df_name_stats.head(20))


# Which names are both genders
name_counts = df_name_stats["Name"].value_counts() # Note: Name is used as index here!
both_genders_Series = name_counts[ name_counts == 2]
both_genders = list(both_genders_Series.index) # get the index names for the both gender cases and make a list
df_both_genders = df_name_stats[df_name_stats['Name'].isin(both_genders)] # grab rows where name is in both_gender list
df_both_genders.head()


# Some plots
df = df_name_stats.loc[0:19] # pull out top 20 (by Count)   

df.plot.bar(x="Name", y="Count", rot=90) # rotate labels
#plt.show()

# this is a bit silly - should just plot a single from-to bar ...
df.plot.bar(x="Name", y=["First", "Last"], ylim=[1880, 2024], rot=90) # limit y 
#plt.show()

# make a new Duration column
duration = df_name_stats["Last"] - df_name_stats["First"]
df.insert(5, "Duration", duration)
#df_name_stats.sort_values(by="Duration", inplace=True, ascending=True) # sort internally by Duration, ascending
#df_name_stats.reset_index(drop=True, inplace=True) # re-index
print(df.head(10))


# which names only lasted for less than X years
df_short = df[df["Duration"] < 120]
print("This is DF short:")
print(df_short.head())




print()

'''
# Some more ideas:
# - are there names that fade in a out over the years, i.e. which have 1 onre more substatial gaps?
# - given a name, try to devop a list of similar names (levinsten or hamming distance: https://rawgit.com/ztane/python-Levenshtein/master/docs/Levenshtein.html#Levenshtein-distance
# - plot popularity as swarm plot or violin plot https://seaborn.pydata.org/examples/index.html


import Levenshtein # word similarity metrics: pip install levenshtein
# https://rawgit.com/ztane/python-Levenshtein/master/docs/Levenshtein.html#Levenshtein-jaro_winkler
print(Levenshtein.jaro_winkler("Annelise", "Amalia")
'''