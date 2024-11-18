import pandas as pd
data = pd.read_excel("Assests/10 Emp Details.xlsx")

#retrieves the maximum salary.
max_salary = data["salary"].max()

#filters the DataFrame for employees with that salary.
max_salary_employee_details = data[data["salary"] == max_salary]

print(max_salary_employee_details.to_string(index = False)) #prints all the details of emp with max salary