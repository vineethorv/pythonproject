import pandas as pd

df = pd.read_csv(r'C:\Users\vinee\Desktop\sampletest.csv')
print(df[["Name", "Marks"]])
print(df.head(3))
print(df.loc[0:1])
#df.dropna()
