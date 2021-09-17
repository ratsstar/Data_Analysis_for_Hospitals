import numpy as np
import pandas as pd

# write your code here
# After all the libraries imports write the following line of code
pd.set_option('display.max_columns', 8)
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
print(df.shape)
# Print random 20 rows of the resulting data frame. For the reproducible output set random_state=30
print(df.sample(n=20, random_state=30))
# print(df.index)