import pandas as pd

df = pd.read_csv("students.csv")

corr = df.corr(numeric_only=True)
print(corr)
