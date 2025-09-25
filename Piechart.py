import matplotlib.pyplot as plt

categories = ['sports', 'Music', 'Dance', 'Art']
values = [20, 15, 30, 35]
plt.pie(values, labels=categories, autopct='%1.1f%%',
        startangle=90, colors=['lightcoral', 'gold', 'lightgreen', 'skyblue'],
        explode=(0, 0.1, 0, 0))  # Highlight 'Music'

plt.title("Student Intrest in Activities")

plt.show()