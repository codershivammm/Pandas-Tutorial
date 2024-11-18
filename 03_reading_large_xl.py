import pandas as pd

data = pd.read_excel("500_Customers.xlsx")
#print (data) #this will nly give by default top 5 and last 5 rows data 

#If you want desired rows data 

#print (data.head(10))      #will give top 10 rows data inexing 0 to 9
#print(data.tail(10))       #will give last 10 rows data 
#print(data.iloc[10:13])    #will give 10th to 12th rows data indexing 10th to 12

#print(data.info())
print(data.describe())       #describe the data mean minimum maximum and many things