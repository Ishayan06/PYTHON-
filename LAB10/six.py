import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")

plt.bar(df["name"], df["marks"])
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.title("Student Marks Bar Chart")
plt.show()
