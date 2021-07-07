import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# set to 1 to generate a new dataset
if 0: 
    df_all = pd.read_csv("ssn_files/all_years.csv")
    uniquenames = df_all.Name.unique()   # FYI: returns a numpy array!


    # for testing only(!): draw X random samples
    # suggestion: feed it a list with 8 sort of common names instead
    uniquenames = np.random.choice(uniquenames, 8)

    # Empty dataframe
    template = {'Name':pd.Series([], dtype='str'),
                'Gender':pd.Series([], dtype='str'),
                "Count":pd.Series([], dtype='str')}        
    df = pd.DataFrame(template) 


    for un in uniquenames:
        print(un, end=" ") # DEBUG print out current name, no linebreaks

        # make a subset (dataframe) of all rows where Name == un, 
        dfun = df_all[df_all["Name"] == un]

        genders = np.unique(dfun["Gender"].values)# get array of and get unique values

        for gender in genders: # Same name could be used for both genders!
            print(gender, end=", ")
            
            dfung = dfun[dfun["Gender"] == gender] # narrow further down by gender

            # Make empty list for count per year, default is nan, which means don't plot
            cpy = [np.nan] * (2020 - 1880 + 1) # count per year, [0] means 1880

            for i, r in dfung.iterrows(): # grab each rows and pull out count and year
                year = r["Year"]
                count = r["Count"]
                cpy[year-1880] = int(count)

            row = {"Name":un, "Gender":gender, "Count":cpy}
            df = df.append(row, ignore_index=True)

    df.to_pickle("count_over_time.pkl") # same in a pkl not a csv file b/c there are too many columns for csv!





df = pd.read_pickle("count_over_time.pkl")
plt.figure(figsize=(12,4)) # set aspect
for i, r in df.iterrows():
    v = r.values # all row values
    y = v[2] # [2] is list of counts over time with [0] for 1880
    x = range(1880, 2021)

    plt.plot(x, y, label=v[0]+", "+v[1])

plt.legend(fontsize=11)
plt.grid(True)
plt.xlim(1880,2020)
plt.show()

