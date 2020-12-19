import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from matplotlib import pyplot as plt
import seaborn as sns
import pickle
sc=StandardScaler()
lr=LinearRegression()
dtr=DecisionTreeRegressor()
le = preprocessing.LabelEncoder()

df = pd.read_csv(r"d_clean.csv")
'''
df.loc[df['Status'] =="Ready_to_move" , 'Status'] = 1.0              #0:work in progress
df.loc[df['Status'] =="Almost_ready" , 'Status'] = 0.0'''
df.Parking.fillna(0,inplace=True)
df.Bathroom.fillna(df.Bathroom.median(),inplace=True)
df.Furnishing.fillna('Unfurnished',inplace=True)
df.Type.fillna('Apartment',inplace=True)
df['Parking'].replace([39,114],2,inplace=True)
df['Parking'].replace([5,9,10],4,inplace=True)
d1=np.array(df[df.Area>5000].index)
df.drop(d1,inplace=True)
d2=np.array(df[df.BHK>6].index)
df.drop(d2,inplace=True)

'''
plt.subplot(2,2,1)
sns.countplot(df.Parking)
plt.grid(True)
plt.subplot(2,2,2)
sns.countplot(df.Furnishing)
plt.grid(True)
plt.subplot(2,2,3)
sns.countplot(df.Type)
plt.grid(True)
plt.subplot(2,2,4)
sns.countplot(df.Transaction)
plt.grid(True)
plt.show()
'''
'''
x1=df[['Area']]
x2=df[['BHK']]
x3=df[['Furnishing']]
x4=df[['Status']]
x5=df[['Transaction']]
x6=df[['Parking']]
y=df[['Price']]
'''

'''
df.drop('Per_Sqft',axis=1,inplace=True)
df.drop('Locality',axis=1,inplace=True)
df.loc[df['Furnishing'] =="Unfurnished" , 'Furnishing'] = 1
df.loc[df['Furnishing'] =="Semi-Furnished" , 'Furnishing'] = 2
df.loc[df['Furnishing'] =="Furnished" , 'Furnishing'] = 3
df.loc[df['Status'] =="Ready_to_move" , 'Status'] = 1
df.loc[df['Status'] =="Almost_ready" , 'Status'] = 2
df.loc[df['Transaction'] =="Resale" , 'Transaction'] = 1
df.loc[df['Transaction'] =="New_Property" , 'Transaction'] = 2
df.loc[df['Type'] =="Builder_Floor" , 'Type'] = 1
df.loc[df['Type'] =="Apartment" , 'Type'] = 2
print(df.dtypes)
df.to_csv('new.csv',index=False)
'''
'''
plt.subplot(2,3,1)
plt.scatter(x1,y)
plt.subplot(2,3,2)
plt.scatter(x2,y)
plt.subplot(2,3,3)
plt.scatter(x3,y)
plt.subplot(2,3,4)
plt.scatter(x4,y)
plt.subplot(2,3,5)
plt.scatter(x5,y)
plt.subplot(2,3,6)
plt.scatter(x6,y)
plt.show()
sns.heatmap(df.corr())
plt.show()
'''
x = df[['Price']]
y = df.drop('Price',axis=1)
'''
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 42)
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)
'''

dtr.fit(x,y)
#budget = int(input("Budget for house: "))
#years = int(input("mortgage loan term: "))
#rate = int(input("interest rate: "))
#principal = int(input("Down Payment: "))

#a = (budget*years*12) 
#b = a + principal
#c = b - ((b*rate*12)/100)
#new=[[float(c)]]

"""

pred = dtr.predict(new)
print("Expected Area :  ",pred[0][0])
print("Expected BHK :  ",pred[0][1])
print("Expected Bathroom :  ",pred[0][2])
print("Expected Furnishing :  ",pred[0][3])
print("Expected Parking :  ",pred[0][4])
print("Expected Status :  ",pred[0][5])
print("Expected Transaction :  ",pred[0][5])
print("Expected Type :  ",pred[0][6])
print("\n")
print("*NOTE:: more float values close to a whole number, more is the chances towards that whole value \n")
"""

# Saving model to disk
pickle.dump(dtr, open('model.pkl','wb'))

#lLoading model to compare the results
model = pickle.load(open('model.pkl','rb'))