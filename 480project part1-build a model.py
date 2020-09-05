import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
#open the file for further use
df = pd.read_csv('xAPI-Edu-Data.csv')
#drop those columns that don't have much impact on the grade
df.drop(['NationalITy', 'PlaceofBirth','StageID','Semester','Class'], axis=1, inplace=True)
#create linear regression object
mlr= LinearRegression()
#encode categorical variables as binary variables
df.loc[df['gender'] == 'F', ['gender']] = 0
df.loc[df['gender'] == 'M', ['gender']] = 1

df.loc[df['Relation'] == 'Father', ['Relation']] = 0
df.loc[df['Relation'] == 'Mum', ['Relation']] = 1

df.loc[df['ParentAnsweringSurvey'] == 'Yes', ['ParentAnsweringSurvey']] = 0
df.loc[df['ParentAnsweringSurvey'] == 'No', ['ParentAnsweringSurvey']] = 1

df.loc[df['ParentschoolSatisfaction'] == 'Good', ['ParentschoolSatisfaction']] = 0
df.loc[df['ParentschoolSatisfaction'] == 'Bad', ['ParentschoolSatisfaction']] = 1

df.loc[df['StudentAbsenceDays'] == 'Under-7', ['StudentAbsenceDays']] = 0
df.loc[df['StudentAbsenceDays'] == 'Above-7', ['StudentAbsenceDays']] = 1
#get the number of grades
for index, row in df.iterrows():
  grade = row['GradeID']
  gradeParts = grade.split('-')
  gradeNum = int(gradeParts[1])
  df.loc[index, ['GradeID']] = gradeNum
#data of raisedhands cleaning
grouped1 = df.groupby(['raisedhands'], as_index=False)
gpedHands = grouped1.mean()
gpedHands['GradeID'] = gpedHands['GradeID'].round()
#plot 1st scatter of raisedhands
plt.subplot(1,3,1)
plt.scatter(gpedHands['raisedhands'], gpedHands['GradeID'], color='red')
plt.title('raisedhands Vs GradeID', fontsize=14)
plt.xlabel('raisedhands', fontsize=14)
plt.ylabel('GradeID', fontsize=14)
plt.grid(True)
plt.show()
#data of VisITedResources cleaning
grouped2 = df.groupby(['VisITedResources'], as_index=False)
gpedvisit = grouped2.mean()
gpedvisit['GradeID'] = gpedvisit['GradeID'].round()
#plot 2nd scatter of VisITedResources
plt.subplot(1,3,2)
plt.scatter(gpedvisit['VisITedResources'], gpedvisit['GradeID'], color='red')
plt.title('VisITedResources Vs GradeID', fontsize=14)
plt.xlabel('VisITedResources', fontsize=14)
plt.ylabel('GradeID', fontsize=14)
plt.grid(True)
plt.show()
#data of AnnouncementsView cleaning
grouped3 = df.groupby(['AnnouncementsView'], as_index=False)
gpedview = grouped3.mean()
gpedview['GradeID'] = gpedvisit['GradeID'].round()
#plot 3rd scatter of AnnouncementsView
plt.subplot(1,3,3)
plt.scatter(gpedview['AnnouncementsView'], gpedview['GradeID'], color='red')
plt.title('AnnouncementsView Vs GradeID', fontsize=14)
plt.xlabel('AnnouncementsView', fontsize=14)
plt.ylabel('GradeID', fontsize=14)
plt.grid(True)
plt.show()
#fit a multiple linear regression
lmModel = mlr.fit(df[['gender','Discussion', 'Relation', 'raisedhands', 'VisITedResources', 
            'AnnouncementsView', 'ParentAnsweringSurvey', 
            'ParentschoolSatisfaction', 'StudentAbsenceDays']], df['GradeID'])
#get the intercept and coefficient of the linear model


print('Intercept: \n', mlr.intercept_)
print('Coefficients: \n', mlr.coef_)