#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 16:59:49 2020

@author: Shubham
"""

''' Pre processing '''
# =============================================================================
import pandas as pd
import numpy as np

#Plotting Packages
import seaborn as sns
import matplotlib.pyplot as plt
pip install plotnine
from plotnine import *

#kNN & Regression Packages
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.decomposition import PCA
from sklearn import linear_model
import statsmodels.api as sm

# Map visualisation Packages
import folium
from folium import plugins
from folium.plugins import HeatMap
from folium.plugins import MarkerCluster


houseDF = pd.read_csv ("kc_house_data.csv")
houseDF.describe()

# To convert the Date column into readable dates
houseDF['date'] = pd.to_datetime(houseDF.date)

# Checking for missing values
print (houseDF.isnull().sum())
print (houseDF.isnull().values.any())

houseDF.info()

houseDF.shape

# Checking for unique values in the columns
houseDF.id.unique()
houseDF.date.unique()
houseDF.price.unique()
houseDF.bedrooms.unique()
houseDF.bathrooms.unique() 
houseDF.floors.unique()
houseDF.waterfront.unique()
houseDF.view.unique()
houseDF.condition.unique()
houseDF.grade.unique()
houseDF.yr_renovated.unique()
houseDF.zipcode.unique()

# Changing the listing with 33 bedrooms to 3 bedrooms
for i in range (len(houseDF)):
    if (houseDF['bedrooms'][i] == 33) :
        houseDF ['bedrooms'][i] = 3
        
# Assigning mean value of bedrooms and bathrooms to listings with 0 bedrooms or 0 bathrooms
import statistics

avgBed = int(statistics.mean(houseDF['bedrooms']))        
avgBath =round (statistics.mean(houseDF['bathrooms']))

for i in range (len(houseDF)):
    if (houseDF ['bedrooms'][i] == 0):
        houseDF ['bedrooms'] [i] = avgBed
    if (houseDF ['bathrooms'][i] == 0):
        houseDF ['bathrooms'][i] = avgBath
        
copyDF = houseDF # For use later in regression models

# Making Categories for conditions ranging from 1 to 5
houseDF['CondCategory'] = pd.Series()
for i in range(len(houseDF)):
    if(houseDF['condition'][i] == 1):
        houseDF['CondCategory'][i] = 'Very Poor'
    elif(houseDF['condition'][i] == 2):
        houseDF['CondCategory'][i] = 'Poor'
    elif(houseDF['condition'][i] == 3):
        houseDF['CondCategory'][i] = 'Average'
    elif(houseDF['condition'][i] == 4):
        houseDF['CondCategory'][i] = 'Good'
    else:
        houseDF['CondCategory'][i] = 'Very Good'

houseDF['CondCategory'].describe()


#describing all the columns
for column in houseDF.columns:
    print('Column: ', column)
    print(houseDF[column].describe())
    
# Making a new column for price per square feet
houseDF ['PerSqftLiving'] = round ((houseDF['price']/ houseDF['sqft_living']),2)

# Changing waterfront to categorical data
def Waterfront(waterfront):
    if waterfront > 0:
        return 'Waterfront' 
    else:
        return 'Not Waterfront'
houseDF['Waterfront'] = houseDF['waterfront'].apply(lambda x:Waterfront(x))

# Zipcodes are further classified into sectors or bins to make grouping easier

def sector(zipcode):
    if zipcode <= 98028:
        return 'A (<= 98028)'
    elif zipcode>98028 and zipcode <= 98072:
        return 'B (>98028 & <=98072)'
    elif zipcode>98072 and zipcode<98122:
        return 'C(>98072 & <98122)'
    else:
        return 'D(>=98122)'

houseDF['Sector'] = houseDF['zipcode'].apply(lambda x:sector(x))

# A column is made categorizing listings on whether they were renovated or not
def renovation(yr_renovated):
    if yr_renovated > 0:
        return 'Renovated' 
    else:
        return 'Original'
houseDF['Renovation'] = houseDF['yr_renovated'].apply(lambda x:renovation(x))

# Drop Columns not put to use
houseDF = houseDF.drop(['date', 'sqft_living15', 'sqft_lot15' ], axis = 1)

for column in houseDF.columns:
    print('Column: ', column)
    print(houseDF[column].describe())

houseDF.shape

# =============================================================================
''''Visualisations''''
# =============================================================================
'''' housing Price distribution''''
# price is our target
#histogram for price distribution
plt.figure(figsize=(9,5))
histPrice = sns.distplot(houseDF['price'], bins=80,kde=False).set_title("Histogram for housing Price")
plt.xlabel('Price (in $)')
plt.ylabel('Frequency')
plt.grid()

#boxplot for price distribution
plt.figure(figsize = (8, 6))
pricebox = sns.boxplot(x='price', data=houseDF).set_title("Box plot for housing Price")
plt.xlabel('Price (in $)')
plt.xticks(rotation=45)

#QQ plot for price variable
from scipy import stats
normalProbPlot = stats.probplot(houseDF['price'], plot=plt)

#skewness and kurtosis parameters
print(houseDF['price'].describe())

print("Skewness: %f" % houseDF['price'].skew())
print("Kurtosis: %f" % houseDF['price'].kurt())


'''univariate analysis and plot histogram for numerical column''''

#bedrooms
plt.figure(figsize=(6,4))
sns.countplot(houseDF['bedrooms'])
print(houseDF['bedrooms'].describe())

#bathrooms
plt.figure(figsize=(12,6))
sns.countplot(houseDF['bathrooms'])
print(houseDF['bathrooms'].describe())

#sqft_living
sns.distplot(houseDF['sqft_living'], bins=30, kde=False);
print(houseDF['sqft_living'].describe())

#sqft_lot
sns.distplot(houseDF['sqft_lot'], bins=80, kde=False);
print(houseDF['sqft_lot'].describe())

#floors
sns.distplot(houseDF['floors'], kde=False);
print(houseDF['floors'].describe())

#grade
sns.distplot(houseDF['grade'], kde=False);
print(houseDF['grade'].describe())
houseDF['grade'].value_counts()

#waterfront
plt.figure(figsize=(4,4))
sns.countplot(houseDF['waterfront'])
houseDF['waterfront'].value_counts()

#view
plt.figure(figsize=(6,6))
sns.countplot(houseDF['view'])
houseDF['view'].value_counts()

#condition
plt.figure(figsize=(6,6))
sns.countplot(houseDF['CondCategory'])
houseDF['CondCategory'].value_counts()
#single categorical variable boxplot

#Sqft_basement 
sns.distplot(houseDF['sqft_basement'],bins=30, kde=False);
print(houseDF['sqft_basement'].describe())

#yr_renovated
sns.distplot(houseDF['yr_renovated'], bins=50, kde=False);
houseDF['yr_renovated'].value_counts()


''''bivariate analysis''''
#plot boxplot of some columns wrt to price

colGrade = 'grade'
data = pd.concat([houseDF['price'], houseDF[colGrade]], axis=1)
f, ax = plt.subplots(figsize=(8, 6))
fig = sns.boxplot(x=colGrade, y="price", data=data)

colBathrooms= 'bathrooms'
data = pd.concat([houseDF['price'], houseDF[colBathrooms]], axis=1)
f, ax = plt.subplots(figsize=(14, 6))
fig = sns.boxplot(x=colBathrooms, y="price", data=data)
plt.xticks(rotation=90)
houseDF['bathrooms'].value_counts()

colZipCode= 'zipcode'
data = pd.concat([houseDF['price'], houseDF[colZipCode]], axis=1)
f, ax = plt.subplots(figsize=(14, 6))
fig = sns.boxplot(x=colZipCode, y="price", data=data)
plt.xticks(rotation=90)
houseDF['zipcode'].value_counts()

colYrBuilt = 'yr_built'
data = pd.concat([houseDF['price'], houseDF[colYrBuilt]], axis=1)
f, ax = plt.subplots(figsize=(17, 6))
fig = sns.boxplot(x=colYrBuilt, y="price", data=data)
plt.xticks(rotation=90)
houseDF['yr_built'].value_counts()

colView = 'view'
data = pd.concat([houseDF['price'], houseDF[colView]], axis=1)
f, ax = plt.subplots(figsize=(7, 6))
fig = sns.boxplot(x=colView, y="price", data=data)
plt.xticks(rotation=90)
houseDF['view'].value_counts()


# Plots count of condition of a house
(ggplot(houseDF, aes('CondCategory', fill='CondCategory'))
 + geom_bar()
 + geom_text(
     aes(label='stat(count)'),
     stat='count',
     nudge_y=0.125,
     va='bottom'
 )
)
 
# Colormap of House Condition
(ggplot(houseDF)
 + aes(x='long', y='lat', color='CondCategory')
 + geom_point()
 + labs(title='Colormap of House Condition', x='Longitude', y='Latitude')
)

# Colormap of Sectors with PerSqftPrice
(ggplot(houseDF)
 + aes(x='long', y='lat', color='Sector', size = 'PerSqftLiving')
 + geom_point()
 + labs(title='Colormap of Sectors with Price/Sqft', x='Longitude', y='Latitude')
)

# Colormap of Price/Sqft
(ggplot(houseDF)
 + aes(x='long', y='lat', color='PerSqftLiving')
 + geom_point()
 + labs(title='Colormap of Price/Sqft', x='Longitude', y='Latitude')
)

# Colormap of Waterfront
(ggplot(houseDF)
 + aes(x='long', y='lat', color='Waterfront')
 + geom_point()
 + labs(title='Colormap of Waterfront', x='Longitude', y='Latitude')
 )

#Zipcode colormap of listing with Price/Sqft markers

(ggplot(houseDF)
 + aes(x='long', y='lat', color='zipcode', size = 'PerSqftLiving')
 + geom_point()
 + labs(title='Colormap of Zipcode', x='Longitude', y='Latitude')
 )

# Plot with Price/Sqft and Sectors
ggplot(houseDF, aes(x='PerSqftLiving', color='Sector')) + \
    geom_density()

# Colormap of House Renovation
(ggplot(houseDF)
 + aes(x='long', y='lat', color = 'Renovation')
 + geom_point()
 + labs(title='Colormap of House Renovation', x='Longitude', y='Latitude')
 )


#Bar chart for renovation

(ggplot(houseDF, aes('Renovation', fill='Renovation'))
 + geom_bar()
 + geom_text(
     aes(label='stat(count)'),
     stat='count',
     nudge_y=0.125,
     va='bottom'
 )
)

# Bar chart of bedrooms

def labels(from_, to_, step_):
    return pd.Series(np.arange(from_, to_ + step_, step_)).apply(lambda x: '{:,}'.format(x)).tolist()

def breaks(from_, to_, step_):
    return pd.Series(np.arange(from_, to_ + step_, step_)).tolist()

(ggplot(houseDF, aes('bedrooms', fill='bedrooms'))
 + geom_bar()
 + geom_text(
     aes(label='stat(count)'),
     stat='count',
     nudge_y=0.125,
     va='bottom'
 )
 +
    scale_x_continuous(
        limits = (1, 12),
        labels = labels(1, 12, 1),
        breaks = breaks(1, 12, 1)
    )
)
# =============================================================================
 '''' Scatter plots of variables with lat and long''''

#lat, long with sqft_living
houseDF.plot.scatter('long','lat',c='sqft_living',colormap='viridis', figsize=(10,10))

#lat,long with grade
houseDF.plot.scatter('long','lat',c='grade', colormap='viridis', figsize=(10,10))
#Or, where are the houses built with higher quality materials?

#lat, long with condition
houseDF.plot.scatter('long','lat',c='condition', colormap='viridis', figsize=(10,10))

# =============================================================================
'''' correlation ''''

#to view which columns are strongly correlated with price
print(houseDF.corr()['price'].sort_values(ascending=False))
    
#correlation matrix
correlation = houseDF.corr()
plt.figure(figsize=(16, 12))
heatmap = sns.heatmap(correlation,annot=True, cbar=True, linewidths=0, cmap="RdBu_r")
heatmap.set_ylim(20.0, 0)

#seperate heatmap for moderate to strong correlation
heatmap_df=correlation.drop(['PerSqftLiving','zipcode','id','long','lat','condition','yr_built','sqft_lot','yr_renovated','floors','waterfront','bedrooms','sqft_basement','view' ]).drop(['PerSqftLiving','zipcode','id','long','lat','condition','yr_built','sqft_lot','yr_renovated','floors','waterfront','bedrooms','sqft_basement','view' ],axis=1)
heatmap2=sns.heatmap(heatmap_df, annot=True, linewidths=0, cmap="RdBu_r")
heatmap2.set_ylim(5, 0)

#scatterplot for some of strong/weak correlation
sns.scatterplot(houseDF['sqft_living'], y=houseDF['price'])
sns.scatterplot(houseDF['grade'], y=houseDF['price'])
sns.scatterplot(houseDF['sqft_above'], y=houseDF['price'])
sns.scatterplot(houseDF['bathrooms'], y=houseDF['price'])

# =============================================================================
''''Interactive Map''''

map = folium.Map(location=[houseDF['lat'].mean(), houseDF['long'].mean()],
                        zoom_start=13)

mc = MarkerCluster()                        
for i in range (len(houseDF)):
    lat = houseDF.lat[i]
    long = houseDF.long[i]
    cond = houseDF.CondCategory[i]
    price = houseDF.PerSqftLiving[i]
    zipcode = houseDF.zipcode[i]
    totalprice = houseDF.price[i]
    tooltip = "Zipcode:{}<br> Total Price: {}<br> Click for more".format(zipcode, totalprice)
    popup_text = "Per Sqft Price: {}, Condition: {}".format(price,cond)
    popup = folium.Popup(popup_text, parse_html=True)
    mc.add_child(folium.Marker(location = [lat, long],tooltip = tooltip ,popup=popup))
    
map.add_child(mc)   
map
map.save('Conditonmap.html')

# =============================================================================
#------------------------------------------------------------------------------------------------------------        
        
"""
Logistic Regression Model 
"""

copyDF

#Adding logistic columns for if it was renovated or not (1 = renovated, 0 = not renovated)
for i in range(len(copyDF)):
    if(copyDF.loc[i,'yr_renovated'] > 0):
        copyDF.loc[i,'WasRenovated'] = 1
    else:
        copyDF.loc[i,'WasRenovated'] = 0

#only keeping columns we want
for colName in copyDF:
    print(colName)

regDF = copyDF[['WasRenovated','price','bedrooms','bathrooms','sqft_living','sqft_lot','floors','waterfront',
                'view','condition','grade','yr_built','zipcode']]

regDF.head()


#setting a seed for the same output
np.random.seed(3)
#couting the number of rows in our new dataframe
numberOfRows = len(regDF)
numberOfRows
#randomly generating indexes to select train & test data without bias
randomRows = np.random.permutation(numberOfRows)
randomRows
#establishing training & testing row indicies
eightypercentofdata = round(len(regDF)*0.8)

trainingRows = randomRows[0:eightypercentofdata]
testRows = randomRows[eightypercentofdata:]

#establishing training and test data
xTrain = regDF.iloc[trainingRows,1:]

yTrain = regDF.iloc[trainingRows,0]

xTest = regDF.iloc[testRows,1:]
yTest = regDF.iloc[testRows,0]


#creating linear regression model
LogReg = linear_model.LogisticRegression()

#fitting the model
LogReg.fit(xTrain,yTrain)

#predicting the remaining rows
model_prediction = LogReg.predict(xTest)
print(model_prediction)

#printing the coefficients
np.set_printoptions(suppress=True)
LogReg.coef_
LogReg.intercept_

#computing accuracy of the model
LogReg.score(xTest,yTest)

#3 hypothetical houses
House1 = [335680,3,1,1022,1562,1,0,0,4,7,1995,98053]
House2 = [556127,3,1.75,2304,3220,1,0,1,3,10,1967,98005]
House3 = [852118,2,2.75,4087,5062,2,1,4,4,7,1969,98118]

#stacking the data in a 2-D array
Predict_Houses = np.vstack((House1,House2,House3))

#predicting the probability that each of the above houses was renovated
LogReg.predict_proba(Predict_Houses)
# =============================================================================
"""
Linear Regression Model
"""

copyDF
#deleting columns that we don't want included in the model & saving the result to new dataframe
regHouseDF = copyDF.drop(['id', 'date','zipcode','lat','long','sqft_living15','sqft_lot15'],axis = 1)
regHouseDF.columns

#looking at the new shape of the regression data frame
regHouseDF.shape
regHouseDF.head()

#creating linear regression model
LinReg = linear_model.LinearRegression()

#setting a seed for the same output
np.random.seed(3)
#couting the number of rows in our new dataframe
numberOfRows = len(regHouseDF)
numberOfRows
#randomly generating indexes to select train & test data without bias
randomRows = np.random.permutation(numberOfRows)
randomRows
#establishing training & testing row indicies
eightypercentofdata = round(len(regHouseDF)*0.8)

trainingRows = randomRows[0:eightypercentofdata]
testRows = randomRows[eightypercentofdata:]

#establishing training and test data
xTrain = regHouseDF.iloc[trainingRows,1:]

yTrain = regHouseDF.iloc[trainingRows,0]

xTest = regHouseDF.iloc[testRows,1:]
yTest = regHouseDF.iloc[testRows,0]

#using statsmodels
LinReg = sm.OLS(yTrain,sm.add_constant(xTrain))
#fitting the model
model = LinReg.fit()
#model predictions
LinReg.predict(xTest,yTest)
#summary of the model
 
# =============================================================================
'''' kNN model of house condition ''''

import numpy as np

select = ['price', 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade', 'yr_built', 'zipcode', 'yr_renovated', 'PerSqftLiving']
selecthouseDF = houseDF.loc[:, select]
X_house = selecthouseDF.drop(['condition'], axis = 1)
X_house.shape
y_house = selecthouseDF ['condition']
y_house.shape

# A random permutation, to split the data randomly
np.random.seed(0)

#Randomize our the order of our data.
indices = np.random.permutation(len(houseDF))

# Select first 4000 rows of data to become our training set.
house_X_train = X_house.iloc[indices[:4000]]
house_y_train = y_house[indices[:4000]]

# 4000th from last row to end becomes test data set.
house_X_test  = X_house.iloc[indices[4000:]]
house_y_test  = y_house[indices[4000:]]

# Create and fit a nearest-neighbor classifier
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(10) 
knn.fit(house_X_train, house_y_train) 

prediction = knn.predict(house_X_test)
actual = house_y_test
difference = abs(prediction-actual)

print(accuracy_score(actual, prediction))
print(classification_report(actual, prediction))

# Correlation Matrix
from sklearn.decomposition import PCA
pca = PCA()
pca.fit(selecthouseDF)

pca.components_
pca.explained_variance_


corrMatrix = selecthouseDF.corr()

sns.heatmap(corrMatrix)
sns.heatmap(corrMatrix, annot=True)

# Testing vs Training Accuracy Graph

neighbors = np.arange(1,11) 
train_accuracy = np.empty(len(neighbors)) 
test_accuracy = np.empty(len(neighbors)) 
  
# Loop over K values 
for i, k in enumerate(neighbors): 
    knn = KNeighborsClassifier(n_neighbors=k) 
    knn.fit(house_X_train, house_y_train) 
      
    # Compute traning and test data accuracy 
    train_accuracy[i] = knn.score(house_X_train, house_y_train) 
    test_accuracy[i] = knn.score(house_X_test, house_y_test) 

plt.plot(neighbors, test_accuracy, label = 'Testing dataset Accuracy') 
plt.plot(neighbors, train_accuracy, label = 'Training dataset Accuracy') 
  
plt.legend() 
plt.xlabel('n_neighbors') 
plt.ylabel('Accuracy') 
plt.show() 
# =============================================================================
