import pandas as pd
df = pd.read_excel("500 Emp Details.xlsx")

print(df.duplicated("EMP_ID").sum()) #this will show the total duplicated rows under EMP_ID column

print(df.drop_duplicates("EMP_ID").to_string(index=False)) #remove all the duplicates values from EMP ID COlumn

