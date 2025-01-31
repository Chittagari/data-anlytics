import pandas as pd
df=pd.read_csv(r"C:/Users/arunk/Downloads/wine+quality/winequality-red.csv")
print(df.describe())
print(pd.isna(df)) 
