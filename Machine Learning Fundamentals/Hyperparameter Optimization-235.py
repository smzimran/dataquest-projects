## 1. Recap ##

import pandas as pd

train_df = pd.read_csv('dc_airbnb_train.csv')
test_df = pd.read_csv('dc_airbnb_test.csv')

## 2. Hyperparameter optimization ##

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

hyper_params = [1, 2, 3, 4, 5]
mse_values = []
for h in hyper_params:
    knn = KNeighborsRegressor(n_neighbors = h, algorithm = 'brute')
    features = ['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews']
    knn.fit(train_df[features], train_df['price'])
    predictions = knn.predict(test_df[features])
    mse_values.append(mean_squared_error(test_df['price'], predictions))
    
print(mse_values)

## 3. Expanding grid search ##

hyper_params = [x for x in range(1,21)]
mse_values = []
for h in hyper_params:
    knn = KNeighborsRegressor(n_neighbors = h, algorithm = 'brute')
    features = ['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews']
    knn.fit(train_df[features], train_df['price'])
    predictions = knn.predict(test_df[features])
    mse_values.append(mean_squared_error(test_df['price'], predictions))
    
print(mse_values)

## 4. Visualizing hyperparameter values ##

import matplotlib.pyplot as plt
%matplotlib inline

features = ['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews']
hyper_params = [x for x in range(1, 21)]
mse_values = list()

for hp in hyper_params:
    knn = KNeighborsRegressor(n_neighbors=hp, algorithm='brute')
    knn.fit(train_df[features], train_df['price'])
    predictions = knn.predict(test_df[features])
    mse = mean_squared_error(test_df['price'], predictions)
    mse_values.append(mse)
    
plt.scatter(hyper_params, mse_values)
plt.show()

## 5. Varying features and hyperparameters ##

hyper_params = [x for x in range(1,21)]
mse_values = list()

for h in hyper_params:
    knn = KNeighborsRegressor(n_neighbors = h, algorithm = 'brute')
    features = train_df.columns
    features.drop('price')
    knn.fit(train_df[features], train_df['price'])
    predictions = knn.predict(test_df[features])
    mse_values.append(mean_squared_error(test_df['price'], predictions))
    
plt.scatter(hyper_params, mse_values)
plt.show()

## 6. Practice the workflow ##

two_features = ['accommodates', 'bathrooms']
three_features = ['accommodates', 'bathrooms', 'bedrooms']
hyper_params = [x for x in range(1,21)]
# Append the first model's MSE values to this list.
two_mse_values = list()
# Append the second model's MSE values to this list.
three_mse_values = list()
two_hyp_mse = dict()
three_hyp_mse = dict()

for k in hyper_params:
    knn = KNeighborsRegressor(n_neighbors = k, algorithm = 'brute')
    knn.fit(train_df[two_features], train_df['price'])
    predictions = knn.predict(test_df[two_features])
    mse = mean_squared_error(test_df['price'], predictions)
    two_mse_values.append(mse)

for k, mse in enumerate(two_mse_values):
    if mse == min(two_mse_values):
        two_hyp_mse[k+1] = mse
        
for k in hyper_params:
    knn = KNeighborsRegressor(n_neighbors = k, algorithm = 'brute')
    knn.fit(train_df[three_features], train_df['price'])
    predictions = knn.predict(test_df[three_features])
    mse = mean_squared_error(test_df['price'], predictions)
    three_mse_values.append(mse)

for k, mse in enumerate(three_mse_values):
    if mse == min(three_mse_values):
        three_hyp_mse[k+1] = mse
