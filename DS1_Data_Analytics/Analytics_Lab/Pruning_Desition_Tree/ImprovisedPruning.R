# Import the rpart library
library(rpart)

# Import the partykit library
library(partykit)

# Import the package for Random Forest
library(randomForest)

# Read the data
inputFile = '/users/pgrad/thundyia/Trinity/DS1_Data_Analytics/Analytics_Lab/Pruning_Desition_Tree/DT-Credit.csv'
csvFileSeperator = ','
data = read.csv(inputFile, header=TRUE,sep=csvFileSeperator)

# Print distinct Categories of data using STR fn
print('*** The Raw Data Set ***')
str(data)

# Columns that need to be converted as factors
columns <- c(1:2,4:10,12:22,24:32)

# Function to change int to factor
data[columns] <- lapply(data[columns],factor)

# Look at the data
str(data)

# Remove the first column
data <- data[,-1]

# Chech the data now
str(data)
names(data)

# Attach the data
attach(data)

# Create the model with RESPONSE as target
dtModel <- rpart(RESPONSE~.,data=data, control=rpart.control(minsplit=60, minbuncket=30, maxdepth=4))

# Plot the data and print it
plot(as.party(dtModel))
print(dtModel)

# Create a Model without control
dtModelNoControl <- rpart(RESPONSE~.,data=data)

# Plot it
plot(as.party(dtModelNoControl))

# Print the CP Table of the no control model and plot it so that we can find the right level to prune
print(dtModelNoControl$cptable)
plotcp(dtModelNoControl)

# Pick the least error tree automatically
opt <- which.min(dtModelNoControl$cptable[,"xerror"])
cp <- dtModelNoControl$cptable[opt,"CP"]

# Create the prunedTree
dtModelPruned <- prune(dtModelNoControl, cp=cp)

# Plot the pruned Model
plot(as.party(dtModelPruned))


### --- Random Forest --- 
randForest <- randomForest(RESPONSE~.,data=data)

# Print the random Forest Result
print(randForest)

# See the importance of each predictor
importance(randForest)

# Plot the importance - Based on this plot, create a new tree
varImpPlot(randForest)

# See the error vs number of tree
plot(randForest)


# Plotting a new DT with the top ten predictors
dtModelSelectedPredictors <- rpart(RESPONSE ~ AMOUNT+CHK_ACCT+AGE+DURATION+HISTORY+EMPLOYMENT+SAV_ACCT+PRESENT_RESIDENT+INSTALL_RATE+JOB, data=data)

# Plot the new tree
plot(as.party(dtModelSelectedPredictors))


