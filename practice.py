string = 'Hello, my name is tittys.'
ignore = [',', '"', '.']
new = []

for l in string:
    letter = l.lower()
    if letter in ignore:
        letter = letter.replace(letter, '')
    new.append(letter)
    updated = ''.join(new)
    print(updated)

