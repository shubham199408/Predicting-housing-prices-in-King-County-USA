#### Predicting-housing-prices-in-King-County-USA

**Overview**

The dataset that was used for this project consists of sales data between May 2014 and May 2015 in King County, Washington, which includes the 18th most populous city in the US, Seattle. Our group sourced this data set from the website Kaggle, which focuses on data science learning, and houses a vast library of datasets across numerous industries. This dataset was chosen due its size, number of numerical and categorical variables, relative cleanliness, completeness and ease of interpretation. It is a CSV file that contains 21,614 rows (21,613 observation & 1 header row), and 21 columns. The table below summarizes the columns, and our interpretation of them

![Picture1](https://user-images.githubusercontent.com/95050679/144138509-415f7ed8-8015-4e70-a291-25a8bc984179.png)

In this analysis, I used several Python packages/techniques including, but not limited to: Pandas, NumPy, Matplotlib and Sci-kit Learn, which will all be highlighted in the following sections of this report, and can be viewed in the Python code for the project. Ultimately, My main objective is to understand the trend in housing prices for King County during this time period; along with what factors have the largest influence on price.

**##Data Cleaning/Pre-Processing##**

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

#**Housing Price Distribution**
