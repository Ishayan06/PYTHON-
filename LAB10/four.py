import pandas as pd

df = pd.read_csv("students.csv")

filtered_df = df[df["marks"] > 60]
print(filtered_df)
