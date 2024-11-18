import pandas as pd

data = {
    "EMP_ID" : [ 'E01' , "E02" , "E03" , "E04" , "E05"],
    "Name" : ["shivam" ,"rahul", "pintu", "chintu" , "mohan"],
    "Age" : [25,18,25,35,34],
   }

df = pd.DataFrame(data)

print(df)
print(df.T) #It will Transpose the data frame rows becomes columns and columns becomes rows