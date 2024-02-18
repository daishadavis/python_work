def make_shirt(message, size='large'):
    """Displaying information about a t-shirt order"""
    print(f"Your ordered a {size.title()} t-shirt with the message {message} printed.")

make_shirt('I Love Python.')
make_shirt('I Love Python', 'medium')
make_shirt('I am ready to party', 'small')