import pandas as pd

data = {
    "Product": ["A", "A", "B", "B"],
    "Region": ["North", "South", "North", "South"],
    "Sales": [100, 200, 150, 250]
}

df = pd.DataFrame(data)
print(df.pivot(index = "Product" ,columns= "Region" , values="Sales"))
