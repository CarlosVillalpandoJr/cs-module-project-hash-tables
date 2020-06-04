def no_dups(s):
    table = {}
    solution_list = []
    word_list = s.split(' ')
    for word in word_list:
        if word in table:
            table[word] += 1
        else:
            table[word] = 1
    for key, value in table.items():
        if value is not 1:
            pass
        else:
            solution_list.append(key)
    return ' '.join(solution_list)



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))