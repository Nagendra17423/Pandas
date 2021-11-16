import pandas as pd
from pandas.core import indexing
df=pd.read_csv("pokemon_data.csv")
# print(df.head())

df['total']=df.iloc[:,4:10].sum(axis=1);

# print(df.head())
# print(type(df.columns.values))
# print(df[0:4])
# print(df.iloc[:,0:4])
# reordering of columsn..
# df1=df[(df[0:4])+df[-1]+df[4:])]
col=list(df.columns.values)
# print(col[0:4]+ col[-1] + col[4:])
print(type(col[0:4]))
print(type(col[-1]))
print(type(df['total']))
print(type(col[4:]))
df1=df[ col[0:4]+ ['total'] + col[4:] ]
df1.head()
print(df1.head())
# save dataframe with index 
df1.to_csv("saved_data.csv");
# save dataframe without indexing
df1.to_csv("without_index.csv",index=False);
# in any fromat
df1.to_csv("any_form.txt",index=False,sep='\t')
