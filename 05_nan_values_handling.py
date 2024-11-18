import pandas as pd
import numpy as np

data = pd.read_excel("Deal with NAN Values.xlsx")

print(data.isnull().sum()) # shows the null value in all column
print(data["salary"].isnull().sum()) #shows the number of null value in all column

print(data["salary"].replace(np.nan , "23587"))  #Replace null value only in salary column with "23587 which is mean"
#print(data.replace(np.nan , "hi"))      #Replace  all null values  with "hi"

print(data["salary"].mean())