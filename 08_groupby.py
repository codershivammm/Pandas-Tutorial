import pandas as pd

data = {
    'Team': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Points': [10, 15, 10, 20, 10, 30],
    'Assists': [5, 7, 8, 6, 5, 9]
}

df = pd.DataFrame(data)
#print(df)

print (df.groupby("Team").agg({"Points" : ["sum" , "mean"]})) #Team column me points ka sum and means groupby kar rha hai
print(df.groupby("Team").agg({"Points" : "max"}))