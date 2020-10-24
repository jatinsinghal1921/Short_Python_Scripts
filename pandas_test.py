import os
import pandas as pd


df = pd.read_excel("Book1.xlsx",sheet_name = "Sheet1")
#print(df)


# See Specific Columns
number1 = df["Numbers"]
number2 = df.Numbers
#print(number1)
#print(number2)


# See List of Specific Columns
number_list = df[["Numbers","Category"]]
#print(number_list)


# create a Sliced DF
df1 = df.iloc[5:8][:]
#print( "df1 : \n" ,df1)

#print("*******************************")

df2 = df1.iloc[:2][:]
#print("df2 : \n", df2)

############ Learning : Always Use df.iloc[] for accessing rows, indexing starts from 0. Even if you slice df then the obtained df indexing will start from 0.


# print via skipping 
#print(df[::2])


# Revese Print the row entries of DF.
#print(df[-4::-1])


# Fetching only filtered Data
filter_criteria = df["Numbers"] > 5
print(df[filter_criteria])