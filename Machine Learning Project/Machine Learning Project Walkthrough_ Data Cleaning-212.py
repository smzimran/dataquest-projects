## 3. Reading in to Pandas ##

import pandas as pd

loans_2007 = pd.read_csv('loans_2007.csv')
print(loans_2007.iloc[0])
print(loans_2007.shape[0])

## 5. First group of columns ##

loans_2007 = loans_2007.drop(["id", "member_id", "funded_amnt", "funded_amnt_inv", "grade", "sub_grade", "emp_title", "issue_d"], axis=1)

## 7. Second group of features ##

loans_2007 = loans_2007.drop(["zip_code", "out_prncp", "out_prncp_inv", "total_pymnt", "total_pymnt_inv", "total_rec_prncp"], axis=1)

## 9. Third group of features ##

loans_2007 = loans_2007.drop(["total_rec_int", "total_rec_late_fee", "recoveries", "collection_recovery_fee", "last_pymnt_d", "last_pymnt_amnt"], axis=1)
print(loans_2007.iloc[0])
print(loans_2007.shape[1])

## 10. Target column ##

loans_2007.loan_status.value_counts()

## 12. Binary classification ##

loans_2007 = loans_2007[(loans_2007['loan_status']=='Fully Paid') | (loans_2007['loan_status']=='Charged Off')]
status_replace = {'loan_status':{'Fully Paid': 1, 'Charged Off': 0}}
loans_2007.replace(status_replace, inplace=True)

## 13. Removing single value columns ##

drop_columns = []
for col in loans_2007.columns:
    if len(loans_2007[col].dropna().unique())==1:
        drop_columns.append(col)
        
loans_2007.drop(drop_columns, axis=1, inplace=True)
print(drop_columns)
        
