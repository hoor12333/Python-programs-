import os

# Step 1: List files in current directory
print("Current Directory:", os.getcwd())
print("Files/Folders:", os.listdir(os.getcwd()))

# Step 2: Create a folder
folder_name = "MyNewFolder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Folder '{folder_name}' created!")
else:
    print(f"Folder '{folder_name}' already exists.")

# Step 3: Delete the folder
if os.path.exists(folder_name):
    os.rmdir(folder_name)
    print(f"Folder '{folder_name}' deleted!")
else:
    print(f"Folder '{folder_name}' does not exist.")
