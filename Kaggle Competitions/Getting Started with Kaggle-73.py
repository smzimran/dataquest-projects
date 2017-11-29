## 2. Examining the Data With .describe() ##

# We can use the pandas library in Python to read in the CSV file
# This creates a pandas dataframe and assigns it to the titanic variable
titanic = pandas.read_csv("titanic_train.csv")

# Print the first five rows of the dataframe
print(titanic.head(5))
print(titanic.describe())

## 3. Cleaning Up Missing Data ##

# The titanic variable is available here
titanic["Age"] = titanic["Age"].fillna(titanic["Age"].median())

## 5. Converting the Sex Column to Numeric ##

# Find all of the unique genders 
# The column appears to contain the values male and female only
print(titanic["Sex"].unique())

# Replace all the occurences of male with the number 0
titanic.loc[titanic["Sex"] == "male", "Sex"] = 0
titanic.loc[titanic["Sex"] == "female", "Sex"] = 1

## 6. Converting the Embarked Column ##

# Find all of the unique values for "Embarked"
print(titanic["Embarked"].unique())
titanic["Embarked"] = titanic["Embarked"].fillna("S")

titanic.loc[titanic["Embarked"] == "S", "Embarked"] = 0
titanic.loc[titanic["Embarked"] == "C", "Embarked"] = 1
titanic.loc[titanic["Embarked"] == "Q", "Embarked"] = 2

## 9. Making Predictions With scikit-learn ##

# Import the linear regression class
from sklearn.linear_model import LinearRegression
# Sklearn also has a helper that makes it easy to do cross-validation
from sklearn.model_selection import KFold

# The columns we'll use to predict the target
predictors = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]

# Initialize our algorithm class
alg = LinearRegression()
# Generate cross-validation folds for the titanic data set
# It returns the row indices corresponding to train and test
# We set random_state to ensure we get the same splits every time we run this
kf = KFold(3, random_state=1)

predictions = []
for train, test in kf.split(titanic):
        # The predictors we're using to train the algorithm  
    # Note how we only take the rows in the train folds
    train_predictors = (titanic[predictors].iloc[train,:])
    # The target we're using to train the algorithm
    train_target = titanic["Survived"].iloc[train]
    # Training the algorithm using the predictors and target
    alg.fit(train_predictors, train_target)
    # We can now make predictions on the test fold
    test_predictions = alg.predict(titanic[predictors].iloc[test,:])
    predictions.append(test_predictions)


## 10. Evaluating Prediction Error ##

import numpy as np

# The predictions are in three separate NumPy arrays  
# Concatenate them into a single array, along the axis 0 (the only 1 axis) 
predictions = np.concatenate(predictions, axis=0)

# Map predictions to outcomes (the only possible outcomes are 1 and 0)
predictions[predictions > .5] = 1
predictions[predictions <=.5] = 0
accuracy = len(predictions[predictions == titanic["Survived"]]) / len(predictions)

## 11. Logistic Regression ##

from sklearn.model_selection import cross_val_score

# Initialize our algorithm
alg = LogisticRegression(random_state=1)
# Compute the accuracy score for all the cross-validation folds; this is much simpler than what we did before
scores = cross_val_score(alg, titanic[predictors], titanic["Survived"], cv=3)
# Take the mean of the scores (because we have one for each fold)
print(scores.mean())
