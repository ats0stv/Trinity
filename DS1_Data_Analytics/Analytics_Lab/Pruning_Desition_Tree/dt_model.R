# Import the rpart library
library(rpart)

# Import the partykit library
library(partykit)

# Read the data
inputFile = './DT-Credit.csv'
csvFileSeperator = ','
data = read.csv(inputFile, header=TRUE,sep=csvFileSeperator)

# Print distinct Categories of data using STR fn
print('*** The Raw Data Set ***')
str(data)

# Convert all features to factor and print it
data[] = lapply(data[],factor)
print('*** After Converting it to Factors***')
str(data)

# Now change only the required one DURATION, AGE and AMOUNT back into the numeric
data[which(names(data) %in% c('DURATION', 'AGE', 'AMOUNT'))] = lapply(data[which(names(data) %in% c('DURATION', 'AGE', 'AMOUNT'))], function(x) as.numeric(as.character(x)))
print('*** After converting the required back to numeric ***')
str(data)

# Remote the index column named OBS. from the data as it is useless
data = data[ ,-which(names(data) %in% c('OBS.'))]

# Attach the data to the R search path so that the objects can be accesed by simply giving their name
attach(data)

# From the DT model
dtModel <- rpart(RESPONSE~., data = data, control = rpart.control(minsplit = 60, minbucket = 30, maxdepth = 4))

# Plot the DT Model
print('*** Plotting the basic Model ***')
plot(as.party(dtModel))

# Print the DT model as values
print('*** Printing the basic Model ***')
print(dtModel)


# --- Working on Binary Values ----


# Change the values of param RESPONSE from 0,1 to N,Y
target = ifelse(RESPONSE==1, 'Y', 'N')

# Add the newly created param to the data
data <- data.frame(data,target)

# Checking the contents of the new data set with the target field
print('*** Data with target inserted***')
str(data)

# Drop the RESPONSE param from the data set
dataNew = data[ ,-which(names(data) %in% c('RESPONSE'))]

print('*** Data with RESPONSE removed ***')
str(dataNew)
# Create a new model using the newly created param target

dtModelNew = rpart(target~., data = dataNew, control = rpart.control(minsplit = 60, minbucket = 30, maxdepth = 4))

# Plot and print the new dtModel
print('*** Plotting the New Data Model with Target ***')
plot(as.party(dtModelNew))
print('*** Printing the New Data Model with Target***')
print(dtModelNew)

# Create a New Data Model without control
dtModelPruning <- rpart(target~., data = dataNew)

# Plot it
print('*** Plotting the model without control***')
plot(as.party(dtModelPruning))

# Plot the Cross Valilation Results

print('*** Printing the CP Graph for finding pruning***')
plotcp(dtModelPruning)

# Printing the CP Table - Complexity Point
print('*** Printing the CP table of the model without control ***')
print(dtModelPruning$cptable)

# Choose the option with minimum xerror - Cross Validation Error
# CV Error grow as the tree gets more level
# Rule of Thumb - Choose the lowest level where rel_error + xstd < xerror
opt <- which.min(dtModelPruning$cptable[,'xerror'])
cp <- dtModelPruning$cptable(opt, 'CP')
dtModelPruned <- prune(dtModelPruning, cp = cp)

# Plot the puned data
print('*** Plotting the Pruned Table ***')
plot(as.party(dtModelPruned))
print('*** Printing the Pruned Table ***')
print(dtModelPruned)
Add the newly created param to the data
data <- data.frame(data,target)

# Checking the contents of the new data set with the target field
print('*** Data with target inserted***')
str(data)

# Drop the RESPONSE param from the data set
dataNew = data[ ,-which(names(data) %in% c('RESPONSE'))]

print('*** Data with RESPONSE removed ***')
str(dataNew)
# Create a new model using the newly created param target

dtModelNew = rpart(target~., data = dataNew, control = rpart.control(minsplit = 60, minbucket = 30, maxdepth = 4))

# Plot and print the new dtModel
print('*** Plotting the New Data Model with Target ***')
plot(as.party(dtModelNew))
print('*** Printing the New Data Model with Target***')
print(dtModelNew)

# Create a New Data Model without control
dtModelPruning <- rpart(target~., data = dataNew)

# Plot it
print('*** Plotting the model without control***')
plot(as.party(dtModelPruning))

# Plot the Cross Valilation Results

print('*** Printing the CP Graph for finding pruning***')
plotcp(dtModelPruning)

# Printing the CP Table - Complexity Point
print('*** Printing the CP table of the model without control ***')
print(dtModelPruning$cptable)

# Choose the option with minimum xerror - Cross Validation Error
# CV Error grow as the tree gets more level
# Rule of Thumb - Choose the lowest level where rel_error + xstd < xerror
opt <- which.min(dtModelPruning$cptable[,'xerror'])
cp <- dtModelPruning$cptable[opt, 'CP']
dtModelPruned <- prune(dtModelPruning, cp = cp)

# Plot the puned data
print('*** Plotting the Pruned Table ***')
plot(as.party(dtModelPruned))
print('*** Printing the Pruned Table ***')
print(dtModelPruned)
