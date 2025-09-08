with open("Students.txt", "w") as file:
    file.write("Alicen\n")
    file.write("bob\n")
    file.write("Charlie\n")
    file.write("David\n")
    file.write("Emma\n")

with open("Students.txt", "r") as file:
    content = file.read()

print("student names from the file:")
print(content)