# -*- coding: utf-8 -*-
"""End to End Toy Project

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YaiknrwEliPGgrfYJ3lxL7igcopESSyf
"""

import pandas as pd
import numpy as np

df = pd.read_csv('/content/drive/MyDrive/100 days of ML by campusX/placement.csv')

# above dataset is about placement of students based on iq and cgpa factor

df.head()

# only 3 columns are of use....unnamed column can be removed through pre processing

df.shape

df.info()

#float can be converted to int for iq, placement represents boolean values

# Steps to be used

# 0. Preprocess + EDA + Feature Selection
# 1. Extract input and output cols
# 2. Scale the values
# 3. Train test split
# 4. Train the model
# 5. Evaluate the model/model selection
# 6. Deploy the model

df = df.iloc[:,1:]
# all rows (:) and all columns starting from (index 1) to the last(1:)

df

import matplotlib.pyplot as plt

plt.scatter(df['cgpa'],df['iq'],c=df['placement'])
# CGPA-->x-axis, IQ-->y-axis,color-coded points based on values in placement

#enhanced version of scatterplot
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
scatter = plt.scatter(df['cgpa'], df['iq'], c=df['placement'], cmap='viridis', alpha=0.7)
plt.colorbar(scatter, label='Placement')
plt.xlabel('CGPA')
plt.ylabel('IQ')
plt.title('Scatter Plot of CGPA vs IQ Colored by Placement')
plt.show()

X = df.iloc[:,0:2]
y = df.iloc[:,-1]
#cgpa,iq--> independent variable, placement--> dependent

X

#another way to represent to have more power over columns
X = df[['cgpa', 'iq']]
y = df['placement']

X

y

y.shape # 1D tensor

from sklearn.model_selection import train_test_split
#X: Features (input data), y: Target variable (output data)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.1)
# 10% of the data will go into test set, and 90% into training set

X_train

X_test

y_train

from sklearn.preprocessing import StandardScaler
# standardize features

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train) #z-score normalization--> subtracting mean-->dividing by standard deviation

X_train

X_test = scaler.transform(X_test)

X_test

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()

# model training
clf.fit(X_train,y_train)

y_pred = clf.predict(X_test)

y_test

from sklearn.metrics import accuracy_score

accuracy_score(y_test,y_pred) # accuracy= 90% predicted correct, 10% wrong

from mlxtend.plotting import plot_decision_regions # visualize decision boundaries of a classifier in 2D space

plot_decision_regions(X_train, y_train.values, clf=clf, legend=2)

import pickle

pickle.dump(clf,open('model.pkl','wb'))# save trained machine learning model (clf) to a file