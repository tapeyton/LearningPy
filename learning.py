# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:37:21 2019

@author: tpeyton
"""

#THE BASICS - FOR AND WHILE LOOPS

for x in range (4):
        print (x)

# For a given range [3,24) that are multiples of 3

for x in range (3,24,3):
    print (x)
    
count = 2
while count < 10:
    print (count)
    count = count + 2
    
for x in range (10):
    if x % 2 == 0:
        continue
    print (x)
    
count = 2
while True:
    print (count)
    count = count + 2
    if count >= 6:
        break
    
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

# print out all even numbers from the numbers list in the same order they are received. Don't print any numbers that come after 237 in the sequence

for x in numbers:
    if x == 237:
        break
    if x % 2 == 0:
        print (x)




#JOINING AND MERGING

#Importing modules
import pandas as pd

#Creating first dataframe
raw_data = {
        'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}
df_a = pd.DataFrame(raw_data, columns = ['subject_id', 'first_name', 'last_name'])
df_a

#Creating second dataframe
raw_data = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}
df_b = pd.DataFrame(raw_data, columns = ['subject_id', 'first_name', 'last_name'])
df_b

#Creating third dataframe
raw_data = {
        'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}
df_n = pd.DataFrame(raw_data, columns = ['subject_id', 'test_id'])
df_n

#Joining the two dataframes along rows
df_new = pd.concat([df_a, df_b])
df_new

df_new.reset_index(drop=True, inplace=True)

#OR..........
pd.concat([df_a, df_b], axis = 0)

#Joining the two dataframes along columns
pd.concat([df_a, df_b], axis = 1)

#Merge two dataframes along the subject_id value
pd.merge(df_new, df_n, on = 'subject_id')

#Merge two dataframes with both the left and right dataframes using the subject_id key
pd.merge(df_new, df_n, left_on = 'subject_id', right_on = 'subject_id')

#Merge with outer join - this can be thought of as a UNION join. 
#Full outer join produces the set of all records in Table A and Table B, with matching records from both sides where available. If there is no match, the missing side will conain NaN.
pd.merge(df_a, df_b, on='subject_id', how='outer')

#Merge with inner join - this can be thought of as an INTERSECTION join.
#Inner join produces only the set of records that match in both Table A and Table B.
pd.merge(df_a, df_b, on='subject_id', how='inner')

#Merge with right join
pd.merge(df_a, df_b, on='subject_id', how='right')

#Merge with left join
pd.merge(df_a, df_b, on='subject_id', how='left')

#Merge based on indexes
pd.merge(df_a, df_b, right_index=True, left_index=True)



#INPLACE PARAMETER
url = 'http://bit.ly/uforeports'
ufo = pd.read_csv(url)

ufo.shape

ufo.head()

#dropping the City column
ufo.drop('City', axis=1).head()

#when ufo.head() is called upon again, the City column remains...
ufo.head()

#this is because the default "inplace" parameter is false, not true

#if, instead, we make inplace = True then the column will be deleted permanently because a new variable has been defined
ufo.drop('City', axis=1, inplace=True)
ufo.head()

# dropna with how='any' would drop any row with 'NaN'
ufo.dropna(how='any').shape

#but the underlying data has not been affected because inplace=False for .dropna()
ufo.shape
