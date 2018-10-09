# Decision Tree - Example 1 

# Import Library DPLYR - Cleaning Dataset and factoring them
library(dplyr)

# Plotting Library
library(rpart)
library(rpart.plot)

# Shuffle Data Set or No
shuffleSet = TRUE

#Home Dir
homeDir <- "/users/pgrad/thundyia/"

# Dataset Available in dataset.csv in Home Dir
datasetName <- "dataset.csv"

# Absolute File Path
absFilePath <- paste(homeDir,datasetName,sep="")

# Read the dataset
myDataSet <- read.csv(file=absFilePath, header=TRUE, sep=",")

# Print the dataset
print(myDataSet)

# Get into some real stuff

# Set seed for randomization
set.seed(18)

# Create a shuffled index to shuffle the data - 1 to size of data
shuffledIndex <- sample(1:nrow(myDataSet))

# Shuffle the data
if(shuffleSet) {
    myDataSet = myDataSet[shuffledIndex, ]
}

# Cleaning is not required as all the variables are already labelled

# Method to split the data into train and test
create_train_test_data <- function(data, size=0.8, train=TRUE) {
    nRow=nrow(data)
    totalRow = size * nRow
    trainSample <- 1:totalRow
    if(train) {
        return (data[trainSample, ])
    }
    else {
        return (data[-trainSample, ])
    }
}

# DF for Train
train <- create_train_test_data(myDataSet)

# DF for Test
test <- create_train_test_data(myDataSet,train=FALSE)


# Debug
print("Test Data Distribution")
print(prop.table(table(test$PlayGold)))

print("Train Data Distribution")
print(prop.table(table(train$PlayGold)))


fit <- rpart(PlayGold~., data=train, method='class')
rpart.plot(fit,extra=106)

predictUnseen <- predict(fit,test, type='class')
testConfusionMatrix <- table(test$PlayGold,predictUnseen)
print("Confusion Matrix")
print(testConfusionMatrix)

accuracy <-sum(diag(testConfusionMatrix)) / sum(testConfusionMatrix)

print("Accuracy")
print(accuracy)
