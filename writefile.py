# Open the file in write mode ('w' stands for write)
file_path = 'output.txt'  # Replace with the desired file path
with open(file_path, 'w') as file:
    # Write content to the file
    file.write("Hello, World!\n")
    file.write("This is a line written to the file.")
