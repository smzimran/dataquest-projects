## 1. Recap ##

import pandas as pd
loans = pd.read_csv('filtered_loans_2007.csv')
null_counts = loans.isnull().sum()
print(null_counts)

## 2. Handling missing values ##

loans.drop('pub_rec_bankruptcies', axis=1, inplace=True)
loans.dropna(inplace=True)

## 3. Text columns ##

object_columns_df = loans.select_dtypes(include=['object'])
print(object_columns_df.iloc[0])

## 5. First 5 categorical columns ##

cols = ['home_ownership', 'verification_status', 'emp_length', 'term', 'addr_state']

[print(loans[col].value_counts()) for col in cols]

## 6. The reason for the loan ##

for col in ['purpose', 'title']:
    print(loans[col].value_counts())

## 7. Categorical columns ##

mapping_dict = {
    "emp_length": {
        "10+ years": 10,
        "9 years": 9,
        "8 years": 8,
        "7 years": 7,
        "6 years": 6,
        "5 years": 5,
        "4 years": 4,
        "3 years": 3,
        "2 years": 2,
        "1 year": 1,
        "< 1 year": 0,
        "n/a": 0
    }
}

loans = loans.drop(["last_credit_pull_d", "earliest_cr_line", "addr_state", "title"], axis=1)
loans["int_rate"] = loans["int_rate"].str.rstrip("%").astype("float")
loans["revol_util"] = loans["revol_util"].str.rstrip("%").astype("float")
loans = loans.replace(mapping_dict)

## 8. Dummy variables ##

cat_cols = ['home_ownership', 'verification_status', 'purpose', 'term']
#[loans[col] = loans[col].astype(category) for col in cat_cols]
dummy_df = pd.get_dummies(loans[cat_cols])
loans = pd.concat([loans, dummy_df], axis=1)
loans = loans.drop(cat_cols, axis=1)

