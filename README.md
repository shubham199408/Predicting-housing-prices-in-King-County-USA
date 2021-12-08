#### Predicting-housing-prices-in-King-County-USA

**Overview**

The dataset that was used for this project consists of sales data between May 2014 and May 2015 in King County, Washington, which includes the 18th most populous city in the US, Seattle. I sourced this data set from the website Kaggle, which focuses on data science learning, and houses a vast library of datasets across numerous industries. This dataset was chosen due its size, number of numerical and categorical variables, relative cleanliness, completeness and ease of interpretation. It is a CSV file that contains 21,614 rows (21,613 observation & 1 header row), and 21 columns. The table below summarizes the columns, and our interpretation of them

![Picture1](https://user-images.githubusercontent.com/95050679/144138509-415f7ed8-8015-4e70-a291-25a8bc984179.png)

In this analysis, I used several Python packages/techniques including, but not limited to: Pandas, NumPy, Matplotlib and Sci-kit Learn, which will all be highlighted in the following sections of this report, and can be viewed in the Python code for the project. Ultimately, My main objective is to understand the trend in housing prices for King County during this time period; along with what factors have the largest influence on price.


**Data Cleaning/Pre-Processing**

1.	After the data is loaded, the date column has been parsed through the datetime package to make it readable in pandas. The whole data is then checked for missing values and was found that were not any.

2.	Upon describing each column, there were some irregularities in the 'bedrooms' column where one listing had 33 bedrooms. Similarly there were a few listings with 0 bedrooms but the house itself was on multiple floors. Analysis of the 'bathrooms' column yielded similar irregularities with some listings having 0 bathrooms. 

3.	To resolve the above, the listing with 33 bedrooms was replaced with 3 bedrooms and listings with 0 in bedrooms and bathrooms columns were assigned the mean value of their respective columns. 

4.	Upon inspection of the zip codes column, there were 70 unique zip codes paired with the listings. To further simplify visual analysis, we break down the zip codes into 4 different sectors named A through D and the assignment is done under a new column named "Sector".
a.	Sector A contains zip codes <= 98028
b.	Sector B contains zip codes >98028 & <=98072
c.	Sector C contains zip codes >98072 & <98122
d.	Sector D contains zip codes >=98122.

5.	Yr_renovated column contains the year in which houses have been renovated or 0 if they were still in their original state. A new column named "Renovation" categorised listings into Renovated or Original based on whether or not they have been renovated

6.	In the initial data, condition of the listing was graded 1 - 5 and listings were further categorised under a new column "CondCategory", based on the below
a.	5 - Very Good
b.	4 - Good
c.	3 - Average
d.	2 - Poor
e.	1 - Very Poor

7.	Value of price per square foot of living space is obtained by dividing the columns "price" with "sqft_living". These values are stored in a new column PerSqftLiving.


**Housing Price Distribution**

The target of this analysis is the price of the houses. Let’s take a look at the histogram below.

![Picture2](https://user-images.githubusercontent.com/95050679/144139483-4cb105d3-9dfb-43a5-a008-e4e5ba6fdd29.png)

From the histogram of price distribution, we can infer that frequency is higher for houses within price range $300000-$500000. Price distribution is highly right-skewed and shows a normal distribution with a long tail to the right. 
 
A box plot is a graphical representation of 5-point statistics to help us understand the spread and centrality of data. Below are the key points that we can see in a box plot:
- Minimum: minimum value in the data set
- Maximum: maximum value in the data set
- Median: the “middle” value when the data set is sorted in ascending order
- First quartile: it indicates 25% of the data when the data set is sorted in ascending order
- Third quartile: it indicates 75% of the data when the data set is sorted in ascending order

![Picture3](https://user-images.githubusercontent.com/95050679/144139734-d8b39626-1789-42bc-a15a-abf002cc8be9.png)

We can infer from above figure that the most expensive house cost around $7.7 million and the data for price is highly right skewed. These outliers of high value cannot be removed from the data set, as they are not irregularities but examples of the luxury market in the region. Outliers are evident to be above ~12,00,000$.

The qq-plot of price as shown below, determines the distribution of price to be highly right skewed. Since the plot does not fit into a straight line, we can say that the price distribution is not normal.

![image](https://user-images.githubusercontent.com/95050679/144329365-b6c5483c-5322-41f1-a1b2-1d29ef31e6dd.png)

Let’s take a look at the skewness and kurtosis in numbers as shown below. 

![image](https://user-images.githubusercontent.com/95050679/144329431-cd077b5e-1b2b-45b6-87fd-a07a52eb8811.png)

The skewness is 4.024069 and kurtosis is 34.585540 which display values greater than zero. Thus, we conclude that the price distribution is right skewed. Also, the most expensive house cost $7.7 million and the median house price $450,000.


**EDA visualizations and insights**

Exploratory data analysis refers to the process of performing initial investigations on data to discover patterns, test conclusions using summary statistics and graphical representations. The dataset comprises 21613 rows and 22 columns.

Let’s do some univariate data distribution and plot a histogram for the numerical column of the data set.

**Bedrooms**

If we look at the pattern of the bedrooms as seen below, the median number of bedrooms is only 3. A majority of the region’s houses have 3 or 4 bedrooms. Examining the describe function for bedrooms, a house with max. 11 bedrooms appears to exist.

![image](https://user-images.githubusercontent.com/95050679/144329664-6583c4a3-0bb4-401b-a839-e27c16673be3.png)

![image](https://user-images.githubusercontent.com/95050679/144329703-925cb7a0-52b6-4003-82f0-de89a52540b8.png)


**Bathrooms:**

The histogram of bathrooms as seen below, approximates to a normal distribution. In this case we have a distribution which is close to normal because the tail is not very long. The median bathrooms is 2.25 and the average is 2.1. The values for bathrooms are unusual because it is possible to have half- and quarter-bathrooms.

![image](https://user-images.githubusercontent.com/95050679/144329760-296ccccd-6c93-441b-bd2b-6f144a23ccb0.png)

![image](https://user-images.githubusercontent.com/95050679/144329773-8d6fee20-266c-4a6c-8c26-96ea33f58b02.png)


**Sqft_living and sqft_lot:**

The sqft living characteristics provide the house's total living area in square feet. The median is 1,910 square feet and the largest property has an area of 13,540 square feet. Figure below shows the histogram of values which is a normal distribution with a long tail, as we might expect.

![image](https://user-images.githubusercontent.com/95050679/144329997-24eed0e2-803b-420a-858a-2b58a57f32ad.png)

The sqft lot feature gives the total area of the plot that includes a property's garden and grounds. Unlike the total area of the living space, the area of the plot is extremely heavily skewed. A histogram of the values is shown below, but because of the very long tail, the histogram is curtailed at 50,000 square feet. The median value is 7,619 square feet and the mean is 15,107.4 square feet.


![image](https://user-images.githubusercontent.com/95050679/144330068-c44287b7-f22a-4859-9094-b12409fa5230.png)

**Floors:**

The number of floors in properties can be half values (e.g., 1.5) most likely due to the Mezzanine floors. The median value is 1.5 floors. 10,679 houses consist of only one floor, 8,241 houses have two floors, and 1,910 houses consist of one and a half floor. The floor feature is right-skewed, with a huge portion of the houses having no basement and there are exceptional houses with 3.5 floors.

![image](https://user-images.githubusercontent.com/95050679/144330181-6e4e3ae5-5ff9-4c8f-a32e-d21a946fb0a3.png)


**Grade:**

Grade is the building grade which represents the construction quality. From the histogram below, grades vary from grade 1 to 13 where 1-3 indicate short of construction and design, 7 indicates standard level of construction and design which is the highest in this data with count of 8981 and, 11-13 indicate a high level of construction and design quality.

![image](https://user-images.githubusercontent.com/95050679/144330270-27c5c778-5236-455b-b655-3557e2e9ad8f.png)

**Waterfront**

The waterfront records a 0 if the house has no waterfront view, and 1 if the house has a view to a waterfront. Looking at the histogram and the describe feature on this attribute, we've got 21,449 houses that don't have a waterfront view and only 163 have a waterfront view.

![image](https://user-images.githubusercontent.com/95050679/144330374-65963c32-899c-46ce-8296-bcd8b48721ad.png)


**View**

It is an indicator of how fine the view from the property is. From the histogram below, view has values from 0 to 4 and the vast majority of houses 19489(90.2 per cent) have a value of 0 with view of 4 being the lowest 319.

![image](https://user-images.githubusercontent.com/95050679/144330404-b766698a-0252-4533-8c3f-295a6c9cb164.png)


**Condition:**

This feature represents the number of properties with different condition which ranges from 1 to 5 with 1 being “very poor” and 5 being “Very Good”. From the histogram of condition as shown in figure below, we can infer that we have the highest number of properties i.e., 14031 with average condition.

![image](https://user-images.githubusercontent.com/95050679/144330434-3d59c515-5c81-40ea-8692-e845d1c256d5.png)

**Sqft_basement:**

A histogram of Sqft_basement is shown in figure below. We can infer that the majority of properties have no basement and certainly the median value is 0.

![image](https://user-images.githubusercontent.com/95050679/144330526-c56f4ca6-09b1-49a6-88a6-32145c22fb36.png)

**Yr_renovated:**

A histogram of the year renovated is shown in figure below. We can infer that 20699 houses never underwent renovation and only 914 houses were renovated

![image](https://user-images.githubusercontent.com/95050679/144330588-21716e50-f7a6-4064-8b3f-64eef9549925.png)


![image](https://user-images.githubusercontent.com/95050679/144330606-534599c6-cb03-4f1c-8a42-8e4582f4b15f.png)

Now, let's look at bivariate analysis of price with other variables through box plots.

**Grade vs. Price:**
 
A boxplot of Grade vs Price is exponential as shown in the figure below. We can infer that as the grade (construction quality) increases the sales prices also increase. This suggests that the grade rating may be one of the strong predictors of price. Higher grades have a significant impact on the house price.

![image](https://user-images.githubusercontent.com/95050679/144330692-3211ee0d-1b07-4479-a0c6-e5a76f3f6054.png)

**Bathroom Vs Price:**

From the boxplot of bathroom vs price as shown in figure below, we can view that as the number of bathrooms increases the sales price of houses also increases gradually.

![image](https://user-images.githubusercontent.com/95050679/144330746-d9da1cdc-485e-40f4-92c8-d9a4543818d9.png)

**View vs Price:**

As learnt previously that the majority of the houses are with view 0 (as learnt previously) however, houses with view 3 and 4 have a higher house price and this can be viewed in figure below.

![image](https://user-images.githubusercontent.com/95050679/144330816-a67f7dff-02de-4cac-8920-362b4fe9724f.png)

**Zipcode vs Price:**

From the boxplot of zip code vs price is shown in figure below, we can conclude that the house prices are not much affected by zip code. This data set contains 70 unique zip codes and region with zip code 98102 have the highest house sales price followed by zip codes 98004 and 98039

![image](https://user-images.githubusercontent.com/95050679/144330918-ae059030-0c4c-4f8d-975e-c2849a2e6ff6.png)

**Yr_built vs Price:**

From the boxplot of yr_built with respect to price, we can infer that the yr_built does not have influence on house price. As the box plots of price vs. year built don’t show any obvious patterns or trends as we go from year 1900 to 2015, and we can conclude that there is no strong relationship between these two variables.

![image](https://user-images.githubusercontent.com/95050679/144331007-0af02af6-1263-44cb-b1a5-afcc520a7765.png)

Scatter plots use dots to display two variables in two dimensions. One along the x-axis and other along the y-axis. In the below figure, we added a third dimension by coloring the dots which indicate a third variable. The two variables latitude and longitude in scatter plots to examine if there were any obvious patterns geographically.

**Scatter plot of lat vs long with sqft_living:**

From the scatter plot in figure below, we can locate the larger houses. Also, we see that the majority of houses are below 4000 sqft_living. The latitude and longitude suggest a higher number of properties in the North-West of the region.

![image](https://user-images.githubusercontent.com/95050679/144331059-a941f299-ec71-430b-bea1-03ace2f61374.png)

**Scatter plot of lat vs long with grade**

From the scatter plot in figure below, we can locate where are the houses built with higher quality materials. Also, we sight that the majority of houses are of grade 7 & 8.

![image](https://user-images.githubusercontent.com/95050679/144331109-3bc48268-7483-4c82-891e-ad1e1cff4a37.png)

**Scatter plot of lat vs long with condition**

From the scatter plot in figure, we can locate where the houses are with good condition. We can see that most of the houses in the region are of condition 3 which is average condition, and we have an exceptional condition of 5 which is represented as very good condition.

![image](https://user-images.githubusercontent.com/95050679/144331165-6586f42c-cc10-49a4-9fad-5108c1f97167.png)

**Scatter Plot of House Listings Against Waterfront**

An obvious conclusion from the plot below that a majority of the listings do not have a waterfront. Listings with waterfront represented by blue dots are very scarce.

![image](https://user-images.githubusercontent.com/95050679/144331205-86e42832-f988-4e32-be91-d591353f8dc2.png)

**Scatter Plot of Price/Sqft in Sectors**

In this scatter plot, we can see that most of the houses belong to sectors A & B. The size of the markers indicate the listings price per square foot and a majority of them are placed under $400/sqft. We also observe that the more expensive listings are in Sector C (>$600/sqft)

![image](https://user-images.githubusercontent.com/95050679/144331233-45b1cf22-f2e9-4966-bffe-40cfce5c34d1.png)

**Correlation**

We will try to find which features are strongly correlated with price through a correlation table. The goal behind the study of the correlation between the variables in the data set is to identify variables with a significant linear relationship to price and those that do not

![image](https://user-images.githubusercontent.com/95050679/144331278-2c003218-3f7d-454e-b20f-2b55f6b3106f.png)

We know that the correlation of 0.7 and greater is considered a positive strong correlation. However, in this case we will consider correlation of 0.5 and greater to analyze more factors with respect to price, so the columns will be bathrooms, sqft_above, grade, sqft_living, PerSqftLiving to identify the relationship with price. Negative correlation means there is a negative relationship between the two variables. This shows that the variables move in opposite directions for a positive increase in one variable, there is a decrease in the second variable.

![image](https://user-images.githubusercontent.com/95050679/144331300-5dfb94f4-2011-4680-ad63-a05bdee44e83.png)

Now, let’s look at the correlation matrix between the numerical variables. Figure shows the heatmap that displays a table of correlation coefficients that range from -1 (perfect negative correlation) to +1 (perfect positive correlation).

![image](https://user-images.githubusercontent.com/95050679/144331326-8a7f6f5f-a1dc-4e66-b3f0-510ad382cca7.png)

From the correlation matrix, we can derive the following:
 
a. Price has a strong positive correlation with sqft_living followed by grade.
 
b. Price has moderate positive correlation with the number of Bathrooms, sqft_above and PerSqftLiving.
 
c. Price has low positive correlation with the number of Bedrooms, Floors, sqft_basement and Latitude.
 
d. Price indicates minimal relationship with sqft_lot, Yr_built and Longitude.
 
e. sqft_above, number of Bathrooms and number of Bedrooms indicates strong positive correlation with sqft_living and may explain the same variation in price as sqft_living.

Scatterplots confirm the findings of the correlation matrix and let's look at the strong relationships closely.
As in figure, we can infer that there’s clearly a linear relationship between sqft_living and housing sales price with a significant portion of outliers and it implies price is highly correlated with sqft_living.


![image](https://user-images.githubusercontent.com/95050679/144331447-1efb60c0-a27a-4312-a5c4-1eb06632b308.png)


We found the grade rating to be the second most important factor in predicting the price of a home as shown in the figure below.

![image](https://user-images.githubusercontent.com/95050679/144331485-16e2b210-d411-46e4-833a-a51d227d9699.png)

The area above ground is related to the price as well and we can infer from the scatter plot as shown in figure , that there is a positive linear relationship between the two variables.

![image](https://user-images.githubusercontent.com/95050679/144331530-31b20fd9-e424-444e-8a58-35394240450b.png)

From the scatter plot of bathrooms vs price in Figure, we can conclude the house price increases with the increase in the number of bathrooms which implies that there is positive correlation between these two variables.

![image](https://user-images.githubusercontent.com/95050679/144331568-140f2243-a9cc-4b8f-9469-58b75730264a.png)

##**Model Building**

**Multiple Linear Regression**

Since we want to understand the trend in housing prices, and which variables are the largest influencers, we created a Multiple Linear Regression model using the statsmodels.api package. However, before fitting the model, we removed the id, date, zip code, latitude, longitude, sqft_living15 and sqft_lot15 columns; since it would be hard to interpret the effect these actually had on predicting the price of a house.

With a data frame consisting of the remaining columns, we used 80% of the data as training data and 20% as testing data. 

Before getting into the model results, a brief note on scaling is needed. We did try to scale the variables prior to running the model. Since most of our variables are not normally distributed, we tried scaling by the standard scaler, standard deviation and minimum/maximum values. We ran every version of scaled data, as well as the unscaled data, and the results (R-squared and Beta Coefficients) did not significantly differ from model to model. So for ease of interpretation, we decided to run the model with unscaled data.

After setting a seed so the output is consistent regardless of who runs it, the model summary is listed below:

![image](https://user-images.githubusercontent.com/95050679/144331654-9c552f27-7731-4fdb-b5e8-7a141bfbf5f9.png)

From the table we see that our response variable (price) is highly sensitive to the waterfront column, view column and bedrooms column. Price is not very sensitive to the sqft_lot, sqft_above, sqft_below and yr_renovated columns.

According to our R-Squared value, we are able to explain about 65.2% of the variation in housing price with this model. Our Adjusted R-Square value, which increases the model only if a new predictor variable enhances the model above what would be obtained by probability, is only slightly lower at 65.1%

While only explaining 65.1% of the variation seems low at first, and we’d obviously like it to be higher, it does not mean that our model is not a good fit. We have to realize that real estate is an emotionally driven industry. Since human emotions are such a large factor in determining what house someone buys, it’s logical to assume that real estate prices have an inherently greater amount of unexplainable variation. Instead, we need to either 1) include additional predictor variables to try and improve our Adjusted R-squared; or 2) look back to our beta coefficients to determine which variables house price is most sensitive to.


**Logistic Regression**

In addition to Linear Regression, we used Logistic Regression to try and predict whether or not a house was renovated. After randomly splitting our data into an 80%/20% train/test split, the coefficients corresponding to each variable are listed next to them in the above table.

![image](https://user-images.githubusercontent.com/95050679/144331734-42270716-0b78-47e9-8cbe-9665576df6c1.png)

Using our testing data, our model was able to correctly predict 95.74% of the outcomes.

Based on our model’s accuracy, we created three hypothetical houses, and used the model to calculate the probability of each being renovated. Their characteristics and probabilities are listed in the table below:

![image](https://user-images.githubusercontent.com/95050679/144331749-133faa4c-0301-449b-a929-3d0e0aa06920.png)


**k-Nearest Neighbors Model**

Following the prediction using logistic regression, we tried to predict the condition of the house by using the kNN model. For this, we consider similar variables as the regression model.

A bar chart for house condition yielded the below results

![image](https://user-images.githubusercontent.com/95050679/144331805-32c20f9b-0931-499b-9788-944a740174ba.png)

We can observe that houses with an average condition or condition = 3 have the highest number of listings which is approximately 38.65% more than the next highest category of Good or 4.

A kNN model was built by taking 4000 rows to be in our training set and the remaining in the test set. The results for the kNN model are as follows:

![image](https://user-images.githubusercontent.com/95050679/144331831-f3c048ed-70e0-46dc-b3c6-cace25bc5262.png)

We find that our model can accurately predict 62% of the time regarding the condition of the house. But as spoken earlier the percentages for average house listings make for almost 65% of the total. Hence it is highly possible that our test set does not include houses from other categories.

By looking at the results, there were no cases of condition 1 & 2 in our classification, hence this precision by default is assigned 0. 

Precision is the ability of the model to correctly predict each condition.The model correctly predicted 65% of values in condition 3, 34% of values in condition 4 and 13% of values in condition 5.

Recall is the ratio of true positives to the sum of true positives and false negatives. In short, it is the ratio of all outcomes that were predicted correctly to the sum of outcomes that were predicted correctly and positive outcomes that were predicted as negative. 

F1 score close to 1 indicates a good score and 0 otherwise. 

Support is the number of conditions that were in our test set.

![image](https://user-images.githubusercontent.com/95050679/144331871-fd94813c-2e6f-4fc4-8d43-e00e5449654c.png)

Although overall kNN accuracy is less, it does not necessarily mean that the model is not appropriate. Factors outside the information available in our data set might contribute towards a better accuracy score. As discussed earlier, real estate sales tend to be emotionally driven and which can be very hard to predict.

**Conclusions:**
1.	The strongest contributors to the house price increase are sqft_living and grade.
2.	Price increase with increase in sqft_above, bathrooms and condition.
3.	Houses with view 3 and 4 are expected to have a higher price.
4.	The year the house was built has negligible relationship with price.
5.	Logistic Regression was able to accurately predict whether a house was renovated or not.
6.	The Multiple Linear Regression model may need additional variables to improve the accuracy of predicting price.


**Recommendations:**
1.	During exploratory data analysis, there were several outliers in housing prices. We suspect that these are luxury homes, and may be impacting the ability to accurately gauge the average house in King County. We recommend that when collecting new data, it is split into two groups: luxury vs. average. This will allow any analysis to be more representative of the population in question.


3.	I also recommend that when collecting new data, additional variables are collected as well. These could include: facilities, neighborhood rating, crime rates, HOA vs. no HOA, etc. These will inevitably make the house price prediction more accurate.











































