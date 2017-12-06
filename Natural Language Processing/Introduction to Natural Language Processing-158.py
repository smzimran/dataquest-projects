## 2. Overview of the Data ##

import pandas as pd
submissions = pd.read_csv("sel_hn_stories.csv")
submissions.columns = ["submission_time", "upvotes", "url", "headline"]
submissions = submissions.dropna()

## 3. Tokenizing the Headlines ##

tokenized_headlines = []
for headline in submissions['headline']:
    tokenized_headlines.append(headline.split(' '))
    


## 4. Preprocessing Tokens to Increase Accuracy ##

punctuation = [",", ":", ";", ".", "'", '"', "’", "?", "/", "-", "+", "&", "(", ")"]
clean_tokenized = []

for item in tokenized_headlines:
    tokens = []
    for token in item:
        token = token.lower()
        for p in punctuation:
            token = token.replace(p, '')
        tokens.append(token)
    clean_tokenized.append(tokens)


## 5. Assembling a Matrix of Unique Words ##

import numpy as np
unique_tokens = []
single_tokens = []

for tokens in clean_tokenized:
    for token in tokens:
        if token not in single_tokens:
            single_tokens.append(token)
        elif token not in single_tokens and token not in unique_tokens:
            unique_tokens.append(token)

counts = pd.DataFrame(0, index=np.arange(len(clean_tokenized)), columns=unique_tokens)

## 6. Counting Token Occurrences ##

# We've already loaded in clean_tokenized and counts
for index, tokens in enumerate(clean_tokenized):
    for token in tokens:
        if token in unique_tokens:
            counts.iloc[index][token] += 1
            

## 7. Removing Columns to Increase Accuracy ##

# We've already loaded in clean_tokenized and counts

word_counts = counts.sum(axis=0)
counts = counts.loc[:, (word_counts >= 5) & (word_counts <= 100)]

## 8. Splitting the Data Into Train and Test Sets ##

from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(counts, submissions["upvotes"], test_size=0.2, random_state=1)

## 9. Making Predictions With fit() ##

from sklearn.linear_model import LinearRegression

clf = LinearRegression()
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)

## 10. Calculating Prediction Error ##

mse = ((predictions - y_test)**2).mean()