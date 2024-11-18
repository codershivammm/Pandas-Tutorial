import pandas as pd

data1 = {
    "EMP_ID" : [ 'E01' , "E02" , "E03" , "E04" , "E05"],
    "Name" : ["shivam" ,"rahul", "pintu", "chintu" , "mohan"],
    "Age" : [25,18,25,35,34],
   }

data2 ={ "EMP_ID" : [ 'E06' , "E07" , "E08" , "E09" , "E10"],
    "Name" : ["jaiswal" ,"pintuiu", "golu", "sona" , "mona"],
    "Age" : [25,18,25,35,34],
   }
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print(pd.concat([df1,df2]).to_string(index=False))