import pandas as pd
import sqldf

# import pyarrow as pq
df = pd.read_parquet(r'C:\Users\vinee\Downloads\userdata1.parquet')
query = """SELECT first_name FROM df LIMIT 5 """
df1 = sqldf.run(query)
print(df1)
# df2 = df1.values.tolist();
# print(df2)

res = []
for column in df1.columns:
    li = df[column].tolist()
    res.append(li)

print(res)
