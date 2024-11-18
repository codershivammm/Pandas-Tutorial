'''import pandas as pd

number = list(range(1,5))
data = {
    "S.NO" : number,
    "Months" : ["January" , "February" , "March" , "April"]}

df = pd.DataFrame(data)

def extract (value):
    return value[0:3]

df["Short_name"] = df["Months"].map(extract)
print (df)'''

# ANOTHER METHOD

import pandas as pd

number = list(range(1,5))
data = {
    "S.NO" : number,
    "Months" : ["January" , "February" , "March" , "April"]}

df = pd.DataFrame(data)

short_names = []

for month in df["Months"]:
    short_names.append(month[0:3])

df["Short Names"] = short_names

print(df)