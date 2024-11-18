import pandas as pd 

data = {"Fruits" : ["Mango", "Banana" , "Apple"],
        "Price" : [ 250,100,320],
        "Quantity" : [12,10,32]}

df1 = pd.DataFrame(data)
df2 = df1.copy()

#Lets Change the value of df2 content to compare both data frame 

df2.loc[0 , "Price"] = 260  # 0 index of price ke value ko change krega df2 me 
df2.loc[2, "Price"] = 360 

df2.loc[0,"Quantity"] = 10 #0 index of quantity ke value ko change krega df2 me 
df2.loc[2,"Quantity"] = 30

# Set 'Fruits' column as index
df1.set_index("Fruits", inplace=True) #sets the Fruits column as the index. This ensures the fruit names are used as row labels in the output.
df2.set_index("Fruits", inplace=True)

print(df1.compare(df2, keep_shape=True)) #retains the original shape, showing NaN for unchanged rows and columns.
