import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# write your code here
# After all the libraries imports write the following line of code
# pd.set_option('display.max_columns', 8)
# Read the CSV files with datasets
general = pd.read_csv('general.csv')
prenatal = pd.read_csv('prenatal.csv')
sports = pd.read_csv('sports.csv')
# Change the column names. The column names of the sports and the prenatal
# tables must match the column names of the general table
prenatal = prenatal.rename(columns={'HOSPITAL':'hospital', 'Sex':'gender'})
sports = sports.rename(columns={'Hospital':'hospital', 'Male/female':'gender'})
# Merge the data frames into one. Use the ignore_index = True parameter
# and the following order: general, prenatal, sports
df = pd.concat([general, prenatal, sports], ignore_index = True)
# Delete the Unnamed: 0 column
df = df.drop(columns={'Unnamed: 0'})
# Delete all the empty rows
df = df.dropna(how='all')
# Correct all the gender column values to f and m respectively
df['gender'] = df['gender'].map({'female': 'f', 'male': 'm', 'woman': 'f', 'man': 'm'}, na_action='ignore')
# Replace the NaN values in the gender column of the prenatal hospital with f
df['gender'] = df['gender'].fillna('f')
# Replace the NaN values in the bmi, diagnosis, blood_test, ecg, ultrasound, mri,
# xray, children, months columns with zeros
c = ['bmi', 'diagnosis', 'blood_test', 'ecg', 'ultrasound', 'mri', 'xray', 'children', 'months']
df[c] = df[c].fillna(0)
# Print shape of the resulting data frame
# print(df.shape)
# Print random 20 rows of the resulting data frame. For the reproducible output set random_state=30
# print(df.sample(n=5, random_state=30))
# print(df.index)
# Answer the following questions and output the answers in the specified format.

# 1. Which hospital has the highest number of patients?
# hospitals = df.hospital.unique()
# print(len(hospitals))
# print(hospitals)
# print(df.hospital.value_counts().general)
# df.groupby('hospital').count()
# print(df.groupby('hospital').count())
# stat = dict(df.groupby('hospital').count().gender)
# hospitals = list(stat.keys())
# patients = list(stat.values())
stat = dict(df.hospital.value_counts())
# print(df.hospital.value_counts().max())
# print(max(patients))
# print(patients.index(max(patients)))
# print(hospitals[patients.index(max(patients))])
# answer_1 = hospitals[patients.index(max(patients))]
pivot = df.hospital.value_counts()
answer_1 = pivot[pivot == pivot.max()].index[0]
# 2. What share of the patients in the general hospital suffers from stomach-related issues? Round the
# result to the third decimal place.
# patients_general = (stat['general'])
patients_general = pivot.general
# print(df.columns.values)
# hospital_general = df.loc[df['hospital'] == 'general']
# print(hospital_general)
general_stomach = df.loc[(df['hospital'] == 'general') & (df['diagnosis'] == 'stomach')].shape[0]
answer_2 = round(general_stomach / patients_general, 3)
# print(answer_2)

# 3. What share of the patients in the sports hospital suffers from dislocation-related issues?
patients_sports = (stat['sports'])
sports_dislocation = df.loc[(df['hospital'] == 'sports') & (df['diagnosis'] == 'dislocation')].shape[0]
answer_3 = round(sports_dislocation / patients_sports, 3)
# Round the result to the third decimal place.

# 4. What is the difference in the median ages of the patients in the general and sports hospitals?
general_median_age = df.loc[(df['hospital'] == 'general')].age.median()
sports_median_age = df.loc[(df['hospital'] == 'sports')].age.median()
answer_4 = int(abs(general_median_age - sports_median_age))

# 5. After data processing at the previous stages, the blood_test column has three values:
# t= a blood test was taken, f= a blood test wasn't taken, and 0= there is no information.'
# In which hospital the blood test was taken the most often (there is the biggest number of t
# in the blood_test column among all the hospitals)? How many blood tests were taken?
blood_test_taken = df.loc[df['blood_test'] == 't']
blood_stat = dict(blood_test_taken.groupby('hospital').count().gender)
hospitals = list(blood_stat.keys())
blood_stat_number = list(blood_stat.values())

# print(max(patients))
# print(patients.index(max(patients)))
# print(hospitals[patients.index(max(patients))])
answer_52 = max(blood_stat_number)
answer_51 = hospitals[blood_stat_number.index(answer_52)]

# print(f'''The answer to the 1st question is {answer_1}
# The answer to the 2nd question is {answer_2}
# The answer to the 3rd question is {answer_3}
# The answer to the 4th question is {answer_4}
# The answer to the 5th question is {answer_51}, {answer_52} blood tests''')

# Answer questions 1-3. Output the answers in the specified format. The answers to the first
# two questions should be formatted as in the examples. No special form is required to answer
# the third question

# 1. What is the most common age of a patient among all hospitals? Plot a histogram and choose one
# of the following age ranges: 0-15, 15-35, 35-55, 55-70, or 70-80
# print(df.head())
# print(df.hospital.unique())
# print(df.loc[df.hospital=='sports'].head())
# print(df.columns)
df.plot(y=['age'], kind='hist', bins=[0,15,35,55,70,80])
plt.show()
answer_91 = '15-35'
# 2. What is the most common diagnosis among patients in all hospitals? Create a pie chart
# print(df.diagnosis.value_counts())
df.diagnosis.value_counts().plot(kind='pie')
plt.show()
answer_92 = 'pregnancy'
# 3. Build a violin plot of height distribution by hospitals. Try to answer the questions. What is the main reason
# for the gap in values? Why there are two peaks, which correspond to the relatively small and big values?
# No special form is required to answer this question
# There is a comprehensive explanation of violin plots by Eryk Lewinson.
ax = sns.violinplot(x=df['hospital'], y=df['height'])
plt.show()
answer_93 = 'gender'
print(f'''The answer to the 1st question: {answer_91}
The answer to the 2nd question: {answer_92}
The answer to the 3rd question: It's because {answer_93}''')