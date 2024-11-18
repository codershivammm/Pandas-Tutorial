import pandas as pd
from faker import Faker

faker =Faker()


numbers = list(range(1,101))

data = {
    "S.No" : numbers,
    "EMP_ID" : [faker.random_int(min = 100 , max = 500) for _ in range (100)],
    "Name" : [faker.name()for _ in range (100)],
    "Age" : [faker.random_int(min= 25, max = 60) for _ in range (100)],
    "salary" : [faker.random_int(10000,50000) for _ in range(100 ) ] 
    }

df =pd.DataFrame(data)

df.to_excel("500 Emp Details.xlsx" ,index=False)