import pandas as pd
import numpy as np

ser = pd.Series(np.random.rand(10))
#print (ser)

df = pd.DataFrame(np.random.rand(10, 5) , index=np.arange(1,11) , columns= ["number 1 " ,"number 2 ","number 3 ","number 4 ", "number 5"]) #generate df of 10 rows and 5 columns with random numbers 
print(df)

print(df.loc[[5] , ["number 5"]]) #Gives the 5th index and 5th column i.e number 5 values 
print(df.loc[[3]])   # 3rd Index ke Saare Values ko Dikhayega

print(df.iloc[0,3]) # 0 index of Rows and 3rd Index of Columns ke value ko Direct Print Kar dega
