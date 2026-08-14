from pyparsing import line


data = open(r"C:\Users\uthay\OneDrive\Documents\MSC800\week3\junk.txt")
lines = data.readlines() # Get a list of all the lines in the file
print(lines) # Print the list of lines
#print total number of lines in the file
print(f'Total number of lines in the file: {len(lines)}')
#total number of different flowers available 
different_flowers = set(line.split(',')[0] for line in lines)
print(f'Total number of different flowers in the dataset: {len(different_flowers)}')
#name  different flowers in the dataset
flower_names = set(line.split(',')[0] for line in lines)
print(f'Flower names in the dataset: {flower_names}')
data.close()