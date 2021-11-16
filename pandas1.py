import pandas as pd
car=['bmw','mercedes','volvo','lanborghini'];
dict1={
    'cars':list(x for x in car),
    'passings':list(x for x in range(8) if x%2==0)
}
# print(dict1);
# print(dict1['cars']);
# print(dict1['passings']);

df1=pd.DataFrame(dict1,index=['day1','day2','day3','day4']);


print(df1.to_string())
print(df1.loc['day1']);
print(df1.loc[['day1','day2','day3']])

# print(df1.loc[0])
# print(df1.loc[[0,2]])

# print(pd.__version__)

