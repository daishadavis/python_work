filenames = ['files_exceptions/the_great_gatsby.txt', 'files_exceptions/sherlock_holmes.txt', 'files_exceptions/dracula.txt']


for filename in filenames:
    try:
     with open(filename, encoding='utf-8') as f:
        contents = f.read()
    except FileNotFoundError:
       print(f"I'm sorry {filename} does not exist")
    else:
       words = contents.count('the ')
       print(f"For {filename} the word 'the' appears {words} times.")