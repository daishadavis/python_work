def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} as about {num_words} words.")


filenames = ['files_exceptions/alice.txt', 'files_exceptions/siddhartha.txt', 'files_exceptions/moby_dick.txt', 'files_exceptions/little_women.txt']
for filename in filenames:
    count_words(filename)