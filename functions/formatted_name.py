def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formated"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musican = get_formatted_name('john', 'hooker')
print(musican)