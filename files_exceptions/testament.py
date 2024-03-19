filename = 'files_exceptions/old_testament.txt'

with open(filename) as f:
    contents = f.read()

words = contents.count('God')
print(f"the word 'God' appears {words} times.")
