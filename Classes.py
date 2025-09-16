class Student:
    def __init__(self, name, marks):
        self.name = name      # attribute
        self.marks = marks    # attribute

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 40:
            return "D"
        else:
            return "F"

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}, Grade: {self.calculate_grade()}")


# Create objects (instances)
s1 = Student("Alice", 92)
s2 = Student("Bob", 76)
s3 = Student("Charlie", 35)

# Call methods
s1.display()
s2.display()
s3.display()
