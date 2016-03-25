#jianmin
#NBA project 2
#fixed effect model and random effect model test
#need install library first
library(plm)

#read raw data, URL in windows OS 
rawdata<- read.csv("C:\\Users\\user\\Documents\\GitHub\\ProjectNBA\\players_2006_clean.csv",header=TRUE)
attach(rawdata)

#to predict Salary
Y <- cbind(Salary)

#test variables
X <- cbind(Height, Weight, Experience, College, G, MP, ThreePoint, TwoPoint, FT, ORB, DRB, AST, STL, BLK, TOV, PF)

#use player name and season as index
paneldata <- plm.data(rawdata, index=c("Name","Season"))

#test show summary of variables
#summary(Y)
#summary(X)

#fixed effects model
fixed <- plm(Y ~ X, data=paneldata, model= "within")
summary(fixed)

#random effects model
random <- plm(Y ~ X, data=paneldata, model= "random")
summary(random)

#do hausman test for fixed vs random effects model
phtest(random, fixed)