import pandas as pd

df = pd.read_csv("ssn_files/all_years.csv")
#print(df.head(10)) # To confirm the correct data is loading

by_name = df.sort_values('Name',ascending=True)

n = input("Enter a name to learn how many times it's been registered with Social Security since 1880.")
dfn = df.query('Name == @n')
sum_names = dfn["Count"].sum()
print(dfn)
print(n,"has been used", sum_names, "times.")

#by_count = df.sort_values('Count',ascending=True)
#print(by_count)