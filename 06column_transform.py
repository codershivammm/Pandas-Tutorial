import pandas as pd

data = pd.read_excel("10 Emp Details.xlsx")


data["Full name"] = data["First Name"] + data["Last Name"]  
#print(data.to_string(index=False))     #concatenate the first and last name column and creates a new column of full  name

data["Bonus"] =   (data["salary"]/100)*20
print(data.to_string(index=False))

