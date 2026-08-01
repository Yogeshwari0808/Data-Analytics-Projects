import pandas as pd
df = pd.read_csv("Salaries.csv")

# 1.  Display Top 10 Rows of The Dataset
print(df.head(10))

#2. Check Last 10 Rows of The Dataset
print(df.tail(10))

#3. Find Shape of Our Dataset (Number of Rows And Number of Columns)
print(df.shape)

# 4.  Getting Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement
df.info()

#5. Check Null Values In The Dataset
print(df.isnull().sum())

#6. Drop ID, Notes, Agency, and Status Columns 
df.drop(columns = ["Id","Notes","Agency","Status"],inplace=True)
print(df.head(5))
#OR
df = df.drop(columns = ["Id","Notes","Agency","Status"])
df = df.drop(["Id","Notes","Agency","Status"],axis=1)
print(df)

#7. Get Overall Statistics About The Dataframe
print(df.describe(include='all'))

#38. Find Occurrence of The Employee Names  (Top 5)
print(df["EmployeeName"].value_counts().head(5))

#9. Find The Number of Unique Job Titles
print(df["JobTitle"].nunique())

#10.Total Number of Job Titles Contain Captain
print(len(df[df["JobTitle"].str.contains('Captain',case = False )]))

#11. Display All the Employee Names From Fire Department
print(df[df['JobTitle'].str.contains('Fire',case=False)]['EmployeeName'])


#12. Find Minimum, Maximum, and Average BasePay
print(df.describe())

#13. Replace 'Not Provided' in EmployeeName' Column to NaN 
df["EmployeeName"]=df["EmployeeName"].replace('Not provided',None)

#14. Drop The Rows Having 5 Missing Values
print(df.drop(df[df.isnull().sum(axis=1)==1].index))

#15. Find Job Title of ALBERT PARDINI
print(df[df['EmployeeName'] == 'ALBERT PARDINI']['JobTitle'])

#16. How Much ALBERT PARDINI Make (Include Benefits)?
print(df[df['EmployeeName'] =='ALBERT PARDINI']['TotalPayBenefits'])

#17.Display Name of The Person Having The Highest BasePay
df['BasePay'] = pd.to_numeric(df["BasePay"],errors='coerce')
print(df[df['BasePay'].max()==df["BasePay"]]['EmployeeName'])

# 18.Find Average BasePay of All Employee Per Year 
print(df.groupby("Year")['BasePay'].mean())

#19. Find Average BasePay of All Employee Per JobTitle 
print(df.groupby('JobTitle')['BasePay'].mean())

#20. Find Average BasePay of Employee Having Job Title ACCOUNTANT  
print(df[df['JobTitle'] == 'ACCOUNTANT']['BasePay'].mean())

#21. Find Top 5 Most Common Jobs
print(df["JobTitle"].value_counts().head(5))

#22.Which department has the highest average BasePay?
print(df.groupby('JobTitle')['BasePay'].mean().max())
print(df.groupby('JobTitle')['BasePay'].mean().sort_values(ascending=False).head(10))

#23.Which year has the highest average TotalPay?
print(df.groupby('Year')['TotalPay'].mean().max())

#24.Top 10 employees with highest TotalPay.
print(df.groupby('EmployeeName')['TotalPay'].sort_values(ascending = False).head(10))// can't use direct sort values after group by
print(df.sort_values(by='TotalPay',ascending=False)[['EmployeeName','TotalPay']].head(10))

# 25.Count employees in each Job Title
print(df['JobTitle'].value_counts())

#26.Which JobTitle appears the most?
print(df['JobTitle'].value_counts().head(1))