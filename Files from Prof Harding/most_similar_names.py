import Levenshtein # word similarity metrics: pip install levenshtein
# https://rawgit.com/ztane/python-Levenshtein/master/docs/Levenshtein.html#Levenshtein-jaro_winkler
import pandas as pd

df = pd.read_csv("ssn_files/all_years.csv")
uniquenames = df.Name.unique()

# user input
name = "Tim" 

similarity_list_Lev = []
similarity_list_JW = []
most_similar = []

# use 2 different word distance metrics and combine result later
for un in uniquenames:
    similarity_JW = Levenshtein.jaro_winkler(name, un)
    similarity_list_JW.append([similarity_JW, un])
    similarity_Lev = Levenshtein.distance(name, un)
    similarity_list_Lev.append([similarity_Lev, un])

similarity_list_JW.sort(reverse=True)  # sort by first list elements i.e. by similarity, high to low
similarity_list_Lev.sort() # levenstein: higher numbers are less similar, so no reversing

print("Jaro-Winkler distance: Most similar to", name)
for sim, name in similarity_list_JW[1:11]:
    print(name, sim)
    most_similar.append(name)

print("Levenshtein distance: Most similar to", name)
for sim, name in similarity_list_Lev[1:11]:
    print(name, sim)
    if not name in most_similar: # only add if not already a jaro-winkler similar name
        most_similar.append(name)

# combined list
print(most_similar)
