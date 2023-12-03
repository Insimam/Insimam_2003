import pandas as pd# To read the dataset
import numpy as np# numerical python 
import matplotlib.pyplot as plt
%matplotlib inline#plot the graph
import seaborn as sns# plot the Graph to grafical 
import warnings
warnings.filterwarnings("ignore")

ckd_data= pd.read_csv('CKD PRO1.csv')
print(ckd_data)

ckd_data.info()

#check null values of the dataset
ckd_data.isnull().sum()

from sklearn.model_selection import train_test_split
x = ckd_data.iloc[:,ckd_data.columns!='classification'] #data
y = ckd_data.iloc[:,ckd_data.columns=='classification'] #Outcome

xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=0.2)

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
model.fit(xtrain,ytrain.values.ravel()) #To train the algorithm 

from sklearn.metrics import accuracy_score
acc=accuracy_score(predict_output,ytest)
print('The accuracy score is:',acc)

#separate numerical and categorical columns
def separate_numerical_categorical_columns(df):
    numerical_cols = []
    categorical_cols = []
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            numerical_cols.append(col)
        else:
            categorical_cols.append(col)
    return numerical_cols, categorical_cols

#get separate columns
numerical_cols, categorical_cols = separate_numerical_categorical_columns(ckd_data)

# print the results
print('Numerical columns:', numerical_cols)
print('Categorical columns:', categorical_cols)

#check summary statistics for numerical columns
ckd_data.describe()

import seaborn as sns
#check distribution of numerical columns by plotting histogram for numerical columns
for col in numerical_cols:
 	plt.figure()
 	sns.histplot(ckd_data[col])
 	plt.xlabel(col)
 	plt.ylabel('No Of Persons')
	plt.show()

corr = ckd_data.corr()

# Extract the correlations between independent variables and the dependent variable
correlation_with_dependent = corr['classification']

# Sort the correlations in descending order
sorted_correlations = correlation_with_dependent.abs().sort_values(ascending=False)

# Display the attributes in descending order of correlation with the dependent variable
for attribute in sorted_correlations.index:
    correlation_percent = sorted_correlations[attribute] * 100
    print(f'{attribute} and dependent variable = {correlation_percent:.2f}%')
in_ckd_data = ckd_data.drop(columns=['classification'])
print(in_ckd_data)
out_ckd_data = ckd_data['classification']
print(out_ckd_data)

from sklearn.tree import DecisionTreeClassifier
data_model = DecisionTreeClassifier()
data_model.fit(in_ckd_data,out_ckd_data)

data_model.predict([[62,2.7,373,1.8,9.6,5,134]])

import pickle
with open ('Data_model_pkl','wb') as file:
    pickle.dump(model,file)