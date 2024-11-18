import pandas as pd

#Creating Data Frame
data = {"Name" : ["Shivam" , "Dev" , "Satyam" , "Rahul"],
        "Age" : [25,24,26,12],
        "Salary" : [ 20000,5000,12000,15000]}
df = pd.DataFrame(data)
#print(df)

#Load Data from csv file
try:
  data = pd.read_csv("pizza_types.csv" ,encoding='ISO-8859-1')
  #print(data)
except FileNotFoundError:
  print("Sorry File Not Found")

#Load Data From Excel File.
try :
  data = pd.read_excel("Customers.xlsx")
  print (data)
except FileNotFoundError:
  print("Sorry File Not Found")