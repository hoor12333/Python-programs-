import matplotlib.pyplot as plt

# Sample data
students = ["Alice", "Bob", "Charlie", "David", "Eva"]
marks = [85, 72, 90, 66, 95]

# Plot line chart
plt.plot(students, marks, marker='o', linestyle='-', color='b')

# Labels and title
plt.title("Student Marks - Line Chart")
plt.xlabel("Students")
plt.ylabel("Marks")

# Show chart
plt.show()
