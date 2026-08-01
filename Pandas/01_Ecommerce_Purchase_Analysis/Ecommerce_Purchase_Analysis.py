import pandas as pd
df= pd.read_csv("Ecommerce Purchases.csv")

# 1. Display Top 10 Rows of The Dataset
first_rows = df.head(10)
# print(first_rows)

#2. Check Last 10 Rows of The Dataset
last_rows = df.tail(10)
# print(last_rows)

#3. Check Datatype of Each Column
print(df.info())
print(df.dtypes)

# 4. Check null values in the dataset
print(df.isnull())
print(df.isnull().sum())

# 5. How many rows and columns are there in our Dataset? 
print(df.shape)

# 6. Highest and Lowest Purchase Prices.
print(f"Highest Price is {df['Purchase Price'].max()}")
print(f"Lowest Price is {df['Purchase Price'].min()}")

# 7. Average Purchase Price
avg_price = df["Purchase Price"].mean()
print(f"Average Purchase Price is : {avg_price}")

#8. How many people have French 'fr' as their Language?
print(df["Language"].value_counts()["fr"])

#9. Job Title Contains Engineer
print(df[df["Job"].str.contains("engineer",case=False)])

# 10. Find The Email of the person with the following IP Address: 132.207.160.22
print(df[df["IP Address"] == '132.207.160.22']["Email"])

#11. How many People have Mastercard as their Credit Card Provider and made a purchase above 50?
print(len(df[(df["CC Provider"] =='Mastercard') & ( df["Purchase Price"]>50)]))

# 12. Find the email of the person with the following Credit Card Number: 4664825258997302
print(df[df["Credit Card"] == 4664825258997302]["Email"])

#13. How many people purchase during the AM and how many people purchase during PM?
am = len(df[df["AM or AM"]=='AM'])
pm = len(df[df["AM or PM"]=='PM'])

print(f"Total number of people who purchase in AM : {am}")
print(f"Total number of people who purchase in AM : {pm}")
#Alternative Solution
print(df["AM or PM"].value_counts())

# 14. How many people have a credit card that expires in 2020?

print(df[df["CC Exp Date"].str.contains("20")].count())
# Alternative Solution
# len(df[df["CC Exp Date"].apply(lambda x : x[3: ] == '20')])

# 15. What are the top 5 most popular email providers (e.g. gmail.com, yahoo.com, etc...) 

list1 = []

for email in df['Email']:
  list1.append(email.split('@')[1])

df['temp'] = list1

print(df['temp'].value_counts().head(5))

# Alternative Solution

print(df["Email"].apply(lambda x : x.split('@')[1]).value_counts().head(5))
