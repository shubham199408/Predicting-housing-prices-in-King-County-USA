#### Predicting-housing-prices-in-King-County-USA

**Overview**

The dataset that was used for this project consists of sales data between May 2014 and May 2015 in King County, Washington, which includes the 18th most populous city in the US, Seattle. Our group sourced this data set from the website Kaggle, which focuses on data science learning, and houses a vast library of datasets across numerous industries. This dataset was chosen due its size, number of numerical and categorical variables, relative cleanliness, completeness and ease of interpretation. It is a CSV file that contains 21,614 rows (21,613 observation & 1 header row), and 21 columns. The table below summarizes the columns, and our interpretation of them

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

##**EDA visualizations and insights**

