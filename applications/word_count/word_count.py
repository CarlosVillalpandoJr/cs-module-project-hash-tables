ignore = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
def word_count(s):
    new = []
    for l in s:
        letter = l.lower()
        if letter in ignore:
            letter = letter.replace(letter, '')
        new.append(letter)
    updated = ''.join(new).split(' ')
    return tableHelper(updated)

def tableHelper(list):
    table = {}
    for word in list:
        if word in table:
            table[word] += 1
        else:
            table[word] = 1
    return table


        



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))