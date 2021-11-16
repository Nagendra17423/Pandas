import pandas as pd
df1=pd.read_csv("pokemon_data.csv")
# to show multiple useful information abt the dataset like mean median mode  avg count max 
# print(df1.describe())

# acsening order on column name
# print(df1.sort_values("Name",ascending=False).head())

# descending order on column name
# print(df1.sort_values("Name",ascending=False).head())

# sort df  on multiple column attribute 
# df.sort_values(["Name","HP"])

# sort df on multiple column and along with it on different fashion
# i.e name acsening type 1 descening etc
# df.sort_values(['Name','Type 1'],ascending=[1,0])

# print(df1.head())

#add rowise content of columns to and store it in different column created
# df1['Total']=df1['Attack']+df1['Defense'];
# print(df1.head())
# df1=df1.drop(columns='Total')
# print(df1.head())




