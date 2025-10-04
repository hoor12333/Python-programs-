import pandas as pd 

students = pd.DataFrame({
    'student_id': [1, 2, 3, 4, 5],
    'student_name': ['alice', 'bob', 'charlie', 'david', 'eva']
})
marks = pd.DataFrame({
    'student_id': [1, 2, 3, 4, 5],
    'subject': ['math', 'science', 'history', 'math', 'science'],
    'score': [85, 90, 78, 92, 88]
})
merged_df = pd.merge(students, marks, on='student_id')
print("===Students Data ===")
print(students)
print("\n===Marks Data ===")
print(marks)
print("\n===Merged Data ===")
print(merged_df)
