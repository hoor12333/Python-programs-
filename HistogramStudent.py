import matplotlib.pyplot as plt

# Sample student marks
marks = [45, 55, 60, 62, 65, 70, 72, 75, 78, 80,
         82, 85, 88, 90, 92, 95, 96, 98, 100, 100]

# Create histogram
plt.hist(marks, bins=10, color='skyblue', edgecolor='black')

# Add labels and title
plt.title("Histogram of Student Marks")
plt.xlabel("Marks Range")
plt.ylabel("Number of Students")

# Show grid
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
