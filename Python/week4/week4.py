#Reading a file
with open('file1.txt','r') as file:
   print(file.read()) 
#Writing a modified version to a new file
with open('file2.txt','w') as file:
    file.write("Holla monsiour")
    
#Error handling
filename = input("Enter a file name:")
try:
    with open(filename, 'r') as file:
        print(file.read())
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")