import pandas as pd
from pandas.core.algorithms import value_counts
df=pd.read_csv("pokemon_data.csv")
# print(df.loc[(df["Name"].str.contains("Mega"))])

# update column value
# df.loc[df["Type 1"]=="Fire","Type 1"]="Flamer"

# add column in df on condition (for fire type it will create a series named legendary and add true if not then false to that row)
# df.loc[df["Type 1"]=="Fire","Leendary"]=True

# modifiy multiple column on condition
# df.loc[df["Total"]>500,["Generation","Legendary"]]=True

#grouby conditions
# print(df.groupby(["Type 1"]).mean().sort_values("Defense",ascending=False).head(50))
# print(df.groupby(["Type 1"]).count());
print(df.groupby(["Type 1","Type 2"]).max())
