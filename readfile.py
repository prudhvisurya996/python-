# Open the file in read mode ('r' stands for rea
file_path = r'C:/Users/prudh/python-/file1.txt'
 # Replace with the path to your file
with open(file_path, 'r') as file:
    # Read the entire contents of the file
    content = file.read()
    print(content)

'''
output 
PS C:\Users\prudh\python-> & C:/Users/prudh/AppData/Local/Programs/Python/Python311/python.exe c:/Users/prudh/python-/readfile.py
I am Prudhvi surya
Created this file to read its content

'''
