import pandas as pd
import matplotlib.pyplot as plt
import os

# Read CSV
df = pd.read_csv("student_data.csv")
df["Average"] = df[["Math", "Physics", "Chemistry"]].mean(axis=1)

# Print basic stats
print("Average Marks:\n", df["Average"])
print("Top Scorer:\n", df.loc[df['Average'].idxmax()])
print("Lowest Scorer:\n", df.loc[df['Average'].idxmin()])

# Create output folder
os.makedirs("output_charts", exist_ok=True)

# Bar chart
plt.figure(figsize=(10,5))
plt.bar(df["Name"], df["Average"], color='skyblue')
plt.title("Average Marks of Students")
plt.xlabel("Name")
plt.ylabel("Average Marks")
plt.savefig("output_charts/average_marks_bar.png")
plt.close()

# Pie chart
subject_totals = df[["Math", "Physics", "Chemistry"]].sum()
plt.figure(figsize=(6,6))
plt.pie(subject_totals, labels=subject_totals.index, autopct='%1.1f%%')
plt.title("Total Marks Distribution by Subject")
plt.savefig("output_charts/subject_distribution_pie.png")
plt.close()