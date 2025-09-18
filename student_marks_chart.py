import  pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("marks.csv")
names = data["Name"]
marks = data["Marks"]
plt.figure(figsize=(8, 5))
plt.bar(names, marks, color='skyblue', edgecolor='black', width=0.6)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()