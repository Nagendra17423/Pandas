import pandas as pd
df=pd.read_csv("pokemon_data.csv")
# print(df.head())
# print(df.columns,df.index);
# for col in df.columns:
#     print(col,df[col])
# for col in df.index:
#     print(df.loc[col])

# print(df.Name.tail())
# print(df[['Name','Type 1','HP']])
# print(type(df['Name']))
# print(df['Name'])

# a=max(df['HP'])
# for index in df.index:
#     if a == df.loc[index]['HP']:
#         print(df.loc[index])


# get multiple rows of a data frame
# print(df.loc[0:2])

# specific row specific values of a column
# print(df.iloc[0,1])

# iterate over row using iterrows() specific rows and as well spefici column of a particular row.
# iterrows returns tuple (index,row) index value and row content 
# for index,row in df.iterrows():
#     print(row[:])
    # print(index,row['Name'])

# iteritem return tuple containign index and series value i.e(whole column value)
# for see in df.iteritems():
#     print(see[:])

# df.itertuple return index and row content as tuple
# for see in df.itertuples():
#     print(see[:])

# print(df.loc[df['Type 1']])

'''
loc can be used situation where u want to access row/col with labels or integer and update it and as well situation where
u want to conditional updation needed to be performed  like below..
'''
# df.loc[0:4] can be used to print 0 to 4 row index 
# df.loc[df['Type']=='Fire'] print rows which have Fire type
# df.loc[df['type']=='Fire' and df['#']>720]
# print(df.loc[(df['Type 1']=='Fire') & (df['#']>720)])


# df.loc[(df["Type 1"]=='Fire',['HP'])]=1000
# print(df.loc[df['Type 1']=='Fire'])
# print(df.loc[(df["Type 1"]=='Grass') & (df['Type 2']=='Ice')])
