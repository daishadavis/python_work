filename = 'files_exceptions/learning_python.txt'

with open(filename) as file_object:
    content = file_object.readlines()
    for line in content:
        line = line.replace('Python', 'C')
        print(line.strip())