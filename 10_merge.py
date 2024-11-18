import pandas as pd

data1 = {
    "EMP_ID" : [ 'E01' , "E02" , "E03" , "E04" , "E05"],
    "Name" : ["shivam" ,"rahul", "pintu", "chintu" , "mohan"],
    "Age" : [25,18,25,35,34],
   
    }

data2 = { "EMP_ID" : [ 'E01' , "E02" , "E03" , "E04" , "E05"],
    
    "salary" : [25000,35000,42000,58000,25600]
    }

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print(pd.merge(df1,df2, on="EMP_ID" ).to_string(index=False))