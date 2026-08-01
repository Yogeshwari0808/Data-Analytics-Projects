#Read the CSV file into a DataFrame.
import pandas as pd
df = pd.read_csv("Employee_Data_Analytics.csv")
print(df)

#Display the first 5 rows.
f_rows = df.head(5)
print(f_rows)

# Display the last 5 rows.
l_rows = df.tail(5)
print(l_rows)


#Check the shape of the dataset.
shapeOfDataSet = df.shape
print(shapeOfDataSet)

# Display the column names.
columnName = df.columns
print(columnName)

# Display dataset information using info().
df.info()

#Display statistical summary using describe().
statistical_summary = df.describe()
print(statistical_summary)

#Find the total missing values in each column.
t_missing_values = df.isnull().sum() 

#Fill missing values in the Salary column with the average salary.

df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
print(df["Salary"])

# Find the employee with the highest salary.
highest_salary = df.sort_values( by= "Salary",ascending=False).head(1)
print(highest_salary)

#Find the employee with the lowest salary.
lowest_salary = df.sort_values( by= "Salary",ascending=True).head(1)
print(lowest_salary)

# Find the average salary of all employees.
print(f"Average salary of employees : {df["Salary"].mean()}")

# Display employees whose salary is greater than 50,000.
print(df.loc[df["Salary"]>50000,"Name"])

# Display only the Name and Salary columns.
print(df[["Name","Salary"]])


# Sort employees by salary in descending order.
sorted_data = df.sort_values(by="Salary",ascending=False)
print(sorted_data)

# Find the average salary department-wise.
grouped = df.groupby("Department")["Salary"].mean()
print(grouped)

# grouped = df.groupby("Department").agg(avg_salary = ("Salary","mean"))
print(grouped)

# Count the number of employees in each department.
total_employees = df.groupby("Department")["Name"].count()
print(total_employees)


# Find the employee with the highest experience.
highest_experience = df.sort_values(by="Experience", ascending=False).head(1)
print(highest_experience)
#OR
highest_experience = df.loc[df["Experience"].idxmax()]
print(highest_experience)

# Create a new column Annual Salary (Salary × 12).
df["Annual_Salary"] = df["Salary"]*12

print(df)

# Find the total salary paid department-wise.

grouped = df.groupby("Department")["Salary"].sum()
print(grouped)

# Find the maximum salary in each department.
max_salary = df.groupby("Department")["Salary"].max()
print(max_salary)
#OR
max_salary_for_each = df.groupby("Department").agg(max_salary=("Salary","max"))
print(max_salary_for_each)

# Find the minimum salary in each department.
min_salary = df.groupby("Department")["Salary"].min()
print(min_salary)

# Find all employees whose experience is greater than 3 years.
print(df[df["Experience"]>3])

condition = df.loc[df["Experience"]>3,["Name","Experience"]]
print(condition)

# Display all employees from the IT department.
display = df[df["Department"] == 'IT']
print(display)

# Find the number of unique departments.
unique_d = df["Department"].nunique()
print(unique_d)

# Rename the Salary column to Monthly Salary.
df.rename(columns={"Salary":"Monthly Salary"},inplace=True)
print(df)
df.to_csv("cleanData.csv",index = False)

