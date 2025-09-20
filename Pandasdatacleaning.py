import pandas as pd

# Sample data
data = {
    'Name': ['Alice', 'Bob', None, 'David', 'Eva'],
    'Age': [25, None, 30, 22, 28],
    'City': ['New York', 'Los Angeles', 'Chicago', None, 'Houston']
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)
df_drop = df.dropna()
print("\nDataFrame after dropping rows with missing values:\n", df_drop)
df_fill = df.fillna({'Name': 'Unknown', 'Age': df['Age'].mean(), 'City': 'Unknown'})
print("\nDataFrame after filling missing values:\n", df_fill)
df_rename = df.rename(columns={'Name': 'Full Name', 'Age': 'Age in Years', 'City': 'City of Residence'})
print("\nDataFrame after renaming columns:\n", df_rename)
df_filtered = df_rename[df_rename['Age in Years'] > 24]
print("\nFiltered DataFrame (Age > 24):\n", df_filtered)