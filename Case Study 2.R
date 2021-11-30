install.packages("tidyverse")  #This package contains an opinionated collection of R packages designed for data manipulation, exploration and visualization. 
install.packages("funModeling") #This package contains a set of functions related to exploratory data analysis, data preparation, and model performance. 
install.packages("Hmisc") 
install.packages("mctest")
install.packages("leaps")
install.packages("DataExplorer")
install.packages("modelr")
install.packages("broom")
install.packages("caret")
install.packages("MASS")

setwd("C:/Users/shubh/OneDrive/Desktop")
ski <- read_excel("ski.xlsx")
View(ski)

install.packages("psych")
library(psych)
library(caret)
library(MASS)
library(readxl)
library(funModeling) 
library(tidyverse)
library(Hmisc)
library(mctest)
library(car)
library(lmtest)
library(leaps)
library(DataExplorer)
library(modelr)
library(broom)
library(boot)

plot_str(ski)#show us what type of variables we have in our data set ski and also the dimensions
plot_missing(ski)#return the number of missing values in our dataset
summary(ski)

# a function to run few lines of codes at one shot
perform_eda <- function(ski)
{
  glimpse(ski)   #Number of observations(rows) and variables (columns)
  df_status(ski) #Getting the metrics about zeros, missing values, infinite numbers, data types & 
  #quantity of unique values
  plot_num(ski) # This function comes in funModeling package and we get histogram
  describe(ski) #This function comes in the Hmisc package and allows us to quickly profile a complete 
  #dataset for both numerical and categorical variables
  profiling_num(ski) #This function comes in funModeling package and we get a full univariate analysis for numerical

}
perform_eda(ski)

# histogram, boxplot and summary for all variabls

b <- hist(ski$Bedrooms,ylim=c(0,20), main="Histogram for bedrooms",xlab="Bedrooms",col="blue")
text(b$mids,b$counts,labels=b$counts, adj=c(0.5, -0.5))
boxplot(ski$Bedrooms,xlab='No. of bedrooms',main='Boxplot of Bedrooms')
summary(ski$Bedrooms)



bath <- hist(ski$Bathrooms,ylim=c(0,20),main="Histogram for bathrooms",xlab="Bathrooms",col="blue")
text(bath$mids,bath$counts,labels=bath$counts, adj=c(0.5, -0.5))
boxplot(ski$Bathrooms,xlab='No. of bathrooms',main='Boxplot of Bathrooms')
summary(ski$Bathrooms)

s <- hist(ski$Sq_Ft,ylim=c(0,15),main="Histogram for Sq_Ft",xlab="Sq_Ft",col="blue")
text(s$mids,s$counts,labels=s$counts, adj=c(0.5, -0.5))
boxplot(ski$Sq_Ft,xlab='Sq_Ft',main='Boxplot of Sq_Ft')
summary(ski$Sq_Ft)

dt <- hist(ski$Downtwon,ylim=c(0,30),main="Histogram for Downtown",xlab="Downtown",col="blue",breaks=20)
text(dt$mids,dt$counts,labels=dt$counts, adj=c(0.5, -0.5))
boxplot(ski$Downtwon,xlab='Downtown',main='Boxplot of Downtown')
summary(ski$Downtwon)


mt <- hist(ski$Mountain,ylim=c(0,20),main="Histogram for Mountain",xlab="Mountain",col="blue")
text(mt$mids,mt$counts,labels=mt$counts, adj=c(0.5, -0.5))
boxplot(ski$Mountain,xlab='Mountain',main='Boxplot of Mountain')
summary(ski$Mountain)

lot <- hist(ski$`Lot size`,ylim=c(0,40),main="Histogram for Lot size",xlab="Lot size",col="blue")
text(lot$mids,lot$counts,labels=lot$counts, adj=c(0.5, -0.5))
boxplot(ski$`Lot size`,xlab='Lot Size',main='Boxplot of Lot Size')
summary(ski$`Lot size`)

g <- hist(ski$Garage,ylim=c(0,30),main="Histogram for Garage",xlab="Garage",col="blue")
text(g$mids,g$counts,labels=g$counts, adj=c(0.5, -0.5))
boxplot(ski$Garage,xlab='Garage',main='Boxplot of Garage')
summary(ski$Garage)


age <- hist(ski$Age,ylim=c(0,20),main="Histogram for Age",xlab="Age",col="blue")
text(age$mids,age$counts,labels=age$counts, adj=c(0.5, -0.5))
boxplot(ski$Age,xlab='Age',main='Boxplot of Age')
summary(ski$Age)


o <- hist(ski$`On market`,ylim=c(0,15),main="Histogram for On market",xlab="On market",col="blue")
text(o$mids,o$counts,labels=o$counts, adj=c(0.5, -0.5))
boxplot(ski$`On market`,xlab='On Market',main='Boxplot of On Market')
summary(ski$`On market`)


sp <- hist(ski$`Selling price`,ylim=c(0,15),main="Histogram for Selling price",xlab="Selling price",col="blue")
text(sp$mids,sp$counts,labels=sp$counts, adj=c(0.5, -0.5))
boxplot(ski$`Selling price`,xlab='Selling Price',main='Boxplot of Selling Price')
summary(ski$`Selling price`)

lp <- hist(ski$`List price`,ylim=c(0,20),main="Histogram for List price",xlab="List price",col="blue")
text(lp$mids,lp$counts,labels=lp$counts, adj=c(0.5, -0.5))
hist(ski$`List price`, main="Histogram for List price", xlab="List price", col="blue")
boxplot(ski$`List price`,xlab='List Price',main='Boxplot of List Price')
summary(ski$`List price`)

#scatterplots of all variables wrt. each other
pairs(ski)

#to make correlation heat map , until after #heatmap
cormat <- round(cor(ski),2)
cormat

# Get upper triangle of the correlation matrix
get_upper_tri <- function(cormat){
  cormat[lower.tri(cormat)]<- NA
  return(cormat)
}

upper_tri <- get_upper_tri(cormat)
upper_tri
library(reshape2)
melted_cormat <- melt(upper_tri, na.rm = TRUE)
# Heatmap
library(ggplot2)
ggplot(data = melted_cormat, aes(Var2, Var1, fill = value))+
  geom_tile(color = "white")+
  scale_fill_gradient2(low = "blue", high = "red", mid = "white", 
                       midpoint = 0, limit = c(-1,1), space = "Lab", 
                       name="Pearson\nCorrelation") +
  theme_minimal()+ 
  theme(axis.text.x = element_text(angle = 45, vjust = 1, 
                                   size = 12, hjust = 1))+
  coord_fixed()


#performing log transform to normalize the data which is very skewed
par(mfrow=c(3,3))
hist(log(ski$Downtwon),xlab='Downtown',main='Histogram of Log Downtown')
hist(log(ski$Mountain),xlab='Mountain',main='Histogram of Log Mountain')
hist(log(ski$`Lot size`),xlab='Lot Size',main='Histogram of Log Lot Size')
hist(log(ski$Garage),xlab='Garage',main='Histogram of Log Garage')
hist(log(ski$Age),xlab='Age',main='Histogram of Log Age')
hist(log(ski$`On market`),xlab='On Market',main='Histogram of Log On Market')


#transforming the varaibles to make the normal

downtownlog=log(ski$Downtwon)
mountainlog=log(ski$Mountain)
lotsizelog=log(ski$`Lot size`)
agelog=log(ski$Age)
onmarlog=log(ski$`On market`)
garagelog=log(ski$Garage)

#MODELING 

model1 <- lm(ski$`Selling price` ~ ski$Bedrooms+ski$Bathrooms+ski$Sq_Ft+ski$Downtwon+ski$Mountain+ski$`Lot size`+ski$Garage+ski$Age+ski$`On market`+ski$`List price`)

summary(model1)
vif(model1)
AIC(model1)

#from m1, we see that the vif of list price is more than 5. 
#removed listprice from m1

model2 <- lm(ski$`Selling price` ~ ski$Bedrooms+ski$Bathrooms+ski$Sq_Ft+ski$Downtwon+ski$Mountain+ski$`Lot size`+ski$Garage+ski$Age+ski$`On market`)
summary(model2)
vif(model2)
AIC(model2)

#removed downtown(high VIF with Mountain),age and on market in m3 due to low significance
model3 <- lm(ski$`Selling price` ~ ski$Bedrooms+ski$Bathrooms+ski$Sq_Ft+ski$Mountain+ski$`Lot size`+ski$Garage)
summary(model3)
vif(model3)
AIC(model3)

#we removed bathroom due to low significance in final model

finalmodel <- lm(ski$`Selling price` ~ ski$Bedrooms+ski$Sq_Ft+ski$Mountain+ski$`Lot size`+ski$Garage)
summary(finalmodel)
vif(finalmodel)
AIC(finalmodel)



#----------------------------------------------------------------------
ski$`rty #`=NULL
ski$`List price`=NULL
head(ski)
ski=ski[c(10,1,2,3,4,5,6,7,8,9)]

head(ski)

# Calculate Relative Importance for Each Predictor
install.packages("relaimpo")
library(relaimpo)
calc.relimp(ski,type=c("lmg"),
            rela=TRUE)

# Bootstrap Measures of Relative Importance (1000 samples)
boot <- boot.relimp(ski, b = 1000, type = "lmg", rank = TRUE,
                    diff = TRUE, rela = TRUE)
booteval.relimp(boot) # print result
plot(booteval.relimp(boot,sort=TRUE)) # plot result
##############


#STEPWISE AIC 
# Fit the full model 
full.model <- lm(ski$`Selling price` ~., data = ski)
# Stepwise regression model
step.model <- stepAIC(full.model, direction = "both", 
                      trace = FALSE)

summary(step.model)
vif(step.model)
step.model$anova

install.packages("plyr")
library(plyr)

#model validation

a=rename(ski, c("Selling price"="sp", "Lot size"="lot","On market"="onmar"))
a

data_ctrl <- trainControl(method = "cv", number = 5)

model_caret <- train( sp ~ Bedrooms+Sq_Ft+Mountain+lot+Garage,   # model to fit
                     data = a,                        
                     trControl = data_ctrl,              # folds
                     method = "lm",                      # specifying regression model
                     na.action = na.pass)     

model_caret$finalModel

model_caret$resample


#linearity assumption
par(mfrow=c(3,2))

plot(ski$Bedrooms,ski$`Selling price`)
abline(lm(ski$`Selling price` ~ ski$Bedrooms))

plot(ski$Sq_Ft,ski$`Selling price`)
abline(lm(ski$`Selling price` ~ ski$Sq_Ft))

plot(ski$Garage,ski$`Selling price`)
abline(lm(ski$`Selling price` ~ ski$Garage))

plot(ski$Mountain,ski$`Selling price`)
abline(lm(ski$`Selling price` ~ ski$Mountain))

plot(ski$`Lot size`,ski$`Selling price`)
abline(lm(ski$`Selling price` ~ ski$`Lot size`))

#residual analysis
par(mfrow=c(2,2))
#for residual vs fitted(homoscedasticity) and qq plot(normality)
plot(step.model)

#residuals vs. independent variables, shows no apparent pattern except SQft
par(mfrow=c(3,2))
plot(ski$Sq_Ft, step.model$residuals, 
            ylab="Residuals", xlab="Sq Ft", main = "Residuals vs Independent Variable") 
abline(0, 0)                  # the horizon

plot(ski$Bedrooms, step.model$residuals, 
     ylab="Residuals", xlab="Bedrooms",main = "Residuals vs Independent Variable") 
abline(0, 0)                  # the horizon

plot(ski$Mountain, step.model$residuals, 
     ylab="Residuals", xlab="Mountain", main = "Residuals vs Independent Variable") 
abline(0, 0)                  # the horizon

plot(ski$`Lot size`, step.model$residuals, 
     ylab="Residuals", xlab="Lot Size",main = "Residuals vs Independent Variable") 
abline(0, 0)                  # the horizon

plot(ski$Garage, step.model$residuals, 
     ylab="Residuals", xlab="Garage",main = "Residuals vs Independent Variable") 
abline(0, 0)                  # the horizon


#independence of errors
dwtest(step.model)

#normality
par(mfrow=c(1,1))
hist(residuals(step.model), main='Histogram of Residuals')




# the bests subsets approach
models <- regsubsets(ski$`Selling price`~., data = ski, nvmax = 5,
                     method = "seqrep")
summary(models)
plot(models,scale="adjr2",main = "The Best subset Model")
subsets(models, statistic="adjr2", main = "The Best subset Model")
#can replace in statistic=bic, cp, adjr2, and rss. rsq

plot(models)

#########################################

