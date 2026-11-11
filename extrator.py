def read_file():
    # TODO: replace with a function to read the site, for developing reasons started as a file to be read
    with open('site.html', 'r', encoding='utf-8') as file:
        content = file.read()

    return content