import pandas as pd
import os

# File name
filename = "Students.csv"

# Step 1: Create CSV if it doesn't exist
if not os.path.exists(filename):
    data = {
        "Roll": [101, 102, 103, 104, 105],
        "Name": ["Alice", "Bob", "Charlie", "David", "Emma"],
        "Marks": [85, 90, 78, 92, 88]
    }
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)  # comma-separated by default
    print("✅ Students.csv created successfully!\n")
else:
    df = pd.read_csv(filename)
    print("📂 Found existing Students.csv\n")

# Step 2: Display data
print("First 5 rows of the DataFrame:")
print(df.head().to_string(index=False))

print("\nLast 5 rows of the DataFrame:")
print(df.tail().to_string(index=False))

print("\nSummary statistics:")
print(df.describe())

# Step 3: Add new student
print("\n--- Add New Student ---")
roll = int(input("Enter Roll Number: "))
name = input("Enter Name: ")
marks = int(input("Enter Marks: "))

new_student = pd.DataFrame({"Roll": [roll], "Name": [name], "Marks": [marks]})
df = pd.concat([df, new_student], ignore_index=True)

# Step 4: Save updated CSV
df.to_csv(filename, index=False)

# Step 5: Show updated DataFrame
print("\nUpdated Students Data:")
print(df.to_string(index=False))
