# Writing to a file
with open('my_file.txt', 'w') as f:
    f.write('Hello, Python!\n')
    f.write('This is a new line.')

# Reading from a file
with open('my_file.txt', 'r') as f:
    content = f.read()
    print(content)